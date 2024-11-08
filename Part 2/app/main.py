import math

from fastapi import FastAPI, Depends
from typing import List
from app.repository.db import DBConnect
from app.models.model import GetCheckin, ReturnCheckin


class Webserver:
    def __init__(self):
        self.app = FastAPI()
        self.setup_routes()
        self.db = DBConnect()

    def setup_routes(self):
        @self.app.get("/", status_code=201)
        async def read_root():
            return {"message": "Hi from root"}

        @self.app.get("/checkins", status_code=200, response_model=ReturnCheckin)
        async def get_checkins(
            params: GetCheckin = Depends()
        ):
            records, records_len = self.db.get_checkins_records(params.user, params.page, params.page_size)
            record_count = self.db.get_checkins_count(params.user)
            return ReturnCheckin(
                total_count=record_count,
                page=params.page,
                max_page=math.ceil(record_count/params.page_size),
                returned_count=records_len,
                records=records
            )


webserver = Webserver()
app = webserver.app