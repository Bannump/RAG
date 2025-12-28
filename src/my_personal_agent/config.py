"""
Configuration management for My Personal Agent
"""
import os
from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # API Keys
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    anthropic_api_key: Optional[str] = Field(None, env="ANTHROPIC_API_KEY")
    
    # Vector Database
    vector_db_path: str = Field("./data/vector_db", env="VECTOR_DB_PATH")
    use_pinecone: bool = Field(False, env="USE_PINECONE")
    pinecone_api_key: Optional[str] = Field(None, env="PINECONE_API_KEY")
    pinecone_environment: Optional[str] = Field(None, env="PINECONE_ENVIRONMENT")
    pinecone_index_name: Optional[str] = Field(None, env="PINECONE_INDEX_NAME")
    
    # Application Settings
    secret_key: str = Field(..., env="SECRET_KEY")
    database_path: str = Field("./data/users.db", env="DATABASE_PATH")
    log_level: str = Field("INFO", env="LOG_LEVEL")
    
    # Model Configuration
    default_llm_provider: str = Field("openai", env="DEFAULT_LLM_PROVIDER")
    default_model: str = Field("gpt-4-turbo-preview", env="DEFAULT_MODEL")
    embedding_model: str = Field("text-embedding-3-small", env="EMBEDDING_MODEL")
    
    # Paths
    data_dir: str = Field("./data", env="DATA_DIR")
    uploads_dir: str = Field("./data/uploads", env="UPLOADS_DIR")
    output_dir: str = Field("./data/outputs", env="OUTPUT_DIR")
    
    # Feature Flags
    enable_auth: bool = Field(True, env="ENABLE_AUTH")
    enable_image_analysis: bool = Field(True, env="ENABLE_IMAGE_ANALYSIS")
    enable_resume_builder: bool = Field(True, env="ENABLE_RESUME_BUILDER")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Ensure directories exist
        Path(self.data_dir).mkdir(parents=True, exist_ok=True)
        Path(self.uploads_dir).mkdir(parents=True, exist_ok=True)
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)
        Path(self.vector_db_path).mkdir(parents=True, exist_ok=True)


# Global settings instance
# Note: This will raise an error if required environment variables are not set
# This is intentional to ensure proper configuration
settings = Settings()

