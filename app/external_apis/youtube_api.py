import aiohttp

from config import settings

from . import http


class Youtube:

    BASE_URL = settings.BASE_URL
    KEY = settings.APIKEY

    def __init__(self, base_url: str = None, key: str = None):
        if base_url:
            self.BASE_URL = base_url
        if key:
            self.KEY = key

    def _get_url(self, path):
        return f"{self.BASE_URL}{path}"

    async def search(self, q: str, part: list, type_: str, max_results: int, published_after: str):
        try:
            response = await http.get(
                self._get_url("/youtube/v3/search"),
                params={
                    "q": q,
                    "part": ",".join(part),
                    "type": type_,
                    "maxResults": max_results,
                    "key": self.KEY,
                    "published_after": published_after
                }
            )
            return response
        except aiohttp.ClientResponseError:
            return []


instance = Youtube()
