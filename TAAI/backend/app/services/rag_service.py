"""RAG (Retrieval-Augmented Generation) Service"""

from typing import List, Dict, Any
from langchain.chat_models import AzureChatOpenAI
from langchain.embeddings import AzureOpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, SystemMessage
import tiktoken

from app.core.config import settings
from app.core.logging import logger
from app.services.search_service import SearchService
from app.models.chat import ChatResponse, Source


class RAGService:
    """RAG orchestration service for Tech Assist AI"""

    def __init__(self):
        self.llm = None
        self.embeddings = None
        self.search_service = SearchService()
        self.encoder = tiktoken.encoding_for_model("gpt-4")

        # System prompt
        self.system_prompt = """You are Tech Assist AI (TAAI), Macquarie Group's intelligent tech support assistant.

Your role:
- Provide accurate, helpful answers to IT and tech questions
- Use ONLY the information from the provided context
- If you don't know something, admit it and suggest escalating to Tech Assist
- Be concise but complete (aim for 3-5 sentences)
- Always include source citations
- Use a friendly, professional tone
- Prioritize security and compliance

Response guidelines:
1. Start with a direct answer to the question
2. Provide step-by-step instructions if applicable
3. Mention any prerequisites or requirements
4. Note if the user needs special permissions
5. End with source citations

If the question is outside your knowledge or requires human judgment:
- Clearly state you don't have enough information
- Suggest escalating to Tech Assist
- Provide the Tech Assist contact options

Context from internal knowledge base:
{context}

Remember:
- Never make up information
- Never share sensitive data like passwords
- Never bypass security protocols
- Always cite your sources"""

    async def initialize(self):
        """Initialize Azure OpenAI and embedding models"""
        try:
            # Initialize LLM
            self.llm = AzureChatOpenAI(
                deployment_name=settings.AZURE_OPENAI_DEPLOYMENT_NAME,
                model_name="gpt-4",
                temperature=settings.TEMPERATURE,
                max_tokens=settings.MAX_TOKENS,
                azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
                api_key=settings.AZURE_OPENAI_API_KEY,
                api_version=settings.AZURE_OPENAI_API_VERSION
            )

            # Initialize embeddings
            self.embeddings = AzureOpenAIEmbeddings(
                deployment=settings.AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
                model="text-embedding-ada-002",
                azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
                api_key=settings.AZURE_OPENAI_API_KEY,
                api_version=settings.AZURE_OPENAI_API_VERSION
            )

            # Initialize search service
            await self.search_service.initialize()

            logger.info("RAG service initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize RAG service: {e}")
            raise

    def _count_tokens(self, text: str) -> int:
        """Count tokens in text"""
        return len(self.encoder.encode(text))

    def _preprocess_query(self, query: str) -> str:
        """Preprocess user query"""
        # Basic preprocessing: strip, lowercase, etc.
        query = query.strip()

        # Intent classification could go here
        # Entity extraction could go here

        return query

    async def _retrieve_context(self, query: str) -> List[Dict[str, Any]]:
        """Retrieve relevant context from knowledge base"""
        try:
            # Generate query embedding
            query_embedding = await self.embeddings.aembed_query(query)

            # Hybrid search: vector + keyword
            results = await self.search_service.hybrid_search(
                query=query,
                query_vector=query_embedding,
                top_k=settings.TOP_K_RESULTS
            )

            # Filter by similarity threshold
            filtered_results = [
                r for r in results
                if r.get("similarity_score", 0) >= settings.SIMILARITY_THRESHOLD
            ]

            logger.info(f"Retrieved {len(filtered_results)} relevant documents")
            return filtered_results

        except Exception as e:
            logger.error(f"Error retrieving context: {e}")
            return []

    def _format_context(self, documents: List[Dict[str, Any]]) -> str:
        """Format retrieved documents into context string"""
        if not documents:
            return "No relevant context found in the knowledge base."

        context_parts = []
        token_count = 0

        for i, doc in enumerate(documents, 1):
            doc_text = f"""
Source {i}:
Title: {doc.get('title', 'Unknown')}
Content: {doc.get('content', '')}
Source Type: {doc.get('source_type', 'Unknown')}
URL: {doc.get('url', '')}
---
"""
            doc_tokens = self._count_tokens(doc_text)

            if token_count + doc_tokens > settings.MAX_CONTEXT_TOKENS:
                break

            context_parts.append(doc_text)
            token_count += doc_tokens

        return "\n".join(context_parts)

    def _extract_sources(self, documents: List[Dict[str, Any]]) -> List[Source]:
        """Extract source citations from documents"""
        sources = []
        for doc in documents[:3]:  # Top 3 sources
            try:
                source = Source(
                    title=doc.get("title", "Unknown"),
                    url=doc.get("url", ""),
                    snippet=doc.get("content", "")[:200] + "...",
                    source_type=doc.get("source_type", "unknown"),
                    relevance_score=doc.get("similarity_score", 0.0)
                )
                sources.append(source)
            except Exception as e:
                logger.warning(f"Failed to extract source: {e}")
                continue

        return sources

    def _calculate_confidence(
        self,
        num_results: int,
        avg_similarity: float,
        response_length: int
    ) -> float:
        """Calculate confidence score for the response"""
        # Simple heuristic - can be improved with ML model
        confidence = 0.0

        # Factor 1: Number of relevant results (40%)
        if num_results >= 3:
            confidence += 0.4
        elif num_results >= 2:
            confidence += 0.25
        elif num_results >= 1:
            confidence += 0.1

        # Factor 2: Average similarity score (40%)
        confidence += avg_similarity * 0.4

        # Factor 3: Response completeness (20%)
        if response_length > 100:
            confidence += 0.2
        elif response_length > 50:
            confidence += 0.1

        return min(confidence, 1.0)

    def _suggest_actions(self, confidence: float, query: str) -> List[str]:
        """Suggest next actions based on confidence"""
        actions = []

        if confidence < 0.6:
            actions.append("escalate")
            actions.append("create_ticket")
        elif confidence < 0.8:
            actions.append("view_sources")
            actions.append("refine_question")
        else:
            actions.append("mark_resolved")

        # Check for specific intents
        if any(word in query.lower() for word in ["urgent", "critical", "emergency"]):
            actions.insert(0, "call_tech_assist")

        return actions

    async def generate_response(
        self,
        query: str,
        conversation_history: List[Dict[str, str]] = None
    ) -> ChatResponse:
        """Generate response using RAG pipeline"""
        try:
            # Step 1: Preprocess query
            processed_query = self._preprocess_query(query)
            logger.info(f"Processing query: {processed_query}")

            # Step 2: Retrieve relevant context
            documents = await self._retrieve_context(processed_query)

            if not documents:
                logger.warning("No relevant context found")
                return ChatResponse(
                    response="I don't have enough information to answer that question. I recommend escalating to Tech Assist for personalized help.",
                    sources=[],
                    confidence=0.0,
                    suggested_actions=["escalate", "create_ticket", "call_tech_assist"],
                    session_id="",
                    timestamp=None
                )

            # Step 3: Format context
            context = self._format_context(documents)

            # Step 4: Generate response with LLM
            system_msg = SystemMessage(content=self.system_prompt.format(context=context))
            human_msg = HumanMessage(content=f"Question: {processed_query}")

            messages = [system_msg]
            if conversation_history:
                for msg in conversation_history[-3:]:  # Last 3 messages for context
                    role = msg.get("role", "user")
                    content = msg.get("content", "")
                    if role == "user":
                        messages.append(HumanMessage(content=content))
                    elif role == "assistant":
                        messages.append(SystemMessage(content=f"Previous response: {content}"))

            messages.append(human_msg)

            response = await self.llm.agenerate([messages])
            answer = response.generations[0][0].text

            # Step 5: Extract sources
            sources = self._extract_sources(documents)

            # Step 6: Calculate confidence
            avg_similarity = sum(d.get("similarity_score", 0) for d in documents) / len(documents)
            confidence = self._calculate_confidence(
                num_results=len(documents),
                avg_similarity=avg_similarity,
                response_length=len(answer)
            )

            # Step 7: Suggest actions
            suggested_actions = self._suggest_actions(confidence, query)

            logger.info(f"Generated response with confidence: {confidence:.2f}")

            return ChatResponse(
                response=answer,
                sources=sources,
                confidence=confidence,
                suggested_actions=suggested_actions,
                session_id="",  # Will be set by caller
                timestamp=None  # Will be set by Pydantic default
            )

        except Exception as e:
            logger.error(f"Error generating response: {e}", exc_info=True)
            raise


# Singleton instance
rag_service = RAGService()
