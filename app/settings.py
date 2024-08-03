from pydantic import BaseModel
import os
from dotenv import load_dotenv

class Settings(BaseModel):
    load_dotenv()

    db_host: str = os.getenv('DB_HOST')
    db_user: str = os.getenv('DB_USERNAME')
    db_password: str = os.getenv('DB_PASSWORD')
    db_name: str = os.getenv('DB_NAME')
    db_port: int = os.getenv('DB_PORT')

    # Configuración de la API
    api_prefix: str = "/api/v1"
    project_name: str = "Customers CRUD"
    project_description: str = "CRUD for customers"
    project_version: str = "1.0.0"
    openapi_url: str = f"{api_prefix}/openapi.json"
    docs_url: str = f"{api_prefix}/docs"
    redoc_url: str = f"{api_prefix}/redoc"

    # Configuración general
    debug: bool = False

    @property
    def database_url(self):
        return f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

settings = Settings()