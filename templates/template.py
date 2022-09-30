from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from starlette.background import BackgroundTasks

from schema import ProductBase

router = APIRouter(
    prefix='/templates',
    tags=['templates']
)

templates = Jinja2Templates(directory='templates')


def log(tag="", message=""):
    with open("log.txt", mode="w+") as log:
        log.write(f"{tag}: {message}\n")


def log_template_call(message: str):
    log("MyAPI", message)


@router.get('/product/{id}', response_class=HTMLResponse)
def get_product(id: str,
                request: Request,
                bt: BackgroundTasks):
    bt.add_task(log_template_call, f"Template read for product with id {id}")
    return templates.TemplateResponse(
        "product.html",
        {"request": request,
         "id": id,
         "title": "Nike Phantom GT2 Academy Dynamic Fit MG Football Boots",
         "description": "Building on the Phantom GT, the Nike Phantom GT2 Dynamic "
                        "Fit MG has an updated design and patterning that are engineered "
                        "to help you place your shots with pinpoint accuracy. ",
         "price": 94.153
         })


@router.post('/product/{id}', response_class=HTMLResponse)
def post_product(id: str, product: ProductBase, request: Request):
    return templates.TemplateResponse(
        "product.html",
        {"request": request,
         "id": id,
         "title": product.title,
         "description": product.description,
         "price": product.price
         })
