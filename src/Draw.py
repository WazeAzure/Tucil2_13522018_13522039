import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Point import Point
import math
import numpy as np

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
            "dot": self.handle_draw_dot,
            "line": self.handle_draw_line
        }
        """
        Daftar nama fungsi yang available.
        
        Dapat di Extend sesuai kebutuhan
        """
        self.fig, self.axes = plt.subplots()

    def init_variables_runtime(self, points: list[list[Point]]) -> None:
        """
        Inisiasi variable pertama kali saat run time
        """
        self.layer_list: list[list[Point]] = points

        x_points = []
        y_points = []

        for x in self.layer_list:
            for y in x:
                x_points.append(y.x)
                y_points.append(y.y)
        max_width = max(x_points) + 2
        min_width = min(x_points) - 2
        max_height = max(y_points) + 2
        min_height = min(y_points) - 2

        self.axes.set_xlim([min_width, max_width])
        self.axes.set_ylim([min_height, max_height])

    def main(self) -> None:
        """
        Fungsi utama untuk menjalankan penggambaran
        """
        self.draw("dot")
        self.draw("line")

        # animate
        # previous_ani = None
        # for animation_data in self.anim_list:
        #     ani = animation_data
        #     if previous_ani is not None:
        #         ani._start_func = previous_ani._end_func  # Chain the animations
        # previous_ani = ani

        plt.show()

    def handle_draw_dot(self):
        for i, layer in enumerate(self.layer_list):
            for point in layer:
                if i == 0:
                    self.axes.plot(point.x, point.y, 'bo')
                elif i == len(self.layer_list)-1:
                    self.axes.plot(point.x, point.y, 'go')
                else:
                    self.axes.plot(point.x, point.y, 'co')

    def draw(self, func_name: str) -> None:
        """
        Fungsi Handle untuk penggamabran
        """
        self.function_name[func_name]()

    def handle_draw_line(self) -> None:
        """
        Fungsi untuk menggambar Garis dengan titik koordinatnya.
        """
        self.anim_list = [None for _ in range(len(self.layer_list))]
        print(self.layer_list)
        for i, layer in enumerate(self.layer_list):
            self.x_points = [p.x for p in layer]
            self.y_points = [p.y for p in layer]

            if i == 0: # gambar soal
                temp, = self.axes.plot([], [], '-b')
            elif i == len(self.layer_list)-1: # gambar bezier curve akhir
                temp, = self.axes.plot([], [], '-g')
            else: # gambar titik koordinat antara (proses pembentukan bezier curve)
                temp, = self.axes.plot([], [], '--c', alpha=0.5)

            # if i == 0:
            x_data = np.array([])
            y_data = np.array([])
            for j in range(len(self.x_points) -1):
                x_data = np.append(x_data, np.linspace(self.x_points[j], self.x_points[j+1], 10))
                y_data = np.append(y_data, np.linspace(self.y_points[j], self.y_points[j+1], 10))
            x_data = np.append(x_data, self.x_points[-1])
            y_data = np.append(y_data, self.y_points[-1])
            
            # if i==0:
            self.anim_list[i] = animation.FuncAnimation(self.fig, self.update, interval=1, frames=len(x_data), repeat=False, fargs=(x_data, y_data, temp))

    def update(self, frame, x_data, y_data, temp):
        temp.set_data(x_data[:frame], y_data[:frame])
        return temp,