import logging
from elasticsearch import AsyncElasticsearch


from config import settings
from database.es import db, get_database

logger = logging.getLogger("youtube_apis")


async def connect_to_es():
    db.client = AsyncElasticsearch(hosts=settings.ES_HOSTS)
    logger.debug("ES Client instantiated")


async def close_es_connection():
    await db.client.close()
    logger.debug("Close ES Client")


async def create_index():
    es = await get_database()

    if not await es.indices.exists(settings.ES_INDEX):
        mapping = {
                "settings": {
                    "index": {
                        "sort.field": "date",
                        "sort.order": "desc" 
                        }
                },
                "mappings": {
                    "properties": {
                    "date": {
                        "type": "date"
                    }
                    }
                }
            }

        await es.indices.create(index=settings.ES_INDEX, body=mapping)
        logger.debug("index created")
