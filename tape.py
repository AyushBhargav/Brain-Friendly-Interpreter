import sys

class Tape:
    def __init__(self):
        self.tape = {}
        self.data_pointer = 0
        self.loop_index = [] # Stack

    def move_pointer(self, left=False, right=False):
        if left:
            self.data_pointer -= 1
        elif right:
            self.data_pointer += 1

    def get_value(self):
        sys.stdout.write(str(self.tape.get(self.data_pointer, 0)))

    def change_value(self, diff=0):
        self.tape[self.data_pointer] = self.tape.get(self.data_pointer, 0) + diff
    
    def set_value(self):
        ch = sys.stdin.read(1)
        self.tape[self.data_pointer] = ch


        
