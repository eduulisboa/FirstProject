from fastapi import APIRouter

template_router = APIRouter(prefix='/template')


@template_router.get('/')
def get_template():
    return {'message': 'Hello World'}
