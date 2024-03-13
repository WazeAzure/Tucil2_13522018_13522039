from InputClass import InputClass
from MainAlgorithm import MainAlgorithm
from Draw import Draw
from Point import Point

class App:
    def __init__(self) -> None:
        self.input_handle = InputClass()
        self.algorithm = MainAlgorithm()
        self.draw = Draw()

        x_offset = -2
        y_offset = -3
        self.input_handle.point_list = [Point(0+x_offset, 0+y_offset), Point(-1+x_offset, 1+y_offset), Point(2+x_offset, 1+y_offset), Point(3+x_offset, 0+y_offset), Point(4+x_offset, 4+y_offset)]
        self.input_handle.iterate = 3

    def main(self):
        # self.input_handle.main()
        self.algorithm.init_variables_runtime(self.input_handle.point_list, self.input_handle.iterate)
        
        self.algorithm.main()
        
        self.draw.init_variables_runtime(self.algorithm.draw_list)
        
        self.draw.main()

if __name__ == "__main__":
    app = App()
    app.main()