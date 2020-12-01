from fastapi import APIRouter

from data import datastore

router = APIRouter()

@router.get("")
async def get():
    return datastore.get_notes()

@router.get("/{identifier}")
async def get(identifier: str):
    return datastore.get_note(identifier)