from abc import ABC, abstractmethod


class UserProfileRepository(ABC):

    @abstractmethod
    def create(self, user):
        pass

    @abstractmethod
    def get_by_user(self, user):
        pass

    @abstractmethod
    def update(self, profile, data):
        pass
