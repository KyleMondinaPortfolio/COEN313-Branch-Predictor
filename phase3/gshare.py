import sys
from bit1Predictor import Bit1Predictor
from hasher import hasher10

class TenBitShiftRegister:
    def __init__(self):
       self.queue = [0,0,0,0,0,0,0,0,0,0]
    def update(self,actual_value):
       self.queue.pop()
       self.queue.insert(0,actual_value)
    def get_pattern(self):
       s = ''.join(str(bit) for bit in self.queue)
       return s


if (len(sys.argv)<2):
    print("incorrect use of program, please supply a file to be parsed")
    print("example: ")
    print("py parser.py <branch_trace.txt>")
    exit()

progress = 0

#dictionary for XOR values
xor_dict = {}

#initializing misprediction counter
mp = 0

shift_register = TenBitShiftRegister()

with open(sys.argv[1]) as f:
    lines = f.readlines()
    for line in lines:
        progress = progress + 1
        print("parsing in progress: " + str(round(progress/len(lines) * 100.0,2)) + " %")

        attributes = line.split(" ")
        addr = hasher10(attributes[0]) #setting addr to 10-bit hashed address

        #XOR address with shift register value here:
        xor = ""
        for i in range(0, 10):
            xor += str(int(shift_register.get_pattern()[i]) ^ int(addr[i]))

        #check if XOR value is in dictionary; if not, add 1-bit predictor to it
        if xor not in xor_dict:
            xor_dict[xor] = Bit1Predictor()
                       
        #Check if the Branch is Taken or Not
        is_taken = attributes[1]

        #Count misprediction
        if (xor_dict[xor].predict() != is_taken):
            mp = mp + 1

        #Update The Predictor and Shift Register
        if (is_taken == "T"):
            xor_dict[xor].taken()
            shift_register.update(1)
        elif (is_taken == "N"):
            xor_dict[xor].notTaken()
            shift_register.update(0)
        

print("-------Parsing Complete-------")
print("Gshare (10-bit shift register and 10-bit of address) Miss Rate: " + str(round(mp/progress * 100.0,2)) + "%")
print("Amount of dictionary keys: " + str(len(xor_dict)))