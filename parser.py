import sys
from collections import Counter
from instruction import Instruction

if (len(sys.argv)<2):
	print("incorrect use of program, please supply a file to be parsed")
	exit()


instructions = []
br_addrs = []
btaken = 0
bntaken = 0
counter = 0

with open(sys.argv[1]) as f:
	lines = f.readlines()
	for line in lines:
		counter = counter + 1	
		print("parsing progress: " + str(counter))
		attributes = line.split(" ")
		bi_addr = attributes[0]
		taken = attributes[1]
		if (taken == "T"):
			btaken = btaken + 1
		elif(taken=="N"):
			bntaken = bntaken + 1
		tbi_addr = attributes[2]
		instr_name = attributes[3]
		instructions.append(Instruction(attributes[0],attributes[1],attributes[2],attributes[3]))
		br_addrs.append(attributes[0])
	


distinct_br_addrs = Counter(br_addrs).keys()
print("Distinct Branch Addresses " + str(len(distinct_br_addrs)))
print("Taken: " + str(btaken))
print("Not Taken: " + str(bntaken))
		

