from abc import ABC, abstractmethod


class GameRepository(ABC):

    @abstractmethod
    def create(self, **data):
        pass

    @abstractmethod
    def list_all(self):
        pass

    @abstractmethod
    def get_by_id(self, game_id):
        pass

    @abstractmethod
    def update(self, game, **data):
        pass
