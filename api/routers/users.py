from fastapi import APIRouter

from data import datastore

router = APIRouter()

@router.get("")
async def get():
    return datastore.get_users()

@router.get("/{username}")
async def get(username: str):
    return datastore.get_user(username)