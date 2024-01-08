from urllib.parse import urljoin
import os
import aiohttp


mapping = {
    "products": "admin/api/2024-01/products.json",
}


class Client:
    def __init__(self, url: str, key: str):
        self.store_url = url
        self.api_key = key

    async def make_request(self,
                     method: str,
                     data: dict = None,
                     params: dict = None,
                     subject: str = None) -> dict:

        async with aiohttp.ClientSession() as session:
            try:
                headers = {
                    "X-Shopify-Access-Token": self.api_key,
                    "Content-Type": "application/json",
                }
                response = await session.request(
                    url=urljoin(self.store_url, mapping[subject]),
                    json=data,
                    params=params,
                    method=method,
                    headers=headers
                )
                return await response.json()
            except Exception as exc:
                print(exc, end="\n\n")

def prepare_client():
    store_url = os.environ.get("SHOPIFY_ADMIN_URL")
    api_key = os.environ.get("SHOPIFY_API_KEY")

    client = Client(url=store_url, key=api_key)
    return client
