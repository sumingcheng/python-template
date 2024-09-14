from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate


class ItemService:
    def create_item(self, db: Session, item_in: ItemCreate, owner_id: int) -> Item:
        item = Item(
            name=item_in.name,
            description=item_in.description,
            owner_id=owner_id
        )
        db.add(item)
        db.commit()
        db.refresh(item)
        return item


item_service = ItemService()
