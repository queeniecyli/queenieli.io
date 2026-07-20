# Tech Assist AI - System Architecture

## Overview

Tech Assist AI (TAAI) is a retrieval-augmented generation (RAG) chatbot that provides instant tech support by querying internal knowledge bases (Confluence, SharePoint) and generating contextual responses using Azure OpenAI.

---

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERFACES                          │
├──────────────┬──────────────────┬──────────────────┬────────────┤
│   Web App    │  Microsoft Teams │  SharePoint Web  │   Mobile   │
│   (React)    │      Bot         │      Part        │    PWA     │
└──────┬───────┴────────┬─────────┴────────┬─────────┴─────┬──────┘
       │                │                  │               │
       └────────────────┴──────────────────┴───────────────┘
                               │
                    ┌──────────▼──────────┐
                    │   API Gateway       │
                    │   (Azure APIM)      │
                    └──────────┬──────────┘
                               │
       ┌───────────────────────┼───────────────────────┐
       │                       │                       │
┌──────▼──────┐      ┌─────────▼────────┐   ┌─────────▼────────┐
│  FastAPI    │      │   WebSocket      │   │  Background      │
│  REST API   │      │   Server         │   │  Workers         │
└──────┬──────┘      └─────────┬────────┘   └─────────┬────────┘
       │                       │                       │
       └───────────────────────┼───────────────────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
    ┌─────────▼──────┐  ┌──────▼──────┐  ┌────▼─────────┐
    │  RAG Engine    │  │  Azure      │  │  Queue       │
    │  (LangChain)   │  │  OpenAI     │  │  Monitor     │
    └─────────┬──────┘  └──────┬──────┘  └────┬─────────┘
              │                │               │
    ┌─────────▼──────────┬─────▼──────┐  ┌────▼─────────┐
    │  Azure Cognitive   │  Vector    │  │  ServiceNow  │
    │  Search            │  Store     │  │  API         │
    └────────────────────┴────────────┘  └──────────────┘
```

---

## Component Details

### 1. Frontend Layer

#### Web Application (React + TypeScript)
```
src/
├── components/
│   ├── Chat/
│   │   ├── ChatWindow.tsx
│   │   ├── MessageBubble.tsx
│   │   ├── InputBox.tsx
│   │   └── TypingIndicator.tsx
│   ├── QueueStatus/
│   │   ├── LiveQueue.tsx
│   │   └── WaitTimeEstimate.tsx
│   └── Escalation/
│       └── CreateTicketModal.tsx
├── services/
│   ├── chatService.ts
│   ├── websocketService.ts
│   └── analyticsService.ts
└── hooks/
    ├── useChat.ts
    └── useQueueStatus.ts
```

**Key Features:**
- Real-time messaging with WebSocket
- Markdown rendering for formatted responses
- Source citation display
- Feedback mechanism (thumbs up/down)
- Escalation to human agent
- Conversation history

---

### 2. Backend Layer

#### FastAPI Application
```python
backend/app/
├── api/
│   ├── chat.py           # Chat endpoints
│   ├── queue.py          # Queue status endpoints
│   ├── feedback.py       # User feedback
│   └── analytics.py      # Usage metrics
├── core/
│   ├── config.py         # Configuration
│   ├── security.py       # Authentication
│   └── logging.py        # Structured logging
├── models/
│   ├── chat.py           # Pydantic models
│   └── user.py
├── services/
│   ├── rag_service.py    # RAG orchestration
│   ├── embedding_service.py
│   ├── search_service.py
│   └── llm_service.py
└── main.py
```

**Key APIs:**

```python
# Chat endpoint
POST /api/v1/chat/message
{
  "user_id": "string",
  "session_id": "string",
  "message": "How do I reset my VPN?",
  "context": {}
}

# Response
{
  "response": "To reset your VPN...",
  "sources": [
    {
      "title": "VPN Setup Guide",
      "url": "https://confluence.../vpn-guide",
      "snippet": "..."
    }
  ],
  "confidence": 0.92,
  "suggested_actions": ["escalate", "create_ticket"]
}

# Queue status
GET /api/v1/queue/status?location=sydney-l5
{
  "location": "Sydney - Level 5",
  "wait_time_minutes": 12,
  "queue_length": 3,
  "available_agents": 2,
  "status": "moderate"
}
```

---

### 3. RAG Pipeline

#### Data Ingestion Pipeline

```python
# Stage 1: Document Collection
┌─────────────────────┐
│  Confluence API     │ → Pull all IT docs
│  SharePoint API     │ → Extract knowledge articles
└─────────────────────┘
           ↓
# Stage 2: Processing
┌─────────────────────┐
│  Text Extraction    │ → Clean HTML, extract text
│  Chunking           │ → Split into 512-token chunks
│  Metadata Tagging   │ → Add source, date, category
└─────────────────────┘
           ↓
