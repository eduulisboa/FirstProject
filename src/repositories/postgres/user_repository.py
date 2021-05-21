from sqlalchemy.orm import Session

from src.schemas.user_schema import UserSchema
from src.entities.user_entity import UserEntity


class UserRepository:

    def __init__(self, database_session: Session):
        self.__database = database_session

    def is_connected(self) -> bool:
        return True if self.__database else False

    def get_all(self):
        users = self.__database.query(UserEntity).all()
        return users

    def get_one(self, user_id):
        user = self.__database.query(UserEntity).get(user_id)

        if not user:
            return None

        return user

    def create(self, user: UserSchema):
        new_user = UserEntity(
            anything=user.anything,
        )

        self.__database.add(new_user)
        self.__database.commit()
        self.__database.refresh(new_user)

        return new_user

    def update(self, user_id, user: UserSchema):
        db_user = self.__database.query(UserEntity).get(user_id)

        if not db_user:
            return None

        updated_user = user.__dict__

        for key, value in updated_user.items():
            setattr(db_user, key, value)

        self.__database.commit()
        self.__database.refresh(db_user)

        return db_user

    def delete(self, user_id):
        user = self.__database.query(UserEntity).get(user_id)

        if not user:
            return None

        self.__database.delete(user)
        self.__database.commit()

        return user
