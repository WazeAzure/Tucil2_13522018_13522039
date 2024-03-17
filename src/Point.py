from dataclasses import dataclass
import typing

@dataclass
class Point:
    """
    Kelas point. Memiliki atribut x dan y
    - `x: float`
    - `y: float`
    """
    x: float
    y: float

    def __add__(self, p2):
        return Point(self.x + p2.x, self.y + p2.y)

    def __mul__(self, constant):
        return Point(self.x * constant, self.y * constant)
    
    def __rmul__(self, constant):
        return Point(self.x * constant, self.y * constant)