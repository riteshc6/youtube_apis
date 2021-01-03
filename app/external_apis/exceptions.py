class ExternalAPIError(Exception):

    def __init__(self, url: str, method: str, status_code: int, response: dict, request_body: dict):
        self.status_code = status_code
        self.response = response
        self.response["url"] = str(url)
        self.response["method"] = method
        self.response["request_body"] = request_body
