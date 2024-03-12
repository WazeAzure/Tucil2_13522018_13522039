from InputClass import InputClass
from MainAlgorithm import MainAlgorithm
from Draw import Draw
from Point import Point

class App:
    def __init__(self) -> None:
        self.input_handle = InputClass()
        self.algorithm = MainAlgorithm()
        self.draw = Draw()

        self.input_handle.point_list = [Point(0, 0), Point(5, 0), Point(2, 3)]
        self.input_handle.iterate = 1

    def main(self):
        # self.input_handle.main()
        self.algorithm.init_variables_runtime(self.input_handle.point_list, self.input_handle.iterate)
        
        self.algorithm.main()
        
        self.draw.init_variables_runtime(self.algorithm.draw_list)
        
        self.draw.main()

if __name__ == "__main__":
    app = App()
    app.main()