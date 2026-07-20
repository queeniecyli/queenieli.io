"""
Tech Assist AI - Main Application
FastAPI backend for RAG-powered tech support chatbot
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from contextlib import asynccontextmanager

from app.core.config import settings
from app.core.logging import setup_logging, logger
from app.api import chat, queue, feedback, analytics
from app.core.security import get_current_user

# Initialize logging
setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    logger.info("Starting Tech Assist AI application...")
    # Startup: Initialize services
    try:
        # Initialize Azure OpenAI connection
        from app.services.llm_service import LLMService
        llm_service = LLMService()
        await llm_service.initialize()

        # Initialize vector store
        from app.services.search_service import SearchService
        search_service = SearchService()
        await search_service.initialize()

        logger.info("All services initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize services: {e}")
        raise

    yield

    # Shutdown: Cleanup
    logger.info("Shutting down Tech Assist AI application...")


# Create FastAPI app
app = FastAPI(
    title="Tech Assist AI API",
    description="RAG-powered tech support chatbot for Macquarie Group",
    version=settings.API_VERSION,
    docs_url=f"/api/{settings.API_VERSION}/docs",
    redoc_url=f"/api/{settings.API_VERSION}/redoc",
    lifespan=lifespan
)


# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Trusted Host Middleware
if not settings.DEBUG:
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=["*.macquarie.com", "localhost"]
    )


# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "version": settings.API_VERSION,
        "service": "Tech Assist AI"
    }


# Root endpoint
@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Tech Assist AI API",
        "version": settings.API_VERSION,
        "docs": f"/api/{settings.API_VERSION}/docs"
    }


# Include routers
app.include_router(
    chat.router,
    prefix=f"/api/{settings.API_VERSION}/chat",
    tags=["chat"]
)

app.include_router(
    queue.router,
    prefix=f"/api/{settings.API_VERSION}/queue",
    tags=["queue"]
)

app.include_router(
    feedback.router,
    prefix=f"/api/{settings.API_VERSION}/feedback",
    tags=["feedback"]
)

app.include_router(
    analytics.router,
    prefix=f"/api/{settings.API_VERSION}/analytics",
    tags=["analytics"]
)


# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "message": str(exc) if settings.DEBUG else "An error occurred"
        }
    )


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG,
        log_level=settings.LOG_LEVEL.lower()
    )
