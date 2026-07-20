"""Application configuration"""

from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # API Configuration
    API_VERSION: str = "v1"
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"

    # Azure OpenAI
    AZURE_OPENAI_ENDPOINT: str
    AZURE_OPENAI_API_KEY: str
    AZURE_OPENAI_DEPLOYMENT_NAME: str = "gpt-4"
    AZURE_OPENAI_EMBEDDING_DEPLOYMENT: str = "text-embedding-ada-002"
    AZURE_OPENAI_API_VERSION: str = "2024-02-15-preview"

    # Azure Cognitive Search
    AZURE_SEARCH_ENDPOINT: str
    AZURE_SEARCH_API_KEY: str
    AZURE_SEARCH_INDEX_NAME: str = "tech-assist-kb"

    # Database
    DATABASE_URL: str

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # Confluence
    CONFLUENCE_URL: str
    CONFLUENCE_TOKEN: str
    CONFLUENCE_SPACES: str = "IT,TECHSUPPORT,INFOSEC"

    # SharePoint
    SHAREPOINT_SITE_URL: str
    SHAREPOINT_CLIENT_ID: str
    SHAREPOINT_CLIENT_SECRET: str

    # ServiceNow
    SERVICENOW_INSTANCE: str
    SERVICENOW_USER: str
    SERVICENOW_PASSWORD: str

    # Azure AD
    AZURE_AD_TENANT_ID: str
    AZURE_AD_CLIENT_ID: str
    AZURE_AD_CLIENT_SECRET: str

    # Application Insights
    APPLICATIONINSIGHTS_CONNECTION_STRING: str

    # Security
    SECRET_KEY: str
    ALLOWED_ORIGINS: List[str] = ["*"]

    # Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = 100
    RATE_LIMIT_GLOBAL: int = 10000

    # RAG Configuration
    MAX_CONTEXT_TOKENS: int = 3000
    TOP_K_RESULTS: int = 5
    SIMILARITY_THRESHOLD: float = 0.7
    TEMPERATURE: float = 0.2
    MAX_TOKENS: int = 500

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
