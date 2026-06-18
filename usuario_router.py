from fastapi import APIRouter

router_usuario = APIRouter(prefix='/usuario', tags=['Usuário'])

@router_usuario.get('/')
async def usuario():
    return

@router_usuario.post('/criar_usuario')
async def criar_conta(nome = str, email = str, senha= str):
    return