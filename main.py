""""this is the main module"""

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from datetime import date
from api.models import Pet_request, Pet_response
from db.model import petadoption
from db.database import get_db, Base, engine

# create db tables
Base.metadata.create_all(bind=engine)
app = FastAPI()

#get pets response here

@app.get("/pets", response_model=list[Pet_response])
def list_pets(db: Session = Depends(get_db)):
    return db.query(petadoption).all()

@app.get("/pets/{pet_id}", response_model=Pet_response)
def get_pet(pet_id: int, db:Session = Depends(get_db)):
    return db.query(petadoption).filter(petadoption.id == pet_id).first()

@app.post("/pets", response_model=Pet_response)
def new_pet(request: Pet_request, db: Session = Depends(get_db)):

   db_pets = petadoption(**request.model_dump())
   db.add(db_pets)
   db.commit()
   db.refresh(db_pets)
   return db_pets

@app.delete("/pets/{pet_id}")
def delete_pet(pet_id: int, db: Session = Depends(get_db)):
    db_pets = db.query(petadoption).filter(petadoption.id == pet_id).first()
    if db_pets:
        db.delete(db_pets)
        db.commit()
    return {"message": f"Pet {pet_id} Deleted Successfully"}

@app.put("/pets/{pet_id}", response_model=Pet_response)
def update_pet(pet_id: int,pet_update: dict, db: Session = Depends(get_db)):
    db_pets = db.query(petadoption).filter(petadoption.id == pet_id).first()
    for key, value in pet_update.items():
        if hasattr(db_pets, key) and value is not None:
            setattr(db_pets, key, value)
    
    db.commit()
    db.refresh(db_pets)
    return db_pets

