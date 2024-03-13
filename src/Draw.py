import matplotlib.pyplot as plt
from Point import Point
import math

class Draw:
    def __init__(self) -> None:
        self.layer_list: list[list[Point]] = []
        
        self.function_name: dict[str, function] = {
            "line": self.handle_draw_line
        }

    def init_variables_runtime(self, points: list[list[Point]]):
        self.layer_list: list[list[Point]] = points

    def main(self):
        self.draw("line")
        plt.show()

    def draw(self, func_name: str):
        self.function_name[func_name]()
        pass

    def handle_draw_line(self):
        for i, layer in enumerate(self.layer_list):
            x_points = [p.x for p in layer]
            y_points = [p.y for p in layer]

            if i == 0:
                plt.plot(x_points, y_points, '-bo')
            elif i == len(self.layer_list)-1:
                plt.plot(x_points, y_points, '-go')
            else:
                plt.plot(x_points, y_points, '--co')
