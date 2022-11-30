import sys
from hasher import hasher5
from FiveBitBranchRegister import FiveBitBranchRegister

if (len(sys.argv)<2):
    print("incorrect use of program, please supply a file to be parsed")
    print("example: ")
    print("py parser.py <branch_trace.txt>")
    exit()

progress = 0

#dictionaries for full and five-bit branch addresses
full = {}
five = {}

#initializing misprediction counters
mp = 0
mp5 = 0


with open(sys.argv[1]) as f:
    lines = f.readlines()
    for line in lines:
        progress = progress + 1
        print("parsing in progress: " + str(round(progress/len(lines) * 100.0,2)) + " %")

        attributes = line.split(" ")
        bi_addr = attributes[0]

        #check if branch address is in dictionary; if not, add branch register to it
        if bi_addr not in full:
            full[bi_addr]=FiveBitBranchRegister()
            
            hashed_bi_addr = hasher5(bi_addr)	
            if hashed_bi_addr not in five:
                five[hashed_bi_addr]=FiveBitBranchRegister()
        
                
        #Check if the Branch is Taken or Not
        #Then, convert to 0 or 1
        is_taken_raw = attributes[1]
        if (is_taken_raw == "T"):
            is_taken = 1
        elif (is_taken_raw == "N"):
            is_taken = 0


        #Count misprediction
        if (full[bi_addr].predict() != is_taken):
            mp = mp + 1

        if (five[hashed_bi_addr].predict() != is_taken):
            mp5 = mp5 + 1

        #Update The Branch Register
        full[bi_addr].update(is_taken)
        five[hashed_bi_addr].update(is_taken)


print("-------Parsing Complete-------")
print ("(5,1) Full Addr Local Predictor Miss Rate: " + str(round(mp/progress * 100.0,2)) + "%")
print ("(5,1) 5-bit Local Predictor Miss Rate: " + str(round(mp5/progress * 100.0,2)) + "%")
        

