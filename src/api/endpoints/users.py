from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Request, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security.api_key import APIKeyHeader

from src.api.models.models import User, Token
from src.core.security import get_current_active_user, create_access_token, authenticate_user
from src.database import fake_users_db
from src.core.config import config

router = APIRouter()
templates = Jinja2Templates(directory="templates")
token_key = APIKeyHeader(name="Authorization")


@router.get('/')
def root():
    return {'message': 'Go to / and /'}


@router.get("/login", response_class=HTMLResponse)
async def login_for_access_token(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("login.html", context)


@router.post("/login", response_model=Token)
async def login_for_access_token(response: Response, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """
        Endpoint to authenticate a user and generate an access token.
        Args:
            form_data (OAuth2PasswordRequestForm): The form data containing the username and password.
        Returns:
            dict: A dictionary containing the access token and token type.
            :param form_data:
            :param response:
        """
    # Authenticate the user
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    # Raise an exception if the user is not authenticated
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Set the access token expiration time
    access_token_expires = timedelta(minutes=config.token.access_token_expires_in)
    # Create the access token
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    # Set the cookie with the access token
    response.set_cookie("access_token", value=f"Bearer {access_token}", httponly=True)
    # Return the access token and token type
    return {"access_token": access_token, "token_type": "bearer"}  # Response(status_code=200,


@router.get("/me/", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user


@router.get("/items/")
async def read_own_items(current_user: Annotated[User, Depends(get_current_active_user)]):
    return [{"item_id": "Foo", "owner": current_user.username}]
