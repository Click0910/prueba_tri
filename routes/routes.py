from fastapi import APIRouter, Response, status
from schemas.schemas import user_entity, users_entity
from config.db import conn
from models.models import User
from passlib.hash import sha256_crypt
from starlette.status import HTTP_204_NO_CONTENT
from stocks import find_total_price


routes = APIRouter()


@routes.get('/users', response_model=list[User], tags=['Users'])
def find_all_users():
    return users_entity(conn.prueba_tri.users.find())


@routes.post('/user', response_model=User, tags=['Users'])
def create_user(user: User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    conn.prueba_tri.users.insert_one(new_user)
    return 'received'


@routes.get('/users/{dni}', response_model=User, tags=['Users'])
def find_user(dni: str):

    return user_entity(conn.prueba_tri.users.find_one({'user_dni': dni}))


@routes.put('/userupdate/{dni}', response_model=User, tags=['Users'])
def update_user(dni: str, user: User):
    conn.prueba_tri.users.find_one_and_update(
        {"user_dni": dni}, {'$set': dict(user)})
    return Response(status_code=HTTP_204_NO_CONTENT)


@routes.delete('/usersdelete/{dni}', status_code=status.HTTP_204_NO_CONTENT, tags=['Users'])
def delete_user(dni: str):
    user_entity(conn.prueba_tri.users.find_one_and_delete({'user_dni': dni}))
    return Response(status_code=HTTP_204_NO_CONTENT)


@routes.get('/users/stocks/{dni}', tags=['Stocks'])
def find_price_stocks(dni: str):
    price = find_total_price()
    conn.prueba_tri.users.find_one_and_update(
        {'user-dni': dni}, {'$set': {'price_stocks': price}})
    return price


@routes.get('/users/buystocks/{dni}', tags=['Stocks'])
def find_price_stocks(dni: str):

    return 'in progres'
