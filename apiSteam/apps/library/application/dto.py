from dataclasses import dataclass


@dataclass
class AddGameDTO:
    user_id: int
    game_id: int
