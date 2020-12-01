from datetime import datetime
from typing import Optional

class User(object):
    """
    class representing a user
    """
    username: str
    password: str

class Note(object):
    """
    class representing a note
    """
    identifier: int
    title: str
    content: str
    created_at: datetime
    username: str
    notes: list[Note]

_users: list[User] = []
_notes: list[Note] = []

def add_user(user: User) -> bool:
    if any(u.username == user.username for u in _users):
        return False
    _users.append(user)
    return True

def get_users() -> list[User]:
    return _users

def get_user(username: str) -> Optional[User]:
    filtered: list[User] = filter(lambda x: x.username == username, _users)
    filtered_count = len(filtered)
    if filtered_count == 1: return filtered[0]
    elif filtered_count == 0: return None
    else: raise Exception("users data is in invalid state")

def add_note(note: Note) -> bool:
    if get_user(note.username) == None:
        return False
    if _notes.count > 0:
        last_identifier = _notes[-1].identifier
        note.identifier = last_identifier
    else:
        note.identifier = 1
    _notes.append(note)

def get_notes() -> list[Note]:
    return _notes

def get_note(identifier: str) -> Optional[Note]:
    filtered: list[Note] = filter(lambda x: x.identifier == identifier, _notes)
    filtered_count = len(filtered)
    if filtered_count == 1: return filtered[0]
    elif filtered_count == 0: return None
    else: raise Exception("notes data is in invalid state")