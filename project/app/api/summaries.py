# project/app/api/summaries.py

from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema

router = APIRouter()


@router.post(path="/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:
    """
    Sending HTTP POST method to /summaries/ endpoint with expected response 
    in `int` to match schema type. 
    """
    response_object = {
        "id": await crud.post(payload),
        "url": payload.url,
    }
    return response_object
