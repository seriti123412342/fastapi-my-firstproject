from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from models import Base
from fastapi import Depends

from config import settings
from typing import Annotated
async_engine = create_async_engine(settings.DATABASE_URL_asyncpg, echo=True, pool_size=5, max_overflow=10)

new_session = async_sessionmaker(async_engine, expire_on_commit=False)



async def get_session():
    async with new_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]




async def setup_database():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    return {'ok': True, 'message': 'Database setup completed successfully'}