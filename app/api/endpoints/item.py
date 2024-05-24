from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.schemas.item import Item, ItemCreate
from app.api.deps import get_db

router = APIRouter()

@router.post("/", response_model=Item)
def create_item(
    item_in: ItemCreate, db: Session = Depends(get_db), user_id: int = 1  # Dummy user_id for simplicity
):
    return crud.item.create_item(db=db, item=item_in, user_id=user_id)

@router.get("/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = crud.item.get_items(db, skip=skip, limit=limit)
    return items

@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.item.get_item(db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, item_in: ItemCreate, db: Session = Depends(get_db)):
    item = crud.item.update_item(db, item_id=item_id, item=item_in)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.delete("/{item_id}", response_model=Item)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.item.delete_item(db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
