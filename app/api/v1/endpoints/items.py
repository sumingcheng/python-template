from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.item import ItemCreate, ItemOut
from app.services.item_service import item_service
from app.db.session import get_db
from app.api.deps import get_current_user
from app.models.user import User

router = APIRouter()


@router.post("/", response_model=ItemOut)
def create_item(
        item_in: ItemCreate,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    item = item_service.create_item(db, item_in, owner_id=current_user.id)
    return item
