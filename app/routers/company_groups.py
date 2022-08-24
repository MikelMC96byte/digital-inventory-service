from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/company-groups",
    tags=["Company Groups"],
    responses={
        404: {"description": "Company group or groups not found"},
        403: {"description": "Operation not allowed"}
    }
)

fake_company_group_db = [
    {
        "id": 1,
        "name": "GROUP A"
    },
    {
        "id": 2,
        "name": "GROUP B"
    }
]

@router.get("/")
async def read_company_groups():
    return fake_company_group_db

@router.get("/{id}")
async def read_company_group(id: int):
    for group in fake_company_group_db:
        if group["id"] == id:
            return group
    return HTTPException(404)