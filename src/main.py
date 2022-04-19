from enum import Enum
from inspect import _void
from gen import rdi

class Genre(Enum):
    # not hcded yet (pull from api later on)
    Pop = 1
    Rock = 2
    Hip_Hop = 3
    Indie = 4
    Jazz = 5

    @classmethod
    def get_genre(genre):
        for i in genre:
            if rdi.gen()[1] == i:
                return genre.name, genre.value



def main() -> _void:
    if rdi.gen()[0]: #isloadable?
        print(Genre.get_genre())

main()