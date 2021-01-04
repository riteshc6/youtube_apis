from fastapi import APIRouter

from database.es_utils import get_database
from external_apis.youtube_api import instance as youtube

router = APIRouter()

@router.get("/videos")
async def get_videos(page: int = 1, size: int = 10):
    """
        Return a paginated response of all videos in the db sorted in
        reverse chronological order of published date

        NOTE : Due to elasticsearch limitation pagination will work only till
               9999 entries, if more entries are required then we can use some
               other db for this api
    """
    last_index = size * (page - 1)
    
    body = {
        "sort": [
            {"published_at": "desc"}
        ]
    }
    es = await get_database()
    response = await es.search(from_= last_index, size=size, body=body)

    videos = []
    for video in response["hits"]["hits"]:
        videos.append(video["_source"])

    return videos


@router.get("/search")
async def search(q: str):
    """
        Return relevant videos for given query
    """
    es = await get_database()
    body = {
        "query": {
            "multi_match": {
                "query": q,
                "fields": ["title", "description"]
            }
        }
    }
    response = await es.search(index="videos", body=body)
    videos = []
    for video in response["hits"]["hits"]:
        videos.append(video["_source"])
    return videos
