from fastapi import APIRouter, HTTPException, status
from schemas import CartItemCreate

router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Добавить товар в корзину",
    description="Добавляет выбранный товар в корзину пользователя."
)
def add_to_cart(item: CartItemCreate):
    if item.quantity <= 0:
        raise HTTPException(status_code=400, detail="Количество товара должно быть больше нуля")

    return {
        "message": "Товар добавлен в корзину",
        "product_id": item.product_id,
        "quantity": item.quantity
    }


@router.get(
    "/",
    summary="Получить содержимое корзины",
    description="Возвращает список товаров, добавленных пользователем в корзину."
)
def get_cart():
    return {
        "items": [
            {"product_id": 1, "name": "Худи oversize", "quantity": 1, "price": 4590}
        ],
        "total": 4590
    }


@router.delete(
    "/{product_id}",
    summary="Удалить товар из корзины",
    description="Удаляет товар из корзины по идентификатору товара."
)
def remove_from_cart(product_id: int):
    return {
        "message": "Товар удален из корзины",
        "product_id": product_id
    }
