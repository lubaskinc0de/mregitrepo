from fastapi import FastAPI

from v1 import include_routers

from sqlalchemy.orm import Session

from core.db import get_async_sessionmaker

app = FastAPI()

# app.dependency_overrides[Settings] = load_settings
app.dependency_overrides[Session] = get_async_sessionmaker

include_routers(app)
