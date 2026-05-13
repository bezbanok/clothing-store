from decimal import Decimal
from pydantic import BaseModel, Field
from typing import List


class Product(BaseModel):
    """Модель товара в каталоге интернет-магазина."""

    id: int = Field(description="Уникальный идентификатор товара")
    name: str = Field(description="Название товара")
    category: str = Field(description="Категория товара")
    size: str = Field(description="Доступный размер")
    color: str = Field(description="Цвет товара")
    price: Decimal = Field(description="Цена товара")
    stock: int = Field(description="Количество товара на складе")


class CartItemCreate(BaseModel):
    """Данные для добавления товара в корзину."""

    product_id: int
    quantity: int = Field(gt=0, description="Количество единиц товара")


class OrderCreate(BaseModel):
    """Данные для оформления заказа."""

    user_id: int
    items: List[CartItemCreate]
    phone: str
    delivery_address: str
