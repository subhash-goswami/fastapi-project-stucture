from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class CoreSchema(BaseModel):
    class Config:
        orm_mode = True


class TimestampSchema(CoreSchema):
    created_at: Optional[datetime] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)


class SoftDeleteSchema(CoreSchema):
    deleted_at: Optional[datetime] = None

    @property
    def is_deleted(self) -> bool:
        return self.deleted_at is not None


class BaseSchema(TimestampSchema, SoftDeleteSchema):
    pass
