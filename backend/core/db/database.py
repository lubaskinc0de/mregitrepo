from .models import Base

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from ..settings import Settings
from fastapi import Depends


async def get_async_sessionmaker() -> sessionmaker:
    return 'a'

    # """Get sessionmaker instance"""
    #
    # print("------- SESSIONMAKER ---------------")
    #
    # engine = create_async_engine(
    #     f"postgresql+asyncpg://{settings.db.user}:{settings.db.password}@{settings.db.host}/{settings.db.db_name}",
    #     future=True,
    # )
    #
    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    #
    # async_sessionmaker = sessionmaker(
    #     engine, expire_on_commit=False, class_=AsyncSession
    # )
    #
    # return async_sessionmaker