# Stage 3: Embedding
┌─────────────────────┐
│  Azure OpenAI       │ → text-embedding-ada-002
│  Embeddings         │ → Generate 1536-dim vectors
└─────────────────────┘
           ↓
# Stage 4: Indexing
┌─────────────────────┐
│  Azure Cognitive    │ → Store vectors + metadata
│  Search             │ → Enable hybrid search
└─────────────────────┘
```

#### Query Pipeline

```python
# User query: "How do I reset my VPN?"

1. Query Preprocessing
   - Spell check
   - Intent classification (vpn_reset)
   - Extract entities (VPN, reset)

2. Embedding Generation
   - Convert query to vector
   - Azure OpenAI: text-embedding-ada-002

3. Hybrid Search
   - Vector similarity search (top 10)
   - Keyword BM25 search (top 10)
   - Merge and re-rank (RRF)

4. Context Retrieval
   - Fetch top 5 most relevant chunks
   - Include metadata (source, date)
   - Format as context window

5. LLM Generation
   - System prompt: "You are Tech Assist AI..."
   - User query + retrieved context
   - GPT-4 generates response
   - Citations extracted

6. Response Post-Processing
   - Format markdown
   - Add source links
   - Calculate confidence score
   - Suggest next actions
```

---

### 4. Data Sources

#### Confluence Integration

```python
from atlassian import Confluence

confluence = Confluence(
    url='https://macquarie.atlassian.net',
    token=os.getenv('CONFLUENCE_TOKEN')
)

# Pull all pages from IT space
spaces = ['IT', 'TECHSUPPORT', 'INFOSEC']
pages = confluence.get_all_pages_from_space(
    space=spaces,
    expand='body.storage,version,metadata'
)

# Extract and process
for page in pages:
    content = page['body']['storage']['value']
    metadata = {
        'source': 'confluence',
        'url': page['_links']['webui'],
        'title': page['title'],
        'last_updated': page['version']['when'],
        'space': page['space']['key']
    }
    # Process and index...
```

#### SharePoint Integration

```python
from office365.sharepoint.client_context import ClientContext

ctx = ClientContext(site_url).with_credentials(
    UserCredential(username, password)
)

# Access Tech Assist knowledge base
list_obj = ctx.web.lists.get_by_title("Knowledge Base")
items = list_obj.items.get().execute_query()

for item in items:
    content = item.properties['Body']
    metadata = {
        'source': 'sharepoint',
        'url': item.properties['FileRef'],
        'title': item.properties['Title'],
        'category': item.properties['Category'],
        'last_modified': item.properties['Modified']
    }
    # Process and index...
```

---

### 5. Azure OpenAI Integration

#### Configuration

```python
from langchain.chat_models import AzureChatOpenAI
from langchain.embeddings import AzureOpenAIEmbeddings

# LLM for generation
llm = AzureChatOpenAI(
    deployment_name="gpt-4",
    model_name="gpt-4",
    temperature=0.2,
    max_tokens=500,
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-15-preview"
)

# Embeddings for RAG
embeddings = AzureOpenAIEmbeddings(
    deployment="text-embedding-ada-002",
    model="text-embedding-ada-002",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY")
)
```

#### Prompt Engineering

```python
SYSTEM_PROMPT = """You are Tech Assist AI (TAAI), Macquarie Group's intelligent tech support assistant.

Your role:
- Provide accurate, helpful answers to IT and tech questions
- Use ONLY the information from the provided context
- If you don't know, say so and suggest escalating to Tech Assist
- Be concise but complete
- Include source citations

Response format:
1. Direct answer to the question
2. Step-by-step instructions if applicable
3. Source citations at the end
4. Suggest escalation if needed

Context:
{context}

Guidelines:
- Be friendly and professional
- Use Macquarie-specific terminology
- Verify information before responding
- Prioritize security and compliance
"""

USER_PROMPT = """Question: {question}

Please provide a helpful answer based on the context above."""
```

---

### 6. Queue Monitoring System

#### ServiceNow Integration

```python
from pysnow import Client

# Connect to ServiceNow
client = Client(
    instance='macquarie',
    user=os.getenv('SNOW_USER'),
    password=os.getenv('SNOW_PASSWORD')
)

# Get current queue status
def get_queue_status(location: str) -> dict:
    incident = client.resource(api_path='/table/incident')

    # Query open Tech Assist tickets
    response = incident.get(
        query={
            'assignment_group': 'Tech Assist',
            'location': location,
            'state': 'Open'
        }
    )

    queue_length = len(response.all())
    avg_resolution_time = calculate_avg_time(response)

    return {
        'location': location,
        'queue_length': queue_length,
        'estimated_wait': avg_resolution_time * queue_length,
        'status': get_status_level(queue_length)
    }
