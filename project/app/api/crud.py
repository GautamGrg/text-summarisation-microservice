# project/app/api/crud.py

from typing import Union
from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )
    await summary.save()
    return summary.id  # pylint: disable=E1101


async def get(summary_id: int) -> Union[dict | None]:
    summary = await TextSummary.filter(id=summary_id).first().values()
    if summary:
        return summary
    return None


async def get_all() -> list:
    summaries = await TextSummary.all().values()
    return summaries
