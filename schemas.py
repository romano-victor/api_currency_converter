import re

from pydantic import BaseModel, Field, field_validator
from typing import List

class ConverterInput(BaseModel):
    price: float = Field(gt=0)
    to_currencies: List[str]

    @field_validator('to_currencies')
    def to_currencies_validator(cls, value):
        for currency in value:
            if not re.match('^[A-Z]{3}$', currency):
                raise ValueError('Currency must be 3 uppercase letters')
        
        return value
    

class ConverterOutput(BaseModel):
    message: str
    data: List[dict]

