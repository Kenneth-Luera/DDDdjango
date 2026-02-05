from abc import ABC, abstractmethod


class LibraryRepository(ABC):

    @abstractmethod
    def add_game(self, user, game):
        pass

    @abstractmethod
    def list_by_user(self, user):
        pass

    @abstractmethod
    def remove_game(self, user, game):
        pass
