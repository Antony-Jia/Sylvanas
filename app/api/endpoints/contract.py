from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import deps
from app.models.models import User
from app.models.contractmodels import Contract
from app.schemas.contractrequests import ContractRequest
from app.schemas.contractresponses import ContractResponse



router = APIRouter()


@router.post("/create", response_model=ContractResponse, status_code=201)
async def create_new_pet(
    contract: ContractRequest,
    session: AsyncSession = Depends(deps.get_session),
    current_user: User = Depends(deps.get_current_user),
):
    """Creates new pet. Only for logged users."""

    contract = Contract(name=contract.ContractAddress)

    session.add(contract)
    await session.commit()
    return contract


@router.get("/list", response_model=list[ContractResponse], status_code=200)
async def get_all_contracts(
    session: AsyncSession = Depends(deps.get_session),
    current_user: User = Depends(deps.get_current_user),
):
    """Get list of pets for currently logged user."""

    contracts = await session.execute(
        select(Contract)

        .order_by(Contract.name)
    )
    return contracts.scalars().all()