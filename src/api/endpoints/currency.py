from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.api.models.models import CurrencyPair
from src.core.security import get_current_active_user
from src.utils.external_api import currency_list, currency_convert

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get('/', response_class=HTMLResponse, dependencies=[Depends(get_current_active_user)])
def root(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)


@router.get('/list/', dependencies=[Depends(get_current_active_user)])
async def get_currency_list():
    data = currency_list()
    return data


@router.get('/exchange/', dependencies=[Depends(get_current_active_user)])
async def get_currency_exchange(pair: CurrencyPair = Depends()):
    data = currency_convert(pair)
    return data
