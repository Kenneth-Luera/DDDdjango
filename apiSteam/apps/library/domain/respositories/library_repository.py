from abc import ABC, abstractmethod


class LibraryRepository(ABC):

    @abstractmethod
    def get_library_by_user(self, user_id):
        pass

    @abstractmethod
    def add_game(self, library_id, game_id):
        pass

    @abstractmethod
    def remove_game(self, library_id, game_id):
        pass

    @abstractmethod
    def list_games(self, library_id):
        pass
