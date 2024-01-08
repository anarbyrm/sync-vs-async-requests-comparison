import requests
import os

from urllib.parse import urljoin

mapping = {
    "products": "admin/api/2024-01/products.json",
}


class Client:
    def __init__(self, url: str, key: str):
        self.store_url = url
        self.api_key = key

    def make_request(self,
                     method: str,
                     data: dict = None,
                     params: dict = None,
                     subject: str = None) -> dict:

        with requests.Session() as session:
            session.headers.update({
                "X-Shopify-Access-Token": self.api_key,
                "Content-Type": "application/json",
            })
            response = session.request(
                url=urljoin(self.store_url, mapping[subject]),
                json=data,
                params=params,
                method=method
            )
            if response:
                return response.json()
            else:
                response.raise_for_status()


def prepare_client():
    store_url = os.environ.get("SHOPIFY_ADMIN_URL")
    api_key = os.environ.get("SHOPIFY_API_KEY")

    client = Client(url=store_url, key=api_key)
    return client
