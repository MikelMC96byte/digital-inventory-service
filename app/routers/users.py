from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={
        404: {"description": "User or users not found"},
        403: {"description": "Operation not allowed"}
    }
)

fake_db = [
    {
        "id": 1,
        "id_company": 1,
        "role": 1,
        "name": "USER A"
    },
    {
        "id": 2,
        "id_company": 1,
        "role": 1,
        "name": "USER B"
    }
]

@router.get("")
async def read_users():
    return fake_db

@router.get("/{id}")
async def read_user(id: int):
    for group in fake_db:
        if group["id"] == id:
            return group
    return HTTPException(404)