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
        list_bezier_points = self.div_n_con(self.point_list, self.max_iter)

        # pemasukkan hasil titik kedalam list untuk digambar
        self.draw_list.append([self.point_list[0]] + list_bezier_points + [self.point_list[-1]])
    
    def get_post(self, point_a: Point, point_b: Point) -> Point:
        """
        Fungsi untuk mendapatkan titik t% dari point_a dan point_b.

        Args:
                `point_a: Point`. Koordinat Awal
                `point_b: point`. Koordinat Akhir
        Rets:
                `q_post: Point`. Titik tengah jika t = 0.5
        """
        q_post = (1-self.t) * point_a + self.t * point_b
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
        
        copy_list = list_points
        first = []
        last = []
        while(len(copy_list) != 1):
            temp = []
            for i in range(len(copy_list)-1):
                temp += [self.get_post(copy_list[i], copy_list[i+1])]
            
            self.draw_list.append(temp)
            first.append(temp[0])
            last.append(temp[-1])
            copy_list = temp
        
        last.reverse()

        """========================== DIVIDE =========================="""
        # go left
        left_branch = self.div_n_con([list_points[0], *first], iter - 1)

        # go right
        right_branch = self.div_n_con([*list(last), list_points[-1]], iter - 1)

        """========================== COMBINE =========================="""
        final_ans = left_branch + [copy_list[0]] + right_branch
        
        return final_ans
    
    def brute_force(self, list_points : list[Point], iter : int) -> list[Point]:
        
        # divide t by n * n
        t = 0
        step = 1 / (2 ** iter)

        n_titik = len(list_points)

        solution = []
        
        # main algorithm
        while(t < 1):
            new_point = Point(0, 0)
            for i in range(n_titik, 0, -1):
                konstanta = self.get_pascal_triangle(n_titik-1, n_titik-i)
                temp = konstanta * ((1-t)**(i-1)) * (t**(n_titik-i)) * list_points[n_titik-i]
                new_point = new_point + temp
            t += step
            solution.append(new_point)
        
        solution.append(list_points[-1]) # insert titik kontrol akhir
        return solution
    
    def get_pascal_triangle(self, n: int, r: int) -> int:
        res = 1
        for i in range(r):
            res = res * (n-i)
            res = res // (i+1)
        return res
    
if __name__ == "__main__":
    a = Point(2, 3)
    b = Point(5, 7)

    print(a + b)
    print(a * 2)
    print(2 * a)

    temp = [Point(-1, -2), Point(0, 1), Point(1, 1)]
    iter = 2
    ma = MainAlgorithm()
    ma.brute_force(temp, iter)