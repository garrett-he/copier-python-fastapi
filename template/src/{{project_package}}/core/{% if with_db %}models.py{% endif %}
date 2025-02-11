import uuid
from typing import Annotated

from sqlmodel import Field, SQLModel


class Sample(SQLModel, table=True):
    __tablename__ = 'samples'
    id: Annotated[uuid.UUID, Field(default_factory=uuid.uuid4, primary_key=True, max_length=36, min_length=36)]
