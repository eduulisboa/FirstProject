from sqlalchemy.orm import Session

from src.schemas.user_schema import UserSchema, UserCreateSchema
from src.entities.user_entity import UserEntity


class UserRepository:

    def __init__(self, database_session: Session):
        self.__database = database_session

    def is_connected(self) -> bool:
        return True if self.__database else False

    def get_all(self):
        db_user = self.__database.query(UserEntity).all()
        user = [UserSchema(**user.__dict__) for user in db_user]
        return user

    def get_one(self, user_id):
        user_entity = self.__database.query(UserEntity).get(user_id)

        if not user_entity:
            return None

        user_schema = UserSchema(**user_entity.__dict__)
        return user_schema

    def create(self, user: UserCreateSchema):
        user_entity = UserEntity(**user.__dict__)

        self.__database.add(user_entity)
        self.__database.commit()
        self.__database.refresh(user_entity)

        user_schema = UserSchema(**user_entity.__dict__)
        return user_schema

    def update(self, user_id, user: UserCreateSchema):
        user_entity = self.__database.query(UserEntity).get(user_id)

        if not user_entity:
            return None

        updated_user = user.__dict__

        for key, value in updated_user.items():
            setattr(user_entity, key, value)

        self.__database.commit()
        self.__database.refresh(user_entity)

        user_schema = UserSchema(**user_entity.__dict__)
        return user_schema

    def delete(self, user_id):
        user = self.__database.query(UserEntity).get(user_id)

        if not user:
            return None

        self.__database.delete(user)
        self.__database.commit()

        return True
