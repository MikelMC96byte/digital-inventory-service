from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/companies",
    tags=["Companies"],
    responses={
        404: {"description": "Company or companies not found"},
        403: {"description": "Operation not allowed"}
    }
)

fake_companies_db = [
    {
        "id": 1,
        "id_company_group": 1,
        "name": "COMPANY A"
    },
    {
        "id": 2,
        "id_company_group": 1,
        "name": "COMPANY B"
    },
    {
        "id": 3,
        "id_company_group": 1,
        "name": "COMPANY C"
    }
]

@router.get("/")
async def read_companies():
    return fake_companies_db

@router.get("/{id}")
async def read_company(id: int):
    for company in fake_companies_db:
        if company["id"] == id:
            return company
    return HTTPException(404)