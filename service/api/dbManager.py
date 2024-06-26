from app.api.models import CastIn, CastOut, CastUpdate
from app.api.db import casts, database


async def addCast(payload: CastIn):
    query = casts.insert().values(**payload.dict())

    return await database.execute(query=query)

async def getCast(id):
    query = casts.select(casts.c.id==id)
    return await database.fetch_one(query=query)