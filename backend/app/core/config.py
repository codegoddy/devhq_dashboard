from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://user:password@localhost/devhq_dashboard"
    secret_key: str = "your-secret-key-change-in-production"
    brevo_api_key: str = "your-brevo-api-key"
    main_backend_url: str = "http://localhost:8001"  # main DevHQ backend URL

    class Config:
        env_file = ".env"

settings = Settings()