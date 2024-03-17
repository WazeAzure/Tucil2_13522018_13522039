from InputClass import InputClass
from MainAlgorithm import MainAlgorithm
from Draw import Draw
from Point import Point
import time

class App:
    def __init__(self) -> None:
        """
        Inisiasi attribut kelas App
        """
        self.input_handle = InputClass()
        """
        Inisiasi untuk handling input
        """
        self.algorithm = MainAlgorithm()
        """
        Inisiasi untuk handling algoritma DnC
        """
        self.draw = Draw()
        """
        Inisiasi untuk handling draw dengan matplotlib
        """

        # VARIABLE UNTUK TESTING. Uncomment on testing TANPA nerima input.
        self.input_handle.point_list = [Point(-1, -2), Point(0, 1), Point(1, 1)]
        self.input_handle.iterate = 3

    def main(self):
        """
        Fungsi utama aplikasi App. Berisi pemanggilan input, algoritma, dan penggambaran
        """
        # Uncomment untuk testing DENGAN input
        # self.input_handle.main()
        self.algorithm.init_variables_runtime(self.input_handle.point_list, self.input_handle.iterate)
        

        print("========== Divide and Conquer")
        start_time = time.time() * 1000 # menghitung start time algoritma dnc
        self.algorithm.main()
        end_time = time.time() * 1000 # menghitung end time algoritma dnc

        print(f"Elapsed Time: {end_time - start_time} ms")
        print(self.algorithm.draw_list[-1])
        print(len(self.algorithm.draw_list[-1]))

        print()
        print("========== Bruteforce")
        start_time = time.time() * 1000 # menghitung start time algoritma bruteforce
        bruteforce_result = self.algorithm.brute_force(self.input_handle.point_list, self.input_handle.iterate)
        end_time = time.time() * 1000 # menghitung end time algoritma bruteforce

        print(f"Elapsed Time: {end_time - start_time} ms")
        print(bruteforce_result)
        print(len(bruteforce_result))

        # Inisiasilasi array untuk menggambar
        self.draw.init_variables_runtime(self.algorithm.draw_list)
        # fungsi menggambar Bezier Curve
        self.draw.main()

if __name__ == "__main__":
    app = App()
    app.main()