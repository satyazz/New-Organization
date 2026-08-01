from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData

# Consistent naming conventions for constraints and indexes
NAMING_CONVENTION = {
    "ix": "ix_%(table_name)s_%(column_0_name)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk":("fk%(table_name)s"
          "%(column_0_name)s"
          "%(referred_table_name)s"
          ),
    "pk": "pk_%(table_name)s",
}

metadata =MetaData(naming_convention=NAMING_CONVENTION)

class Base(DeclarativeBase):
    """ Base class for all SQLAlchemy ORM models
    """
    metadata = metadata

