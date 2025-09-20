from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.schemas.project import ProjectCreate, ProjectUpdate, ProjectInDB
from backend.app.services import project as project_service
from backend.app.core.database import get_db

router = APIRouter()

@router.post("/projects/", response_model=ProjectInDB, status_code=status.HTTP_201_CREATED, tags=["Projects"])
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    return project_service.create_project(db=db, project=project)

@router.get("/projects/", response_model=List[ProjectInDB], tags=["Projects"])
def read_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    projects = project_service.get_projects(db=db, skip=skip, limit=limit)
    return projects

@router.get("/projects/{project_id}", response_model=ProjectInDB, tags=["Projects"])
def read_project(project_id: int, db: Session = Depends(get_db)):
    db_project = project_service.get_project(db=db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return db_project

@router.put("/projects/{project_id}", response_model=ProjectInDB, tags=["Projects"])
def update_project(project_id: int, project: ProjectUpdate, db: Session = Depends(get_db)):
    db_project = project_service.update_project(db=db, project_id=project_id, project=project)
    if db_project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return db_project

@router.delete("/projects/{project_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Projects"])
def delete_project(project_id: int, db: Session = Depends(get_db)):
    db_project = project_service.delete_project(db=db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return {"message": "Project deleted successfully"}
