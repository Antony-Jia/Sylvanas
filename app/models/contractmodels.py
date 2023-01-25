import uuid
from dataclasses import dataclass, field

from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import registry

ContractBase = registry()

@ContractBase.mapped
@dataclass
class Contract:
    __tablename__ = "contract"
    __sa_dataclass_metadata_key__ = "sa"
    
    id: int = field(init=False, metadata={"sa": Column(Integer, primary_key=True)})
    name: str = field(default=None, metadata={"sa": Column(String(50))})