from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from routers import products, cart, orders, users

app = FastAPI(
    title="Clothing Store API",
    description="API интернет-магазина одежды: каталог, корзина, заказы и пользователи.",
    version="1.0.0"
)

app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(cart.router, prefix="/cart", tags=["Cart"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])
app.include_router(users.router, prefix="/users", tags=["Users"])


@app.get("/scalar", include_in_schema=False)
def scalar_html():
    """Возвращает страницу интерактивной документации API в интерфейсе Scalar."""
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Clothing Store API documentation"
    )
