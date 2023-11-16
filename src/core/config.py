from dataclasses import dataclass
from environs import Env


@dataclass
class Token:
    secret_key: str
    algorithm: str
    access_token_expires_in: int


@dataclass
class Config:
    api_key: str
    token: Token


def load_config() -> Config:
    """
    Load the configuration settings from the environment variables and create a Config object.

    Returns:
        Config: The configuration object containing the loaded settings.
    """
    # Создаем экземпляр класса Env
    env: Env = Env()
    # Добавляем в переменные окружения данные, прочитанные из файла .env
    env.read_env()

    # Создаем экземпляр класса Config и наполняем его данными из переменных окружения
    return Config(api_key=env('CURRENCY_API_KEY'),
                  token=Token(secret_key=env('SECRET_KEY'), algorithm=env('ALGORITHM'),
                              access_token_expires_in=int(env('ACCESS_TOKEN_EXPIRE_MINUTES'))))


config: Config = load_config()
