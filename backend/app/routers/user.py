from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user import UserCreate, User
from app.services.user import UserService
from app.utils.security import get_password_hash # Assuming this utility will be created

router = APIRouter()

@router.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(db)
    db_user = user_service.get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    return user_service.create_user(user=user, hashed_password=hashed_password)

@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user_service = UserService(db)
    db_user = db.query(user_service.get_user_by_email).filter(user_service.get_user_by_email.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user