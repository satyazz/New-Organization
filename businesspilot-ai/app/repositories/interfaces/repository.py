from abc import ABC,abstractmethod
from typing import Generic,Optional,Sequence,TypeVar
from app.repositories.base.base_repository import BaseRepository 
T = TypeVar("T")

class IRepository (Generic[T],ABC):
    @abstractmethod
    def add(self,entity : T) ->T :
        """presist a new entity"""

    @abstractmethod
    def get_by_id(self,entity_id: T)->Optional[T]:
        """return entity by its id ...or identifier"""

    @abstractmethod
    def list(self) ->Sequence[T]:
        """return all entityes"""

    @abstractmethod
    def update(self,entity: T) -> T:
        """Presist update to an entity"""

    @abstractmethod
    def delete(self, entity: T) -> None:
        """delete an entity"""

    @abstractmethod
    def exists(self,entity: T) -> bool:
        """Return Ture if entity is exisits """`````   ``