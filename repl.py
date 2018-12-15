import sys
import tape

def scan_char(cmd, t):
    index = 0
    while index < len(cmd):
        ch = cmd[index]
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
            n_index = cmd.find(']', index+1)
            if n_index == -1:
                print("Loop unclosed.")
                return
            if t.peek_value() == "0":
                # Skip loop
                index = n_index
        elif ch == ']':
            p_index =  cmd.find('[', 0, index-1)
            if p_index == -1:
                print("Loop unclosed.")
                return
            if t.peek_value() != "0":
                # Skip loop
                index = p_index
        index += 1


def run():
    t = tape.Tape()
    print("REPL for BF interpreter. Enter 'exit' to close shell.")
    while(True):
        cmd = input(">> ")
        if cmd == 'exit':
            print("Shell aborted.")
            return
        scan_char(cmd, t)
        print() # Newline
