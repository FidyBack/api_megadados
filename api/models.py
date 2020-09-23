from pydantic import BaseModel, Field

class Task(BaseModel):
    description: str = Field(
        'no description',
        title='Task description',
        max_length=1024,
    )
    completed: bool = Field(
        False,
        title='Shows whether the task was completed',
    )

    class Config:
        schema_extra = {
            'example': {
                'description': 'Buy baby diapers',
                'completed': False,
            }
        }