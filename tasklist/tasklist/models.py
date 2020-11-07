# pylint: disable=missing-module-docstring,missing-class-docstring
from typing import Optional
import uuid

from pydantic import BaseModel, Field  # pylint: disable=no-name-in-module


# pylint: disable=too-few-public-methods
class Task(BaseModel):
    uuiduser: Optional[str] = Field(
        title='uuid user',
    )
    description: Optional[str] = Field(
        'no description',
        title='Task description',
        max_length=1024,
    )
    completed: Optional[bool] = Field(
        False,
        title='Shows whether the task was completed',
    )

    class Config:
        schema_extra = {
            'example': {
                'uuiduser':'3fa85f64-5717-4562-b3fc-2c963f66afa6',
                'description': 'Buy baby diapers',
                'completed': False,
            }
        }

# pylint: disable=too-few-public-methods
class User(BaseModel):
    user: str = Field(max_length=32)
    
