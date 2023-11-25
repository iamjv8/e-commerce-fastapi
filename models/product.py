from pydantic import BaseModel

class Product(BaseModel):
    title: str
    description: str
    category: str
    price: int
    image: str

