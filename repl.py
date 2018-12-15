import sys
import tape

def scan_char(cmd, t):
    for ch in cmd:
        if ch == '>':
            t.move_pointer(right=True)
        elif ch == '<':
            t.move_pointer(left=True)
        elif ch == '+':
            t.change_value(diff=1)
        elif ch == '-':
            t.change_value(diff=-1)
        elif ch == '.':
            t.get_value()
        elif ch == ',':
            t.set_value()
        elif ch == '[':
            # Todo
            pass
        elif ch == ']':
            # Todo
            pass


def run():
    t = tape.Tape()
    print("REPL for BF interpreter.")
    while(True):
        cmd = input(">> ")
        scan_char(cmd, t)
