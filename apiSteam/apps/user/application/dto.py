from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class CreateUserDTO:
    username: str
    email: str
    password: str
    rol: Optional[str] = 'user'
    state_account: Optional[str] = 'ACTIVE'
    balance: Optional[float] = 0.00
    nationality: Optional[str] = None
    ip_address: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

@dataclass(frozen=True)
class UpdateUserDTO:
    user_id: int
    email: Optional[str] = None
    rol: Optional[str] = None
    state_account: Optional[str] = None
    balance: Optional[float] = None