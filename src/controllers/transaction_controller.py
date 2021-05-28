from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from src.schemas.transaction_schema import TransactionSchema, TransactionCreateSchema
from src.repositories.postgres.sqlalchemy import get_database
from src.repositories.postgres.transaction_repository import TransactionRepository

transaction_router = APIRouter(prefix='/transaction')


@transaction_router.get('/', response_model=List[TransactionSchema])
def get_all_transaction(session: Session = Depends(get_database)):
    repository = TransactionRepository(session)
    transaction = repository.get_all()
    return transaction


@transaction_router.get('/{transaction_id}', response_model=TransactionSchema)
def get_transaction_by_id(transaction_id: int, session: Session = Depends(get_database)):
    repository = TransactionRepository(session)
    transaction = repository.get_one(transaction_id)
    if not transaction:
        response = {'detail': 'Transaction not found!'}
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=response)
    return transaction


@transaction_router.post('/', response_model=TransactionSchema)
def create_transaction(transaction: TransactionCreateSchema, session: Session = Depends(get_database)):
    repository = TransactionRepository(session)
    transaction = repository.create(transaction)
    return transaction


@transaction_router.put('/{transaction_id}', response_model=TransactionSchema)
def update_transaction_by_id(transaction_id: int, transaction: TransactionCreateSchema, session: Session = Depends(get_database)):
    repository = TransactionRepository(session)
    transaction = repository.update(transaction_id, transaction)
    if not transaction:
        response = {'detail': 'Transaction not found!'}
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=response)
    return transaction


@transaction_router.delete('/{transaction_id}')
def delete_transaction_by_id(transaction_id: int, session: Session = Depends(get_database)):
    repository = TransactionRepository(session)
    deleted = repository.delete(transaction_id)
    if not deleted:
        response = {'detail': 'Transaction not found!'}
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=response)
    return 'successfully deleted'
