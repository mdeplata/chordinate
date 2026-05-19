from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    redis_url: str = "redis://localhost:6379/0"
    max_file_mb: int = 50
    allowed_origins: str = "http://localhost:5173"
    class Config:
        env_file = ".env"

settings = Settings()