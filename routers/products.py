from fastapi import APIRouter, Query
from typing import List, Optional
from schemas import Product
from services.products import ProductService

router = APIRouter()


@router.get(
    "/",
    response_model=List[Product],
    summary="Получить каталог товаров",
    description="Возвращает список товаров с возможностью фильтрации по категории, размеру и цвету."
)
def get_products(
    category: Optional[str] = Query(default=None, description="Категория одежды"),
    size: Optional[str] = Query(default=None, description="Размер одежды"),
    color: Optional[str] = Query(default=None, description="Цвет товара")
):
    return ProductService.get_products(category=category, size=size, color=color)
