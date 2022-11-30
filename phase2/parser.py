import sys
from bit1Predictor import Bit1Predictor
from bit2Predictor import Bit2Predictor
from bit3Predictor import Bit3Predictor
from hasher import hasher

if (len(sys.argv)<2):
    print("incorrect use of program, please supply a file to be parsed")
    print("example: ")
    print("py parser.py <branch_trace.txt>")
    exit()

progress = 0

BPP1 = {}
BPP2 = {}
BPP3 = {}

BP1 = {}
BP2 = {}
BP3 = {}


mpp1 = 0
mpp2 = 0
mpp3 = 0

mp1 = 0
mp2 = 0
mp3 = 0


with open(sys.argv[1]) as f:
    lines = f.readlines()
    for line in lines:
        progress = progress + 1
        print("parsing in progress: " + str(round(progress/len(lines) * 100.0,2)) + " %")

        attributes = line.split(" ")
        
        bi_addr = attributes[0]

        #check if branch address is in BP dictionary, if not added it and added a 1-bit predictor to it
        if bi_addr not in BPP1:
            BPP1[bi_addr]=Bit1Predictor()
        if bi_addr not in BPP2:
            BPP2[bi_addr]=Bit2Predictor()
        if bi_addr not in BPP3:
            BPP3[bi_addr]=Bit3Predictor()

        hashed_bi_addr = hasher(bi_addr)	

        if hashed_bi_addr not in BP1:
            BP1[hashed_bi_addr]=Bit1Predictor()
        if hashed_bi_addr not in BP2:
            BP2[hashed_bi_addr]=Bit2Predictor()
        if hashed_bi_addr not in BP3:
            BP3[hashed_bi_addr]=Bit3Predictor()


        is_taken = attributes[1]

        #counting misprediction
        if (BPP1[bi_addr].predict() != is_taken):
            mpp1 = mpp1 + 1
        if (BPP2[bi_addr].predict() != is_taken):
            mpp2 = mpp2 + 1
        if (BPP3[bi_addr].predict() != is_taken):
            mpp3 = mpp3 + 1

        if (BP1[hashed_bi_addr].predict() != is_taken):
            mp1 = mp1 + 1
        if (BP2[hashed_bi_addr].predict() != is_taken):
            mp2 = mp2 + 1
        if (BP3[hashed_bi_addr].predict() != is_taken):
            mp3 = mp3 + 1

        #updating taken and not taken
        if (is_taken == "T"):
            BPP1[bi_addr].taken()
            BPP2[bi_addr].taken()
            BPP3[bi_addr].taken()
            BP1[hashed_bi_addr].taken()
            BP2[hashed_bi_addr].taken()
            BP3[hashed_bi_addr].taken()
        elif (is_taken == "N"):
            BPP1[bi_addr].notTaken()
            BPP2[bi_addr].notTaken()
            BPP3[bi_addr].notTaken()
            BP1[hashed_bi_addr].notTaken()
            BP2[hashed_bi_addr].notTaken()
            BP3[hashed_bi_addr].notTaken()


print("-------Parsing Complete-------")
print ("1bit misprediction rate: " + str(round( mpp1/progress * 100.0,2)) + "%")
print ("2bit misprediction rate: " + str(round( mpp2/progress * 100.0,2)) + "%")
print ("3bit misprediction rate: " + str(round( mpp3/progress * 100.0,2)) + "%")
print ("1bit with 10-bit address misprediction rate: " + str(round( mp1/progress * 100.0,2)) + "%")
print ("2bit with 10-bit address misprediction rate: " + str(round( mp2/progress * 100.0,2)) + "%")
print ("3bit with 10-bit address misprediction rate: " + str(round( mp3/progress * 100.0,2)) + "%")