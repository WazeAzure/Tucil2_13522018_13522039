from typing import List, Optional, Union
from Point import Point

class MainAlgorithm:
    def __init__(self) -> None:
        self.max_iter: int = 0

        self.point_list: list[Point] = []
        
        self.draw_list: list[list[Point]] = []

        self.t = 0.5
    
    def init_variables_runtime(self, points: list[Point], iter: int) -> None:
        self.point_list = points
        self.max_iter = iter
    
    def main(self) -> None:
        self.draw_list.append(self.point_list) # draw the problem

        list_bezier_points = self.div_n_con(self.point_list, self.max_iter)

        self.draw_list.append([self.point_list[0], *list_bezier_points, self.point_list[2]])
    
    def get_post(self, point_a: Point, point_b: Point) -> Point:
        q_post = Point((1-self.t)*point_a.x + self.t*point_b.x,
                       (1-self.t)*point_a.y + self.t*point_b.y)
        return q_post

    def div_n_con(self, list_points: list[Point], iter: int):
        
        # the inside of list_points always consist of 3 points
        q_point1 = self.get_post(list_points[0], list_points[1])
        q_point2 = self.get_post(list_points[1], list_points[2])
        r_point = self.get_post(q_point1, q_point2) # new control point
        
        if iter == 1:
            return [r_point]


        iter -= 1

        # left branch
        ans_1 = self.div_n_con([list_points[0], q_point1, r_point], iter)

        # right branch
        ans_2 = self.div_n_con([r_point, q_point2, list_points[2]], iter)

        # self.draw_list.append([self.point_list[0], *ans_1, r_point, *ans_2, self.point_list[2]])

        return [*ans_1, r_point, *ans_2]