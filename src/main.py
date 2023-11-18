import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

from src.api.endpoints.users import router as user_router
from src.api.endpoints.currency import router as curr_router

app = FastAPI()
app.include_router(user_router, prefix='/auth')
app.include_router(curr_router, prefix='/currency')
app.mount("/auth/static", StaticFiles(directory="static", html=True), name="static")
app.mount("/currency/static", StaticFiles(directory="static", html=True), name="static")


@app.exception_handler(ValueError)
async def value_error_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=422,
        content={"message": str(exc)},
    )


@app.get('/')
async def root():
    return {'message': 'Go to /auth for authentication and /currency for currency'}


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1',
                port=8080, reload=True, workers=1)
