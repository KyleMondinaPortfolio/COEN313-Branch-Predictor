import sys
from hasher import hasher5, hasher10
from TournamentPredictor import TournamentPredictor

if (len(sys.argv)<2):
    print("incorrect use of program, please supply a file to be parsed")
    print("example: ")
    print("py parser.py <branch_trace.txt>")
    exit()

progress = 0

#dictionaries for full, 5-bit, and 10-bit branch addresses
full = {}
five = {}
ten = {}

#initializing misprediction counters
mp = 0
mp5 = 0
mp10 = 0


with open(sys.argv[1]) as f:
    lines = f.readlines()
    for line in lines:
        progress = progress + 1
        print("parsing in progress: " + str(round(progress/len(lines) * 100.0,2)) + " %")

        attributes = line.split(" ")
        bi_addr = attributes[0]

        #check if branch address is in dictionary; if not, add branch register to it
        if bi_addr not in full:
            full[bi_addr]=TournamentPredictor()
            
            hashed_bi_addr_5 = hasher5(bi_addr)	
            if hashed_bi_addr_5 not in five:
                five[hashed_bi_addr_5]=TournamentPredictor()

            hashed_bi_addr_10 = hasher10(bi_addr)	
            if hashed_bi_addr_10 not in ten:
                ten[hashed_bi_addr_10]=TournamentPredictor()
        
                
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

        if (five[hashed_bi_addr_5].predict() != is_taken):
            mp5 = mp5 + 1

        if (ten[hashed_bi_addr_10].predict() != is_taken):
            mp10 = mp10 + 1

        #Update The Branch Register
        full[bi_addr].update(is_taken)
        five[hashed_bi_addr_5].update(is_taken)
        ten[hashed_bi_addr_10].update(is_taken)


print("-------Parsing Complete-------")
print ("5-bit Addr Tourney Predictor Miss Rate: " + str(round(mp5/progress * 100.0,2)) + "%")
print ("10-bit Addr Tourney Predictor Miss Rate: " + str(round(mp10/progress * 100.0,2)) + "%")
print ("Full Addr Tourney Predictor Miss Rate: " + str(round(mp/progress * 100.0,2)) + "%")

        

