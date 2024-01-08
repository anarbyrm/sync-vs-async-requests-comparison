def get_data():
    """
    returns fake product data for Shopify REST API (product creation endpoint)
    """
    result = [
        {"product":{"title":"Product 1","body_html":"<strong>BODY 1</strong>","status":"active"}},
        {"product":{"title":"Product 2","body_html":"<strong>BODY 2</strong>","status":"active"}},
        {"product":{"title":"Product 3","body_html":"<strong>BODY 3</strong>","status":"active"}},
        {"product":{"title":"Product 4","body_html":"<strong>BODY 4</strong>","status":"active"}},
        {"product":{"title":"Product 5","body_html":"<strong>BODY 5</strong>","status":"active"}},
        {"product":{"title":"Product 6","body_html":"<strong>BODY 6</strong>","status":"active"}},
        {"product":{"title":"Product 7","body_html":"<strong>BODY 7</strong>","status":"active"}},
        {"product":{"title":"Product 8","body_html":"<strong>BODY 8</strong>","status":"active"}},
    ]

    return result
