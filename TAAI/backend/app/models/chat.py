"""Chat-related Pydantic models"""

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum


class MessageRole(str, Enum):
    """Message role enum"""
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


class Source(BaseModel):
    """Source citation model"""
    title: str
    url: str
    snippet: str
    source_type: str = Field(..., description="confluence, sharepoint, etc.")
    last_updated: Optional[datetime] = None
    relevance_score: float = Field(..., ge=0.0, le=1.0)


class ChatMessage(BaseModel):
    """Incoming chat message"""
    user_id: str
    session_id: str
    message: str = Field(..., min_length=1, max_length=2000)
    context: Optional[Dict[str, Any]] = None


class ChatResponse(BaseModel):
    """Outgoing chat response"""
    response: str
    sources: List[Source]
    confidence: float = Field(..., ge=0.0, le=1.0)
    suggested_actions: List[str] = []
    session_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class ConversationHistory(BaseModel):
    """Conversation history"""
    session_id: str
    user_id: str
    messages: List[Dict[str, Any]]
    created_at: datetime
    updated_at: datetime


class EscalationRequest(BaseModel):
    """Request to escalate to human agent"""
    user_id: str
    session_id: str
    summary: str
    category: str
    priority: str = Field(..., regex="^(low|medium|high|critical)$")
    description: str
    attachments: Optional[List[str]] = None
