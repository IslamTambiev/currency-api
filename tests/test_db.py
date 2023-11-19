from src.api.models.models import UserInDB
from src.database import get_user


# Тестирование функции get_user
def test_get_user():
    # Подготовка тестовых данных
    fake_users_db = {
        "john": {
            "username": "john",
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "hashed_password": "$2b$12$NqYBREI5fQCcJdVeDPy/DOktc70404zc7Lit1L9i01P1itr47gJ16",
            "disabled": False,
        }
    }

    # Тестирование успешного получения пользователя
    username = "john"
    user = get_user(fake_users_db, username)
    assert isinstance(user, UserInDB)
    assert user.username == fake_users_db[username]["username"]
    assert user.full_name == fake_users_db[username]["full_name"]
    assert user.email == fake_users_db[username]["email"]
    assert user.hashed_password == fake_users_db[username]["hashed_password"]
    assert user.disabled == fake_users_db[username]["disabled"]

    # Тестирование случая, когда пользователя нет в базе данных
    non_existing_username = "nonexistent"
    user = get_user(fake_users_db, non_existing_username)
    assert user is None  # Функция должна вернуть None, если пользователя нет в базе данных
