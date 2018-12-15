import sys
import msvcrt

class Tape:
    def __init__(self):
        self.tape = {}
        self.data_pointer = 0
        self.loops = [] # Stack

    def move_pointer(self, left=False, right=False):
        if left:
            self.data_pointer -= 1
        elif right:
            self.data_pointer += 1

    def get_value(self):
        sys.stdout.write(self.tape.get(self.data_pointer, "0"))

    def peek_value(self):
        return self.tape.get(self.data_pointer, "0")

    def change_value(self, diff=0):
        self.tape[self.data_pointer] = str(int(self.tape.get(self.data_pointer, 0)) + diff)
    
    def set_value(self):
        ch = msvcrt.getch()
        self.tape[self.data_pointer] = ch.decode("UTF-8")


        
