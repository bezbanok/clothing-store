from fastapi import APIRouter, HTTPException, status
from schemas import OrderCreate

router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Оформить заказ",
    description="Создает заказ на основе товаров из корзины и контактных данных пользователя."
)
def create_order(order: OrderCreate):
    if not order.items:
        raise HTTPException(status_code=400, detail="В заказе должен быть хотя бы один товар")

    return {
        "message": "Заказ успешно создан",
        "user_id": order.user_id,
        "items_count": len(order.items),
        "delivery_address": order.delivery_address
    }
