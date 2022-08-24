from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime

router = APIRouter(
    prefix="/traces",
    tags=["Traces"],
    responses={
        404: {"description": "Trace or traces not found"},
        403: {"description": "Operation not allowed"}
    }
)

fake_traces_db = [
    {
        "id": 1,
        "action": "create",
        "data": {
            "id": 1
        },
        "user": 1,
        "timestamp": datetime.now()
    },
    {
        "id": 2,
        "action": "update",
        "data": {
            "old": {
                "id": 1,
                "id_article_type": 1,
                "id_warehouse": 1,
                "id_company": 1,
                "id_zone": 1
            },
            "new": {
                "id": 1,
                "id_article_type": 2,
                "id_warehouse": 1,
                "id_company": 1,
                "id_zone": 1
            }
        },
        "user": 1,
        "timestamp": datetime.now()
    },
    {
        "id": 3,
        "action": "delete",
        "data": {
            "id": 1,
            "id_article_type": 2,
            "id_warehouse": 1,
            "id_company": 1,
            "id_zone": 1
        },
        "user": 1,
        "timestamp": datetime.now()
    }
]

@router.get("/")
async def read_traces():
    return fake_traces_db

@router.get("/{id}")
async def read_trace(id: int):
    for trace in fake_traces_db:
        if trace["id"] == id:
            return trace
    return HTTPException(404)