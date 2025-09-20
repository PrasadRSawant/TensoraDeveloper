from typing import Optional
from datetime import datetime
from pydantic import BaseModel, HttpUrl

class ProjectBase(BaseModel):
    title: str
    description: str
    image_url: Optional[HttpUrl] = None
    project_url: Optional[HttpUrl] = None
    github_url: Optional[HttpUrl] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    pass

class ProjectInDB(ProjectBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
