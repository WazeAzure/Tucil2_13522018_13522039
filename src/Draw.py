import turtle
from Point import Point
import math

class Draw:
    def __init__(self) -> None:
        self.layer_list: list[list[Point]] = []
        self.magnifier: float = 100
        # turtle settings
        turtle.degrees(360)
        turtle.setx(0)
        turtle.sety(0)
        turtle.speed("fastest")
        
        # turtle.setup(width=500, height=500, startx=0, starty=0)

        self.function_name: dict[str, function] = {
            "dot": self.handle_draw_dot,
            "line": self.handle_draw_line
        }

    def init_variables_runtime(self, points: list[list[Point]]):
        self.layer_list: list[list[Point]] = points

    def main(self):
        self.draw("dot")
        self.draw("line")

        turtle.done()

    def get_direction(self, point_a: Point, point_b: Point) -> int:
        return math.atan2(point_b.x - point_a.x, point_b.y - point_a.y)

    def draw(self, func_name: str):
        turtle.showturtle()

        for layer in self.layer_list:
            for i in range(len(layer)-1):

                turtle.penup()

                # set startup location
                turtle.setpos((layer[i].x * self.magnifier, layer[i].y * self.magnifier))

                # function to call
                self.function_name[func_name]()

                # get direction
                direction = self.get_direction(layer[i], layer[i+1])
                turtle.setheading(direction)

                # go to destination
                turtle.goto((layer[i+1].x * self.magnifier, layer[i+1].y * self.magnifier))

            self.function_name[func_name]()
        turtle.hideturtle()
    
    def handle_draw_dot(self):
        turtle.dot(0.05 * self.magnifier, "black")
    
    def handle_draw_line(self):
        turtle.pendown()

