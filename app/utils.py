from datetime import datetime, timedelta

from config import settings
from external_apis.youtube_api import instance as youtube
from fastapi_utils.tasks import repeat_every
from database.es import get_database


@repeat_every(seconds=settings.PERIOD)
async def add_new_videos(q: str = "cricket", max_results: int = 10):
    """
        Fetch query results and update db
    """
    t = datetime.utcnow() - timedelta(seconds=settings.PERIOD)
    published_after = t.isoformat("T") + "Z"
    response = await youtube.search(q=q, part=["snippet"], type_="video", max_results=max_results, published_after=published_after)
    es = await get_database()
    for item in response["items"]:
        snippet = item["snippet"]
        video = {
            "id": item["id"]["videoId"],
            "title": snippet["title"],
            "description": snippet["description"],
            "published_at": snippet["publishedAt"],
            "url": "https://www.youtube.com/watch?v=" + item["id"]["videoId"],
            "query": q
        }
        await es.index(index=settings.ES_INDEX, id=item["id"]["videoId"], body=video)

    print("New Videos Added to DB")
