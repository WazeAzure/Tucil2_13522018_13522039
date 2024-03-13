from typing import List, Optional, Union
from Point import Point

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
        
        # initiate all q points place
        q_points = [Point(0, 0) for i in range(len(list_points) - 1)]
        # initiate all r points place
        r_points = [0 for i in range(len(list_points) - 2)]
        
        # initiate q_points
        for i in range(len(list_points) - 1):
            q_points[i] = self.get_post(list_points[i], list_points[i+1])
        
        # initiate r points
        for i in range(len(q_points)-1): 
            # the inside of list_points always consist of 3 points
            r_points[i] = self.get_post(q_points[i], q_points[i+1]) # new control point
        
        # draw all q points
        self.draw_list.append(q_points)

        if iter == 1:
            return r_points
        elif iter < 1:
            return []

        # decrement iteration
        iter -= 1

        """========================== DIVIDE =========================="""

        # init all branches
        r_all_branches = []
        
        # start from first
        ans_1 = self.div_n_con([list_points[0], q_points[0], r_points[0]], iter)
        # append first region result to draw
        r_all_branches.append(ans_1)
        # between
        for i in range(0, len(r_points)-1):
            ans_2 = self.div_n_con([r_points[i], q_points[i+1], r_points[i+1]], iter)
            # append between region result to draw
            r_all_branches.append(ans_2)
        # last
        ans_2 = self.div_n_con([r_points[len(r_points)-1], q_points[len(q_points)-1], list_points[len(list_points)-1]], iter)
        # append last region result to draw
        r_all_branches.append(ans_2)

        """========================== MERGE =========================="""

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