from models.product import Category, Product


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


def individual_serial_category(category: Category) -> dict:
    if category:
        return {
            "id": str(category["_id"]),
            "title": category["title"],
        }
    

def list_serial_category(categories) -> list:
    return [individual_serial_category(category) for category in categories]