from fastapi import APIRouter

user_router = APIRouter(prefix='/user')


@user_router.get('/user')
def get_user():
    return {'message': 'Hello World'}
