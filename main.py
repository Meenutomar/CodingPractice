from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from fastapi.responses import JSONResponse
import os
import json
from datetime import datetime
from controller.films import actor
import controller.products.products as products
import controller.users.users as users
import controller.customers.customers as customers
import controller.payments.payment as payments
import controller.films.FilmController as films
from controller.films import actor as actors
from controller.staffs import staffs as staffs
from controller.category import CategoryController as categories
from logging_config import configure_logging


app = FastAPI()

configure_logging()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(products.router)
app.include_router(users.router)
app.include_router(customers.router)
app.include_router(payments.router)
app.include_router(films.router)
app.include_router(actors.router)
app.include_router(staffs.router)
app.include_router(categories.router)




