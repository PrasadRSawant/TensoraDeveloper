from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(Text, nullable=False)
    image_url = Column(String, nullable=True)
    project_url = Column(String, nullable=True)
    github_url = Column(String, nullable=True)
