from sqlalchemy.orm import declared_attr
from sqlalchemy import DateTime, Column
from datetime import datetime
from typing import Optional

from src.core.db import Base as DeclarativeBase


class Base(DeclarativeBase):
    __abstract__ = True

    id: Optional[int]

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class CoreModel(Base):
    __abstract__ = True


class TimestampModel(CoreModel):
    __abstract__ = True

    created_at = Column(
        DateTime(timezone=True), default=datetime.utcnow, nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )


class SoftDeleteModel(CoreModel):
    __abstract__ = True

    deleted_at = Column(DateTime(timezone=True), nullable=True)

    @property
    def is_deleted(self) -> bool:
        return self.deleted_at is not None


class BaseModel(TimestampModel, SoftDeleteModel):
    __abstract__ = True
