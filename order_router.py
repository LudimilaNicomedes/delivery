from fastapi import APIRouter

router_order = APIRouter(prefix='/order', tags=['Order'])

@router_order.get('/')
async def pegar_pedido():
    return