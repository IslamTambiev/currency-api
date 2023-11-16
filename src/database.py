from src.api.models.models import UserInDB

fake_users_db = {
    "john": {
        "username": "john",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$NqYBREI5fQCcJdVeDPy/DOktc70404zc7Lit1L9i01P1itr47gJ16",
        "disabled": False,
    }
}


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
