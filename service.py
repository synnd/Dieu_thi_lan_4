from sqlalchemy.orm import Session
from models import PhoneModels, BrandsModels
from schemas import CreatePhone

def get_all_phones_service(db: Session):
    return db.query(PhoneModels).all()
    
    
def create_phone_service(phone :CreatePhone ,db: Session):
    phone_code =db.query(PhoneModels).filter(PhoneModels.phone_code == phone.phone_code).first()
  
    brand = db.query(PhoneModels).filter(BrandsModels.id == phone.brand_id).first()
    
    if  phone_code:
        return None
    if not  brand :
        return False
    new_phone = PhoneModels(**phone.model_dump())
    db.add(new_phone)
    db.commit()
    db.refresh(new_phone)
    return new_phone

def delete_phone_service(id: int, db: Session):
    delete_phone = db.query(PhoneModels).filter(PhoneModels.id == id).first()
    
    if delete_phone:
        db.delete(delete_phone)
        db.commit()
        return delete_phone
    return None