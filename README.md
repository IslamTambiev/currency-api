# API обмена валют

## Используемые технологии
- FastAPI для создания API с автоматической документацией.
- Pydantic для валидации данных.
- OAuth2 с паролем (и хешированием), Bearer с JWT токенами.
- Хранение JWT токенов в куки файлах и ограниченный срок действия токена.
- Внешний API для получения обменных курсов с помощью requests.
- Модульное тестирование с использованием pytest.
- Конфигурация переменных окружения с использованием environs.
- HTML страницы с CSS и JavaScript для отображения данных.
- Jinja для шаблонизации HTML страниц.
- Запуск приложения с использованием uvicorn.

## Установка 🔧

### 1. Настройка проекта
- Создайте виртуальное окружение и активируйте его.
- Установите зависимости из файла `requirements.txt`.
  ```shell
  pip install -r requirements.txt
  ```

### 2. Конфигурация среды
- Переименуйте файл `.env.example` на `.env` в корне проекта и заполните необходимые конфиденциальные переменные:
    ```
    CURRENCY_API_KEY=your_api_key
    SECRET_KEY=your_secret_key
    ```

### 3. Запуск приложения
- Приложение будет доступно по адресу `http://127.0.0.1:8000`.
  ```shell
  uvicorn main:app --reload
  ```

## Тестирование
- Запустите тесты папки `tests` с помощью команды `pytest`.

## Примеры запросов API

- **Вход пользователя и получение JWT-токена:**
    ```shell
    curl -X POST 'http://127.0.0.1:8000/auth/login/' --header 'content-type: application/x-www-form-urlencoded' --form 'username="john"' --form 'password="pass"''
    ```

- **Получение списка поддерживаемых валют и их кодов (валидный JWT-токен):**
    ```shell
    curl -X GET 'http://127.0.0.1:8000/currency/get_list/' --header 'Cookie: access_token="Bearer your_jwt_token"'  
    ```

- **Обмен валюты (валидный JWT-токен):**
    ```shell
    curl -X GET 'http://127.0.0.1:8000/currency/exchange/?base=usd&quote=rub&amount=1000' --header 'Cookie: access_token="Bearer your_jwt_token"'  
    ```

## Примеры ответов API
- **При успешном входе и токен сохраняется в куки файлах:**
    ```text
    'Cookie: access_token="Bearer received_jwt_token"'
    ```
- **Список поддерживаемых валют:**
    ```json
    {
        "AED": "United Arab Emirates Dirham",
        "AFN": "Afghan Afghani",
        "ALL": "Albanian Lek",
        ...
    }
    ```
- **Успешный обмен валюты:**
    ```json
    {
        "success": true,
        "query": {
            "from": "USD",
            "to": "RUB",
            "amount": 1000
        },
        "info": {
            "timestamp": 1700419983,
            "quote": 89.350433
        },
        "result": 89350.433
    }
    ```

## Примеры запросов и ответов с помощью Postman
<p align="center"><img src="https://i.ibb.co/cx8X67X/2023-11-19-221513.png" alt="img"></p>
<p align="center"><img src="https://i.ibb.co/hB8QhpH/2023-11-19-221715.png" alt="img"></p>
<p align="center"><img src="https://i.ibb.co/nQyrmMn/2023-11-19-221823.png" alt="img"></p>

## HTML страницы для удобства выполнения запросов
<p align="center"><img src="https://i.ibb.co/2M29gpj/2023-11-19-222658.png" alt="img"></p>
<p align="center"><img src="https://i.ibb.co/VN48pDf/2023-11-19-222744.png" alt="img"></p>
<p align="center"><img src="https://i.ibb.co/wrhWtjW/2023-11-19-222755.png" alt="img"></p>
