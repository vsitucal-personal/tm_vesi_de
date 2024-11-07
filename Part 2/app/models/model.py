from typing import Union, List
from pydantic import BaseModel, Field
from datetime import date
from fastapi import Query


class CheckinsModel(BaseModel):
    user: str
    hours: float
    project: str
    date: date


class ReturnCheckin(BaseModel):
    total_count: int
    returned_count: int
    records: List[CheckinsModel]


class GetCheckin(BaseModel):
    page: int = Query(1, ge=1)  # Page number, default is 1, with validation that it should be >= 1
    page_size: int = Query(20)  # Page size, default is 20, with validation that it should be <= 1000
    user: str = Query(...)  # Required field for the username