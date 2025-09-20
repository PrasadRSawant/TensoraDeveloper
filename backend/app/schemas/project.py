from pydantic import BaseModel, HttpUrl

class ProjectBase(BaseModel):
    title: str
    description: str
    image_url: HttpUrl | None = None
    project_url: HttpUrl | None = None
    github_url: HttpUrl | None = None

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    title: str | None = None
    description: str | None = None

class ProjectInDB(ProjectBase):
    id: int

    class Config:
        from_attributes = True
