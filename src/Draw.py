import matplotlib.pyplot as plt
from Point import Point
import math

class Draw:
    def __init__(self) -> None:
        """
        Inisialisasi variable atribut draw
        """
        self.layer_list: list[list[Point]] = []
        """
        List berisi iterasi dari setiap point untuk penggambaran

        struktur `list[list[Point]]`
        """
        self.function_name: dict[str, function] = {
            "line": self.handle_draw_line
        }
        """
        Daftar nama fungsi yang available.
        
        Dapat di Extend sesuai kebutuhan
        """

    def init_variables_runtime(self, points: list[list[Point]]) -> None:
        """
        Inisiasi variable pertama kali saat run time
        """
        self.layer_list: list[list[Point]] = points

    def main(self) -> None:
        """
        Fungsi utama untuk menjalankan penggambaran
        """
        self.draw("line")
        plt.show()

    def draw(self, func_name: str) -> None:
        """
        Fungsi Handle untuk penggamabran
        """
        self.function_name[func_name]()

    def handle_draw_line(self) -> None:
        """
        Fungsi untuk menggambar Garis dengan titik koordinatnya.
        """
        for i, layer in enumerate(self.layer_list):
            x_points = [p.x for p in layer]
            y_points = [p.y for p in layer]

            if i == 0: # gambar soal
                plt.plot(x_points, y_points, '-bo')
            elif i == len(self.layer_list)-1: # gambar bezier curve akhir
                plt.plot(x_points, y_points, '-go')
            else: # gambar titik koordinat antara (proses pembentukan bezier curve)
                plt.plot(x_points, y_points, '--co', alpha=0.5)
