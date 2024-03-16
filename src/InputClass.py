from typing import List, Optional, Union
from Point import Point
from colorama import Fore, Style, Back

class InputClass:
    def __init__(self) -> None:
        """
        Inisialisasi dari kelas InputClass sebagai handling input
        """
        self.n_titik: int = 0
        """
        Banyak titik input
        """
        self.point_list: list[Point] = []
        """
        Kumpulan Titik Koordinat
        struktur `list[Point]`
        """
        self.iterate: int = 0
        """
        Banyak iterasi sesuai masukan
        """
        self.magic_number: int = 20040406
        """
        Angka untuk stop looping
        """
        self.function_name: dict[str, function] = {
            "n": self.handle_input_n,
            "points": self.handle_input_points,
            "iterate": self.handle_input_iterate
        }

        self.error_code: dict[int, str] = {
            1: "Format Input Salah!. Mohon Masukkan Angka Saja",
            2: "Banyak Titik Minimal Tidak Boleh kurang dari 3.",
            3: "Program Terminated!",
            4: "Banyak input tidak sesuai banyak titik (n)",
            5: "Banyak Iterasi Minimal Tidak Boleh kurang dari 0.",
        }

    def main(self) -> None:
        """
        Fungsi utama menjalankan handle input n, points, iterate
        """
        self.handle_inputs("n")
        self.handle_inputs("points")
        self.handle_inputs("iterate")

    def handle_inputs(self, func_name: str) -> None:
        """
        Fungsi Template untuk menghandle masukan sesuai argumen func_name
        Args:
                `func_name: str`. Function name
        Rets:
                `int`. Kode Error
        """
        ret_val = None
        while(self.n_titik != self.magic_number and # break loop mechanism
              ret_val != 0): # input succeed

            ret_val = self.function_name[func_name]()
            
            # print error message
            if(ret_val != 0):
                self.error_message(ret_val)

        ret_val = -1
        self.end_program_mechanism() 

    def handle_input_n(self) -> int:
        """
        Input Handling untuk mendapatkan banyak titik

        Returns:
                `int: error message`
        """
        try:
            self.n_titik = int(input("Masukkan banyak titik contorol\nUntuk stop masukkan " + str(self.magic_number) + "\n> "))
            
            # minimum number is 3 to make a bezier curve
            if(self.n_titik < 3):
                return 2
            
            return 0
        except:
            # Wrong input format
            return 1
        
    
    def handle_input_points(self) -> int:
        """
        Input Handling untuk mendapatkan pasangan titik

        Returns:
                `int: error message`
        """
        point_str = input("Masukkan seluruh titik dengan urutan \"x1 y1 x2 y2 x3 y3 ...\" tanpa titik dua\nUntuk stop masukkan " + str(self.magic_number) + " \n> ")
        point_str = point_str.split(" ")
        point_str = [x for x in point_str if x]

        temp_arr = [0 for i in range(len(point_str))]
        
        # check break loop
        if(point_str[0] == "20040406"):
            self.n_titik = 20040406
            return 0

        # check point count
        if( len(point_str) != self.n_titik * 2):
            return 4
        
        # check all input type
        for i in range(len(point_str)):
            try:
                temp_arr[i] = float(point_str[i])
            except:
                return 1
        
        # insert to attribute
        self.point_list = [Point(temp_arr[i], temp_arr[i+1]) for i in range(0, len(temp_arr), 2)]

        return 0

    def handle_input_iterate(self) -> int:
        """
        Input Handling untuk mendapatkan maksimum iterasi

        Returns:
                `int: error message`
        """
        try:
            self.iterate = int(input("Masukkan banyak iterasi yang ingin dilakukan\nUntuk stop masukkan " + str(self.magic_number) + "\n> "))
            
            # minimum number is 0 to iterate
            if(self.iterate < 0):
                return 5
            
            return 0
        except:
            # Wrong input format
            return 1
            
    def error_message(self, code: int) -> None:
        """
        Prosedur untuk menampilkan pesan error.

        Args:
                `code: int`. error code
        """
        print(Fore.RED)
        message_len = len(self.error_code[code]) + 2
        print("+" + "-" * message_len + "+")
        print("| " + self.error_code[code] + " |")
        print("+" + "-" * message_len + "+")
        print(Style.RESET_ALL)
    
    def end_program_mechanism(self) -> None:
        """
        Prosedur menghentikan eksekusi program
        """
        if(self.n_titik == self.magic_number):
            self.error_message(3)
            exit(0)

if __name__ == "__main__":
    InputClass().main()


