from fastapi import APIRouter

router_address = APIRouter(prefix='/address', tags=['Address'])

@router_address.post('/')
async def criar_address():
    return