from sqlalchemy import Column, Float,Integer, String,ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class BrandsModels(Base):
    __tablename__ = "brands"
    id =Column(Integer, primary_key=True, autoincrement= True)
    name = Column(String(50), unique=True, nullable=False)
    
    brand = relationship('PhoneModels',back_populates='phone')
    
class PhoneModels(Base):
    __tablename__ = "phones"
    id =Column(Integer, primary_key=True, autoincrement= True)
    phone_code = Column(String(10), unique=True, nullable=False)
    price = Column(Float, nullable= False)
    brand_id = Column(Integer,ForeignKey(BrandsModels.id), nullable=False)
    
    phone = relationship('BrandsModels',back_populates='brand')
    