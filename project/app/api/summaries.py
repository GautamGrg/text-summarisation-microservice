# project/app/api/summaries.py

from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.tortoise import SummarySchema
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


@router.get(path="/{summary_id}/", response_model=SummarySchema)
async def read_summary(summary_id: int):
    if not await crud.get(summary_id):
        raise HTTPException(status_code=404, detail="Summary not found")
    return await crud.get(summary_id)


@router.get(path="/", response_model=list[SummarySchema])
async def read_all_summaries() -> list:
    return await crud.get_all()