```

---

### 7. Security & Authentication

#### Azure AD Integration

```python
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials"
    )

    try:
        payload = jwt.decode(
            token,
            os.getenv("AZURE_AD_SECRET"),
            algorithms=["RS256"],
            audience=os.getenv("AZURE_AD_CLIENT_ID")
        )
        username: str = payload.get("preferred_username")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    return username

# Protected endpoint
@app.post("/api/v1/chat/message")
async def chat(
    message: ChatMessage,
    current_user: str = Depends(get_current_user)
):
    # Process message...
```

---

### 8. Monitoring & Analytics

#### Telemetry

```python
from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry import trace

configure_azure_monitor(
    connection_string=os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING")
)

tracer = trace.get_tracer(__name__)

@app.post("/api/v1/chat/message")
async def chat(message: ChatMessage):
    with tracer.start_as_current_span("chat_request") as span:
        span.set_attribute("user_id", message.user_id)
        span.set_attribute("message_length", len(message.message))

        # Process and track
        response = await rag_service.generate_response(message)

        span.set_attribute("response_confidence", response.confidence)
        span.set_attribute("sources_count", len(response.sources))

        return response
```

#### Metrics Dashboard

```
Key Metrics:
├── Usage
│   ├── Total conversations
│   ├── Active users (DAU/MAU)
│   ├── Messages per session
│   └── Peak usage times
├── Performance
│   ├── Avg response time
│   ├── P95/P99 latency
│   ├── Error rate
│   └── Uptime
├── Quality
│   ├── Resolution rate
│   ├── Escalation rate
│   ├── User satisfaction (CSAT)
│   └── Feedback sentiment
└── Business Impact
    ├── Ticket deflection rate
    ├── Time saved (hrs)
    ├── Cost savings ($)
    └── ROI
```

---

## Deployment Architecture

```
Production Environment (Azure)

┌─────────────────────────────────────────────────┐
│  Azure Front Door (CDN + WAF)                   │
└────────────┬────────────────────────────────────┘
             │
┌────────────▼────────────────────────────────────┐
│  Azure API Management                           │
│  - Rate limiting                                │
│  - API keys                                     │
│  - Request throttling                           │
└────────────┬────────────────────────────────────┘
             │
     ┌───────┴────────┐
     │                │
┌────▼─────┐    ┌────▼──────┐
│ App      │    │ App       │
│ Service  │    │ Service   │
│ (API)    │    │ (Workers) │
│ - Auto   │    │ - Batch   │
│   scale  │    │   jobs    │
└────┬─────┘    └────┬──────┘
     │               │
     └───────┬───────┘
             │
  ┌──────────┼──────────┐
  │          │          │
┌─▼──────┐ ┌─▼──────┐ ┌▼───────┐
│ Azure  │ │ Azure  │ │ Cosmos │
│ OpenAI │ │ Search │ │ DB     │
└────────┘ └────────┘ └────────┘
```

---

## Scalability Considerations

1. **Horizontal Scaling**
   - API servers: Auto-scale based on CPU/memory
   - Workers: Queue-based scaling

2. **Caching Strategy**
   - Redis for frequent queries
   - CDN for static assets
   - Response caching (5 min TTL)

3. **Rate Limiting**
   - 100 requests/min per user
   - 10,000 requests/min globally

4. **Database Optimization**
   - Read replicas for analytics
   - Indexed queries
   - Partitioning by date

---

## Disaster Recovery

- **RPO**: 1 hour (data replication)
- **RTO**: 15 minutes (automated failover)
- **Backup Strategy**: Daily snapshots + continuous replication
- **Failover**: Multi-region deployment (Primary: Australia East, Secondary: Australia Southeast)

---

## Cost Estimation

**Monthly Operating Costs (at scale):**

| Service | Usage | Cost |
|---------|-------|------|
| Azure OpenAI (GPT-4) | 1M tokens/day | ~$1,200 |
| Azure OpenAI (Embeddings) | 10M tokens/day | ~$200 |
| Azure Cognitive Search | Standard tier | $250 |
| App Service | Premium V3 | $400 |
| Cosmos DB | 1000 RU/s | $300 |
| Storage | 100GB | $20 |
| **Total** | | **~$2,370/month** |

**Break-Even Analysis:**
- Tech Assist hourly cost: ~$50/hour (blended rate)
- If TAAI deflects 10 tickets/day @ 15 min each
- Time saved: 2.5 hours/day = $125/day
- Monthly savings: $3,750
- **Net savings: $1,380/month** (58% ROI)

---

## Next Steps

1. Provision Azure resources
2. Set up CI/CD pipeline
3. Ingest initial knowledge base
4. Build MVP interface
5. Internal pilot with 50 users
6. Iterate based on feedback
7. Production launch

