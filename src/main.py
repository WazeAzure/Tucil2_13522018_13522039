from InputClass import InputClass
from MainAlgorithm import MainAlgorithm
from Draw import Draw
from Point import Point
from colorama import Fore, Style, Back
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

    def main(self):
        """
        Fungsi utama aplikasi App. Berisi pemanggilan input, algoritma, dan penggambaran
        """
        self.input_handle.main()
        self.algorithm.init_variables_runtime(self.input_handle.point_list, self.input_handle.iterate)
        
        print(Fore.YELLOW)
        print("========== Divide and Conquer")
        print(Style.RESET_ALL)
        start_time = time.perf_counter() * 1000 # menghitung start time algoritma dnc
        self.algorithm.main()
        end_time = time.perf_counter() * 1000 # menghitung end time algoritma dnc

        print(Fore.GREEN)
        print(f"Elapsed Time: {end_time - start_time} ms")
        print(Style.RESET_ALL)
        print(self.algorithm.draw_list[-1])
        print(len(self.algorithm.draw_list[-1]))

        print(Fore.YELLOW)
        print("========== Bruteforce")
        print(Style.RESET_ALL)
        start_time = time.perf_counter() * 1000 # menghitung start time algoritma bruteforce
        bruteforce_result = self.algorithm.brute_force(self.input_handle.point_list, self.input_handle.iterate)
        end_time = time.perf_counter() * 1000 # menghitung end time algoritma bruteforce

        print(Fore.GREEN)
        print(f"Elapsed Time: {end_time - start_time} ms")
        print(Style.RESET_ALL)
        print(bruteforce_result)
        print(len(bruteforce_result))

        # Inisiasilasi array untuk menggambar
        self.draw.init_variables_runtime(self.algorithm.draw_list)
        
        # fungsi menggambar Bezier Curve
        self.draw.main()

if __name__ == "__main__":
    app = App()
    app.main()