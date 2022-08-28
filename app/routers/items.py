from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/items",
    tags=["Items"],
    responses={
        404: {"description": "Item or items not found"},
        403: {"description": "Operation not allowed"}
    }
)

fake_db = [
    {
        "id": 1,
        "id_item_type": 1,
        "name": "ITEM A"
    },
    {
        "id": 2,
        "id_item_type": 1,
        "name": "ITEM B"
    }
]

@router.get("")
async def read_items():
    return fake_db

@router.get("/{id}")
async def read_item(id: int):
    for group in fake_db:
        if group["id"] == id:
            return group
    return HTTPException(404)