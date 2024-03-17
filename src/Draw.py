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
            "line": self.handle_draw_line_animate,
            "no-line": self.handle_draw_line
        }
        """
        Daftar nama fungsi yang available.
        
        Dapat di Extend sesuai kebutuhan
        """
        self.fig, self.axes = plt.subplots()
        """
        figure dan axes dari matplotlib
        """
        self.frame_tot: int = 0
        """
        total frame animasi
        """
        self.animation_data: list = []
        """
        Senarai untuk menyimpan data animasi garis
        """
        self.animation_dot_data: list = []
        """
        Senarai untuk menyimpan data animasi titik
        """
        self.layer_list: list[list[Point]] = []
        """
        Senarai berisi lapisan dari animasi
        """


    def init_variables_runtime(self, points: list[list[Point]]) -> None:
        """
        Inisiasi variable pertama kali saat run time
        """

        self.layer_list: list[list[Point]] = points

        x_points = []
        y_points = []

        for layer in self.layer_list:
            for points in layer:
                x_points.append(points.x)
                y_points.append(points.y)
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
        self.draw("line") # dengan animasi
        # self.draw("no-line") # tanpa animasi

        # animate
        self.anim_list[0] = animation.FuncAnimation(self.fig, self.update, interval=1, frames=self.frame_tot, repeat=False)
        self.anim_list[1] = animation.FuncAnimation(self.fig, self.update_dot, interval=1, frames=self.frame_tot, repeat=False)

        plt.show()

    def handle_draw_dot(self):
        for i, layer in enumerate(self.layer_list):
            x_dot_points = [p.x for p in layer]
            y_dot_points = [p.y for p in layer]

            if i == 0:
                temp, = self.axes.plot([], [], 'bo', alpha=0.5)
            elif i == len(self.layer_list)-1:
                temp, = self.axes.plot([], [], 'go', alpha=0.5)
            else:
                temp, = self.axes.plot([], [], 'co', alpha=0.5)
            
            self.animation_dot_data.append([x_dot_points, y_dot_points, temp, 1])

    def draw(self, func_name: str) -> None:
        """
        Fungsi Handle untuk penggamabran
        """
        self.function_name[func_name]()
    
    def handle_draw_line(self) -> None:
        """
        Fungsi untuk menggambar garis tanpa animasi
        """
        self.anim_list = [None for _ in range(len(self.layer_list))]
        # print(self.layer_list)
        for i, layer in enumerate(self.layer_list):
            self.x_points = [p.x for p in layer]
            self.y_points = [p.y for p in layer]

            if i == 0: # gambar soal
                self.axes.plot(self.x_points, self.y_points, '-bo')
            elif i == len(self.layer_list)-1: # gambar bezier curve akhir
                self.axes.plot(self.x_points, self.y_points, '-go')
            else: # gambar titik koordinat antara (proses pembentukan bezier curve)
                self.axes.plot(self.x_points, self.y_points, '--co', alpha=0.5)

    def handle_draw_line_animate(self) -> None:
        """
        Fungsi untuk menggambar Garis dengan titik koordinatnya. Dengan animasi
        """
        self.anim_list = [None for _ in range(len(self.layer_list))]
        # print(self.layer_list)
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
            self.frame_tot += len(x_data)
            self.animation_data.append([x_data, y_data, temp])
            

    def update(self, frame) -> None:
        """
        fungsi untuk memperbaharui axes plot garis sesuai dengan frame

        Args:
                `frame: int`. frame saat ini
        """
        # make boundary for interval
        boundary_list = [0]
        for i in range(len(self.animation_data)):
            boundary_list.append(boundary_list[i] + len(self.animation_data[i][0]))
        
        # look for which interval
        for i in range(len(boundary_list)):
            if (frame < boundary_list[i]):
                self.animation_data[i-1][2].set_data(self.animation_data[i-1][0][:(frame - boundary_list[i-1])], self.animation_data[i-1][1][:(frame - boundary_list[i-1])])
                return self.animation_data[i-1][2],
    
    def update_dot(self, frame) -> None:
        """
        fungsi untuk memperbaharui axes plot titik sesuai dengan frame

        Args:
                `frame: int`. frame saat ini
        """
        boundary_list = [0]
        for i in range(len(self.animation_data)):
            boundary_list.append(boundary_list[i] + len(self.animation_data[i][0]))
        
        for i in range(len(boundary_list)):
            if(frame < boundary_list[i]):
                end = self.animation_dot_data[i-1][3]
                self.animation_dot_data[i-1][2].set_data(self.animation_dot_data[i-1][0][:end], self.animation_dot_data[i-1][1][:end])
                self.animation_dot_data[i-1][3] = end + 1
                
                return self.animation_dot_data[i-1][2],