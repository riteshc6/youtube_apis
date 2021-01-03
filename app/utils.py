from external_apis.youtube_api import instance as youtube
from fastapi_utils.tasks import repeat_every


@repeat_every(seconds=30)
async def update_query_results(q: str = "cricket", max_results: int = 10):
    """
        Fetch query results and update db
    """
    response = await youtube.search(q=q, part=["snippet"], type_="video", max_results=max_results)
    videos = []
    for item in response["items"]:
        snippet = item["snippet"]
        video = {
            "id": item["id"]["videoId"],
            "title": snippet["title"],
            "description": snippet["description"],
            "published_at": snippet["publishedAt"],
            "url": "https://www.youtube.com/watch?v=" + item["id"]["videoId"],
        }
        videos.append(video)

    print("db updated")
