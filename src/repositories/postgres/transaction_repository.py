from sqlalchemy.orm import Session

from src.schemas.transaction_schema import TransactionSchema, TransactionCreateSchema
from src.entities.transaction_entity import TransactionEntity


class TransactionRepository:

    def __init__(self, database_session: Session):
        self.__database = database_session

    def is_connected(self) -> bool:
        return True if self.__database else False

    def get_all(self):
        db_transaction = self.__database.query(TransactionEntity).all()
        transaction = [TransactionSchema(**transaction.__dict__) for transaction in db_transaction]
        return transaction

    def get_all_by_user_id(self, user_id):
        db_transaction_user_id = self.__database.query(TransactionEntity).filter(TransactionEntity.user_id == user_id)
        transaction = [TransactionSchema(**transaction.__dict__) for transaction in db_transaction_user_id]
        return transaction

    def get_one(self, transaction_id):
        transaction_entity = self.__database.query(TransactionEntity).get(transaction_id)

        if not transaction_entity:
            return None

        transaction_schema = TransactionSchema(**transaction_entity.__dict__)
        return transaction_schema

    def create(self, transaction: TransactionCreateSchema):
        transaction_entity = TransactionEntity(**transaction.__dict__)

        self.__database.add(transaction_entity)
        self.__database.commit()
        self.__database.refresh(transaction_entity)

        transaction_schema = TransactionSchema(**transaction_entity.__dict__)
        return transaction_schema

    def update(self, transaction_id, transaction: TransactionCreateSchema):
        transaction_entity = self.__database.query(TransactionEntity).get(transaction_id)

        if not transaction_entity:
            return None

        updated_transaction = transaction.__dict__

        for key, value in updated_transaction.items():
            setattr(transaction_entity, key, value)

        self.__database.commit()
        self.__database.refresh(transaction_entity)

        transaction_schema = TransactionSchema(**transaction_entity.__dict__)
        return transaction_schema

    def delete(self, transaction_id):
        transaction = self.__database.query(TransactionEntity).get(transaction_id)

        if not transaction:
            return None

        self.__database.delete(transaction)
        self.__database.commit()

        return True
