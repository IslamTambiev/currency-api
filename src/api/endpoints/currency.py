from fastapi import APIRouter, Depends

from src.api.models.models import CurrencyPair
from src.core.security import get_current_active_user
from src.utils.external_api import currency_list, currency_convert

router = APIRouter()


@router.get('/', dependencies=[Depends(get_current_active_user)])
def root():
    return {'message': 'Go to /list for currency list and /exchange for currency exchange'}


@router.get('/list', dependencies=[Depends(get_current_active_user)])
async def get_currency_list():
    data = currency_list()
    return data


@router.get('/exchange', dependencies=[Depends(get_current_active_user)])
async def get_currency_exchange(pair: CurrencyPair):
    data = currency_convert(pair)
    return data
