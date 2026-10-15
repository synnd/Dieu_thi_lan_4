from pydantic import BaseModel,Field
from typing import Any


class CreatePhone(BaseModel):
    phone_code : str = Field(...,min_length=4, max_length=10)
    price : float = Field(..., gt=0)
    brand_id : int = Field(...,)
    


class BrandResponse(BaseModel):
    id: int
    name: str
class PhoneResponse(BaseModel):
    id : int
    phone_code : str
    price : float
    brand_id : BrandResponse
    
def create_response(
    statusCode : int,
    message : str,
    data :  Any = None,
    error : str = None,
):
    return statusCode , message , data , error 

