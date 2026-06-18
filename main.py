from fastapi import FastAPI

app = FastAPI()

from usuario_router import router_usuario
from address_router import router_address
from order_router import router_order
from products_router import router_products

app.include_router(router_usuario)
app.include_router(router_address)
app.include_router(router_order)
app.include_router(router_products)


