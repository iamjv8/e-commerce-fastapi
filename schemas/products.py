from models.product import Product


def individual_serial(product: Product) -> dict:
    if product:
        return {
            "id": str(product["_id"]),
            "title": product["title"],
            "category": product["category"],
            "description": product["description"],
            "price": product["price"],
            "image": product["image"],
        }
    

def list_serial(products) -> list:
    return [individual_serial(product) for product in products]