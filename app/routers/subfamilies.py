from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/subfamilies",
    tags=["Subfamilies"],
    responses={
        404: {"description": "Item or items not found"},
        403: {"description": "Operation not allowed"}
    }
)

fake_db = [
    {
        "id": 1,
        "id_family": 1,
        "name": "FAMILY A"
    },
    {
        "id": 2,
        "id_family": 1,
        "name": "FAMILY B"
    }
]

@router.get("")
async def read_subfamilies():
    return fake_db

@router.get("/{id}")
async def read_subfamily(id: int):
    for group in fake_db:
        if group["id"] == id:
            return group
    return HTTPException(404)