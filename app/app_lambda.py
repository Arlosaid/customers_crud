from fastapi import FastAPI, Request
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

@app.middleware("http")
async def remove_stage_from_path(request: Request, call_next):
    path = request.url.path
    if path.startswith(f"/{settings.stage}"):
        request.scope["path"] = path.replace(f"/{settings.stage}", "", 1)
    return await call_next(request)

app.include_router(items_router, prefix=f"{settings.api_prefix}", tags=["Customer"])

handler = Mangum(app)