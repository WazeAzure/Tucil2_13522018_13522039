from typing import List, Optional, Union
from Point import Point
from collections import deque

class MainAlgorithm:
    def __init__(self) -> None:
        """
        Inisiasi seluruh atribut yang digunakan oleh MainAlgorithm
        """
        self.max_iter: int = 0
        """
        Maksimum iterasi yang dilakukan sesuai input
        """
        self.point_list: list[Point] = []
        """
        List berisi point yang akan diolah.

        struktur `list[Point]`
        """
        self.draw_list: list[list[Point]] = []
        """
        List titik yang disimpan untuk digambar oleh visualizer
        """
        self.t: float = 0.5
        """
        t merupakan persenan jarak antara titik awal dengan titik akhir

        `0 <= t <= 1`
        """
    
    def init_variables_runtime(self, points: list[Point], iter: int) -> None:
        """
        Inisiasi variable satu kali saja saat runtime. Point list dan max iter
        """
        self.point_list = points
        self.max_iter = iter
        
        self.draw_list.append(self.point_list) # draw the problem
    
    def main(self) -> None:
        """
        Fungsi utama untuk menjalankan algoritma Divide And Conquer
        """
        list_bezier_points = self.brute_force(self.point_list, self.max_iter)

        # pemasukkan hasil titik kedalam list untuk digambar
        self.draw_list.append([self.point_list[0], *list_bezier_points, self.point_list[len(self.point_list) - 1]])
    
    def get_post(self, point_a: Point, point_b: Point) -> Point:
        """
        Fungsi untuk mendapatkan titik t% dari point_a dan point_b.

        Args:
                `point_a: Point`. Koordinat Awal
                `point_b: point`. Koordinat Akhir
        Rets:
                `q_post: Point`. Titik tengah jika t = 0.5
        """
        q_post = Point((1-self.t)*point_a.x + self.t*point_b.x,
                       (1-self.t)*point_a.y + self.t*point_b.y)
        return q_post

    def div_n_con(self, list_points: list[Point], iter: int) -> list[Point]:
        """
        Algoritma Utama Divide dan Conquer

        Args:
                `list_points: list[Point]`. Kumpulan titik koordinat untuk dicari nilai tengahnya
                `iter: int`. Mencatat iterasi
        Rets:
                `final_ans: list[Point]`. Kumpulan titik r (titik kontrol) untuk dikembalikan.
        """
        

        """========================== CONQUER =========================="""

        if iter <= 0:
            return []
        
        copy_list = [x for x in list_points]
        first = []
        last = deque([])
        while(len(copy_list) != 1):
            temp = []
            for i in range(len(copy_list)-1):
                temp.append(self.get_post(copy_list[i], copy_list[i+1]))
            
            self.draw_list.append(temp)
            first.append(temp[0])
            last.appendleft(temp[-1])
            copy_list = temp
        
    
        
        # go left
        left_branch = self.div_n_con([list_points[0], *first], iter - 1)

        # go right
        right_branch = self.div_n_con([*list(last), list_points[-1]], iter - 1)

        final_ans = [*left_branch, copy_list[0], *right_branch]
        
        return final_ans
    
    def brute_force(self, list_points : list[Point], iter : int) -> list[Point]:
        iter *= iter
        if len(list_points) == 3:
            solution : list[Point] = []
            for i in range(1, iter+1):
                self.t = round(i/iter, 2)
                new_point : Point = Point(((1-self.t)**2)*list_points[0].x + (1-self.t)*self.t*list_points[1].x + (self.t**2)*list_points[2].x,
                                        ((1-self.t)**2)*list_points[0].y + (1-self.t)*self.t*list_points[1].y + (self.t**2)*list_points[2].y)
                solution.append(new_point)

            return solution
        else:
            print("Gabisa brow")
            return None