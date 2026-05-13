from decimal import Decimal
from typing import List, Optional
from schemas import Product


class ProductService:
    """Сервисный слой для работы с каталогом товаров."""

    @staticmethod
    def get_products(
        category: Optional[str] = None,
        size: Optional[str] = None,
        color: Optional[str] = None
    ) -> List[Product]:
        products = [
            Product(id=1, name="Худи oversize", category="hoodie", size="M", color="black", price=Decimal("4590"), stock=12),
            Product(id=2, name="Базовая футболка", category="t-shirt", size="S", color="white", price=Decimal("1990"), stock=25),
            Product(id=3, name="Джинсы straight", category="jeans", size="L", color="blue", price=Decimal("5490"), stock=8),
        ]

        if category:
            products = [item for item in products if item.category == category]
        if size:
            products = [item for item in products if item.size == size]
        if color:
            products = [item for item in products if item.color == color]
        return products
