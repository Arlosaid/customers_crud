from fastapi import FastAPI
from mangum import Mangum
from app.api.controller import router as items_router
from app.settings import settings

app = FastAPI(
    title=settings.project_name,
    description=settings.project_description,
    version=settings.project_version,
    openapi_url=settings.openapi_url,
    docs_url=settings.docs_url,
    redoc_url=settings.redoc_url
)

app.include_router(items_router, prefix=f"{settings.api_prefix}", tags=["Customer"])

handler = Mangum(app)