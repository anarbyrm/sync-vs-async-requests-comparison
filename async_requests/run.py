import asyncio
from time import time

from product_data import get_data
from async_client import prepare_client, Client


def create_task(client: Client, product: dict):
    request_coroutine = client.make_request(
        subject="products",
        method="POST",
        data=product
    )
    task = asyncio.create_task(request_coroutine)
    return task


async def publish_products(products: list, client: Client):
    tasks = [create_task(client, product) for product in products]
    responses = await asyncio.gather(*tasks)
    return responses


async def main():
    # get client to make requests
    client = prepare_client()

    # get fake product data 
    product_data = get_data()

    started = time()
    responses = await publish_products(product_data, client=client)
    finished = time()

    print(f"\n{len(responses)} products out of {len(product_data)} are migrated")
    print(f"finished in {finished - started} seconds")

    # 8 products out of 8 are migrated
    # finished in 1.1848883628845215 seconds

if __name__ == "__main__":
    asyncio.run(main())
