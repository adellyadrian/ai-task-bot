from app.models import TaskSource, TaskStatus
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=500)
    source: TaskSource
    telegram_id: int
    model_config = ConfigDict(str_strip_whitespace=True)




class TaskStatusUpdate(BaseModel):
    status: TaskStatus




class TaskRead(BaseModel):
    id: int
    user_id: int
    title: str
    status: TaskStatus
    source: TaskSource
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
