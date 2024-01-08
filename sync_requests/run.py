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

    # 8 products out of 8 are migrated
    # finished in 9.888469934463501 seconds
