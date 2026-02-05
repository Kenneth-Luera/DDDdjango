from abc import ABC, abstractmethod
from apiSteam.apps.user.domain.entities.user import User

class UserRepository(ABC):
    @abstractmethod
    def create_user(self, *, username: str, email: str, password: str, rol: str, account: str) -> User:
        pass

    @abstractmethod
    def get_all(self) -> list[User]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User:
        pass