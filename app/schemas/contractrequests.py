from pydantic import BaseModel, EmailStr

from app.schemas.requests import BaseRequest

class ContractRequest(BaseRequest):
    ContractAddress: str
