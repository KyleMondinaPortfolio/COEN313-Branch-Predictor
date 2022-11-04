import sys
from collections import Counter
from instruction import Instruction

if (len(sys.argv)<2):
	print("incorrect use of program, please supply a file to be parsed")
	print("example: ")
	print("py parser.py <branch_trace.txt>")
	exit()


instructions = []
br_addrs = []
btaken = 0
bntaken = 0
progress = 0
totalBranches = 0

with open(sys.argv[1]) as f:
	lines = f.readlines()
	for line in lines:
		progress = progress + 1
		totalBranches = progress
		print("parsing in progress: " + str(round(progress/len(lines)*100.0,2)) + " %")

		attributes = line.split(" ")
		
		bi_addr = attributes[0]
		br_addrs.append(attributes[0])

		taken = attributes[1]
		if (taken == "T"):
			btaken = btaken + 1
		elif(taken=="N"):
			bntaken = bntaken + 1

		tbi_addr = attributes[2]
		instr_name = attributes[3]

		instructions.append(Instruction(attributes[0],attributes[1],attributes[2],attributes[3]))


distinct_br_addrs = Counter(br_addrs).keys()
print("-------Parsing Complete-------")
print("Total Branches: " + str(totalBranches))
print("Distinct Branch Addresses: " + str(len(distinct_br_addrs)))
print("Taken: " + str(btaken))
print("Not Taken: " + str(bntaken))
		

