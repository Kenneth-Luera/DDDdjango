import re

class Username:
    def __init__(self, username: str):
        if not re.match(r'^[a-zA-Z0-9_]{3,30}$', username):
            raise ValueError("Invalid username format")
        self._username = username

    @property
    def value(self) -> str:
        return self._username

class Email:
    def __init__(self, email: str):
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise ValueError("Invalid email format")
        self._email = email

    @property
    def value(self) -> str:
        return self._email
    
class Rol:
    def __init__(self, role: str):
        valid_roles = {'admin', 'user'}
        if role not in valid_roles:
            raise ValueError("Invalid role")
        self._role = role

    @property
    def value(self) -> str:
        return self._role

class AccountStatus:
    def __init__(self, status: str):
        valid_statuses = {'active', 'inactive', 'suspended'}
        if status not in valid_statuses:
            raise ValueError("Invalid account status")
        self._status = status

    @property
    def value(self) -> str:
        return self._status
    
class Balance:
    def __init__(self, amount: float):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._amount = amount

    @property
    def value(self) -> float:
        return self._amount
    
class Password:
    def __init__(self, password: str):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        self._password = password

    @property
    def value(self) -> str:
        return self._password


