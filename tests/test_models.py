import pytest
from pydantic import ValidationError
from src.api.models.models import Token, TokenData, User, UserInDB, CurrencyPair


# Тестирование модели Token
def test_token_model():
    token_data = {'access_token': 'test_access_token', 'token_type': 'bearer'}
    token = Token(**token_data)
    assert token.model_dump() == token_data


# Тестирование модели TokenData
def test_token_data_model():
    token_data = {'username': 'test_username'}
    token_data_model = TokenData(**token_data)
    assert token_data_model.model_dump() == token_data


# Тестирование модели User
def test_user_model():
    user_data = {'username': 'testusername', 'email': 'test@example.com', 'full_name': 'Test User', 'disabled': False}
    user = User(**user_data)
    assert user.model_dump() == user_data

    # Попытка создать пользователя с неверным именем пользователя
    with pytest.raises(ValidationError):
        User(username='us')  # Имя пользователя должно состоять из 3 или более символов


# Тестирование модели UserInDB
def test_user_in_db_model():
    user_in_db_data = {'username': 'testusername', 'email': 'test@example.com', 'full_name': 'Test User',
                       'disabled': False, 'hashed_password': 'hashed_password'}
    user_in_db = UserInDB(**user_in_db_data)
    assert user_in_db.model_dump() == user_in_db_data


# Тестирование модели CurrencyPair
def test_currency_pair_model():
    currency_pair_data = {'base': 'USD', 'quote': 'EUR', 'amount': 100}
    currency_pair = CurrencyPair(**currency_pair_data)
    assert currency_pair.model_dump() == currency_pair_data

    # Попытка создать CurrencyPair с недопустимыми значениями
    with pytest.raises(ValidationError):
        CurrencyPair(base='US', quote='EUR', amount=100)  # Недопустимый код валюты и отрицательное количество
    with pytest.raises(ValidationError):
        CurrencyPair(base='USD', quote='EUR', amount=-100)
    with pytest.raises(ValidationError):
        CurrencyPair(base='USD', quote='USD', amount=100)
