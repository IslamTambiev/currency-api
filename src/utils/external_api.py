from requests import get, Response
from src.core.config import config
from src.api.models.models import CurrencyPair

URL = "https://api.apilayer.com/currency_data/"

payload = {}
headers = {"apikey": config.api_key, }


def currency_list() -> dict:
    response: Response = get(URL + "list", headers=headers, data=payload)
    return response.json()["currencies"]


def currency_convert(pair: CurrencyPair) -> float:
    response: Response = get(
        URL + f"convert?to={pair.quote}&from={pair.base}&amount={pair.amount}",
        headers=headers, data=payload,
    )
    return response.json()  # ["result"]

