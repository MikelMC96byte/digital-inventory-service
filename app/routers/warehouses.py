from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/warehouses",
    tags=["Warehouses"],
    responses={
        404: {"description": "Warehouse or warehouses not found"},
        403: {"description": "Operation not allowed"}
    }
)

fake_db = [
    {
        "id": 1,
        "name": "WAREHOUSE A"
    },
    {
        "id": 2,
        "name": "WAREHOUSE B"
    }
]

@router.get("")
async def read_warehouses():
    return fake_db

@router.get("/{id}")
async def read_warehouse(id: int):
    for group in fake_db:
        if group["id"] == id:
            return group
    return HTTPException(404)