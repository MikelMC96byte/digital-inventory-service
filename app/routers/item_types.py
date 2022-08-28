from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/item-types",
    tags=["Item Types"],
    responses={
        404: {"description": "Item type or types not found"},
        403: {"description": "Operation not allowed"}
    }
)

fake_db = [
    {
        "id": 1,
        "name": "ITEM TYPE A"
    },
    {
        "id": 2,
        "name": "ITEM TYPE B"
    }
]

@router.get("")
async def read_item_types():
    return fake_db

@router.get("/{id}")
async def read_item_type(id: int):
    for group in fake_db:
        if group["id"] == id:
            return group
    return HTTPException(404)