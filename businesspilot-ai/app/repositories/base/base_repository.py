from typing import Type,Generic,Optional,Sequence
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.repositories.interfaces.repository import IRepository ,T

class BaseRepository (Generic[T],IRepository[T]):
    def __int__(
            self,
            session : Session,
            model: Type[T],
                ) -> None:
        self._session = session
        self._model = model

    def add(self,entity : T)-> T:
        self._session.add(entity)
        return entity

    def get_by_id(self, entity_id)->Optional[T]:
        return self._session.get(self._model,entity_id)

    def list(self)->Sequence[T]:
        statement = select(self._model)
        return self._session.scalars(statement).all()

    def update(self, entity)-> T:
        return self._session.merge(entity)

    def delete(self, entity)-> None:
        return self._session.delete(entity)

    def exists(self, entity_id: int)->bool:
        return self._session.get(self._model,entity_id) is not None
        

