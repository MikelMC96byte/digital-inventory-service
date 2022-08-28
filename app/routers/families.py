from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/families",
    tags=["Families"],
    responses={
        404: {"description": "Family or families not found"},
        403: {"description": "Operation not allowed"}
    }
)

fake_db = [
    {
        "id": 1,
        "name": "FAMILY A"
    },
    {
        "id": 2,
        "name": "FAMILY B"
    }
]

@router.get("")
async def read_families():
    return fake_db

@router.get("/{id}")
async def read_family(id: int):
    for group in fake_db:
        if group["id"] == id:
            return group
    return HTTPException(404)