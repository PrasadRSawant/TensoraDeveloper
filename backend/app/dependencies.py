from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.utils.security import decode_access_token
# In a real application, you would have a user model and service
# from backend.app.models.user import User
# from backend.app.services.user import get_user_by_email

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # This will be for admin login later

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exception
    # In a real application, you would fetch the user from the database
    # user = get_user_by_email(db, email=payload.get("sub"))
    # if user is None:
    #     raise credentials_exception
    # For now, we'll just return the payload subject as a placeholder for the user
    user_email = payload.get("sub")
    if user_email is None:
        raise credentials_exception
    return {"email": user_email, "id": 1} # Placeholder user
