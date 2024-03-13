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
        
        self.draw_list.append(self.point_list) # draw the problem
    
    def main(self) -> None:

        list_bezier_points = self.div_n_con(self.point_list, self.max_iter)

        self.draw_list.append([self.point_list[0], *list_bezier_points, self.point_list[len(self.point_list) - 1]])
    
    def get_post(self, point_a: Point, point_b: Point) -> Point:
        q_post = Point((1-self.t)*point_a.x + self.t*point_b.x,
                       (1-self.t)*point_a.y + self.t*point_b.y)
        return q_post

    def div_n_con(self, list_points: list[Point], iter: int):
        
        q_points = [Point(0, 0) for i in range(len(list_points) - 1)]

        r_points = [0 for i in range(len(list_points) - 2)]
        
        # initiate q_points
        for i in range(len(list_points) - 1):
            q_points[i] = self.get_post(list_points[i], list_points[i+1])
        
        # initiate r points
        for i in range(len(q_points)-1): 
            # the inside of list_points always consist of 3 points
            r_points[i] = self.get_post(q_points[i], q_points[i+1]) # new control point
        
        self.draw_list.append(q_points)

        if iter == 1:
            return r_points
        elif iter < 1:
            return []

        iter -= 1

        # all branches

        r_all_branches = []
        
        # start from first
        ans_1 = self.div_n_con([list_points[0], q_points[0], r_points[0]], iter)
        r_all_branches.append(ans_1)
        # between
        for i in range(0, len(r_points)-1):
            ans_2 = self.div_n_con([r_points[i], q_points[i+1], r_points[i+1]], iter)
            r_all_branches.append(ans_2)
        # last
        ans_2 = self.div_n_con([r_points[len(r_points)-1], q_points[len(q_points)-1], list_points[len(list_points)-1]], iter)
        r_all_branches.append(ans_2)

        # self.draw_list.append([self.point_list[0], *ans_1, r_point, *ans_2, self.point_list[2]])

        final_ans = []
        # suusn semua
        i = 0
        j = 0
        while(i < len(r_all_branches) and j < len(r_points)):
            for x in r_all_branches[i]:
                final_ans.append(x)
            final_ans.append(r_points[j])
            i += 1
            j += 1
        for x in r_all_branches[i]:
            final_ans.append(x)

        return final_ans