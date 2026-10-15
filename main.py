from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from database import get_db, engine,Base
from models import BrandsModels, PhoneModels
from schemas import create_response, CreatePhone ,PhoneResponse
from service import get_all_phones_service,create_phone_service,delete_phone_service
app = FastAPI()

Base.metadata.create_all(engine)

@app.get('/test')
def test():
    return {
        'message': 'API chạy thành công'
    } 
    
    
@app.get('/phones')
def get_all_phone(db: Session= Depends(get_db)):
    list_phone = get_all_phones_service(db)
    return create_response(
        statusCode= status.HTTP_200_OK,
        message='Lấy danh sách điện thoại thành công',
        data = list_phone,
        error= None
    )
    
@app.post('/phones')
def create_phone(phone: CreatePhone, db: Session= Depends(get_db)):
    new_phone = create_phone_service(phone, db)
    if new_phone is None:
        return create_response(
            statusCode= status.HTTP_200_OK,
            message='Mã điện thoại bị trùng',
            data = None,
            error= None
        )
    if new_phone is False:
            return create_response(
                statusCode= status.HTTP_200_OK,
                message='Brand không tồn tại',
                data = None,
                error= None
            )
    return create_response(
            statusCode= status.HTTP_200_OK,
            message='Lấy danh sách điện thoại thành công',
            data = new_phone,
            error= None
        )

@app.delete('/phones/{id}')
def create_phone(id: int, db: Session= Depends(get_db)):
    delete_phone= delete_phone_service(id, db)
    if delete_phone is None:
            return create_response(
                statusCode= status.HTTP_200_OK,
                message='ID không tồn tại',
                data = None,
                error= None
            )
    return create_response(
            statusCode= status.HTTP_200_OK,
            message='Lấy danh sách điện thoại thành công',
            data = delete_phone,
            error= None
        )
        