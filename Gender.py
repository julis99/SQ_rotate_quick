from enum import Enum


class Gender(Enum):
    BOY = "b"
    GIRL = "g"
    BOTH = "b/g"

    def __str__(self):
        return self.value