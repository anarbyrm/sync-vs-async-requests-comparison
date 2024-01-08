from time import time

from product_data import get_data
from sync_client import prepare_client, Client


def publish_products(products: list, client: Client) -> list:
    result = []

    for product in products:
        try:
            response = client.make_request(
                subject="products",
                method="POST",
                data=product
            )
            result.append(response)
            print(f"{response['product']['title']} published")

        except Exception as exc:
            print(exc)

    return result


if __name__ == "__main__":
    # get client to make requests
    client = prepare_client()

    # get fake product data 
    product_data = get_data()

    started = time()
    result = publish_products(product_data, client=client)
    finished = time()

    print(f"\n{len(result)} products out of {len(product_data)} are migrated")
    print(f"finished in {finished - started} seconds")

    # result in terminal:
    # Product 1 published
    # Product 2 published
    # Product 3 published
    # Product 4 published
    # Product 5 published
    # Product 6 published
    # Product 7 published
    # Product 8 published

    # 8 products out of 8 are migrated
    # finished in 6.66955828666687 seconds
