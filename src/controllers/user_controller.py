from fastapi import APIRouter

user_router = APIRouter(prefix='/user')


@user_router.get('/')
def get_user():
    return {'message': 'Hello World'}
