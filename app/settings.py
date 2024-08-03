from pydantic import BaseModel

class Settings(BaseModel):
    # Configuración de la base de datos
    db_host: str = "localhost"
    db_user: str = "root"
    db_password: str = "admin"
    db_name: str = "crud"
    db_port: str = "3306"

    # Configuración de la API
    api_prefix: str = "/api/v1"
    project_name: str = "Mi API"
    project_description: str = "Esta es una API de ejemplo con FastAPI"
    project_version: str = "1.0.0"
    openapi_url: str = "/api/v1/openapi.json"
    docs_url: str = "/documentacion"
    redoc_url: str = "/redoc"

    # Configuración general
    debug: bool = False

    @property
    def database_url(self):
        return f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

settings = Settings()