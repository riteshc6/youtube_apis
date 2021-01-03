from http_client import session
from .exceptions import ExternalAPIError


async def _fetch(method: str, url: str, **kwargs):
    """
    Fetches the given url using the method and
    returns the body after json decoding.

    Parameters
    ----------
    method: str
        The HTTP method to use when requesting the resource
    url: str
        The URL for the resource

    Returns
    -------
    dict
        The response data dictionary

    Raises
    ------
    ExternalAPIError
        ExternalAPIErrror is raised if the response status_code >= 400
    """
    method = method.upper()
    async with session.request(method, url, ssl=False, **kwargs) as response:
        response_data = await response.json()
        if response.status >= 400:
            raise ExternalAPIError(
                url=response.request_info.real_url,
                method=method,
                status_code=response.status,
                response=response_data,
                request_body=kwargs.get("json", {})
            )
    return response_data


async def get(url: str, **kwargs: dict):
    return await _fetch("GET", url, **kwargs)


async def post(url, **kwargs):
    return await _fetch("POST", url, **kwargs)


async def put(url: str, **kwargs: dict):
    return await _fetch("POST", url, **kwargs)
