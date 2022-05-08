from cmath import nan
from enum import Enum, auto
import random
from db_test import DataHandler

class genre(Enum):
    JAZZ=auto()
    ROCK=auto()
    HIP=auto()
    OLD=auto()

    @classmethod
    def set_genre(self: Enum) -> list:
        results: list = DataHandler.get_data()
        print(results)
        results[0] = []
        results[0].append(results)
        for i in self:
            choose: int = random.randrange(1, self[i])
            results[0].genre = self[choose].name #is string
            return results

class song:
    def format_song() -> list:
        for I in genre.set_genre():
            return [I[0]]