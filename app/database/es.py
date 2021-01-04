from elasticsearch import AsyncElasticsearch


class DataBase:
    client: AsyncElasticsearch = None

db = DataBase()

async def get_database() -> AsyncElasticsearch:
    return db.client
