from fastapi import APIRouter

router_products = APIRouter(prefix='/products' , tags=['products'] )

@router_products.get('/')
async def pegar_produto():
    return