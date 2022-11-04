import sys
from instruction import Instruction

if (len(sys.argv)<2):
	print("incorrect use of program, please supply a file to be parsed")
	exit()


instructions = []
btaken = 0
bntaken = 0
counter = 0

with open(sys.argv[1]) as f:
	lines = f.readlines()
	for line in lines:
		counter = counter + 1	
		print("parsing progress: " + str(counter/15061011))
		attributes = line.split(" ")
		bi_addr = attributes[0]
		taken = attributes[1]
		tbi_addr = attributes[2]
		instr_name = attributes[3]
		instructions.append(Instruction(attributes[0],attributes[1],attributes[2],attributes[3]))

counter = 0

for instruction in instructions:
	counter=counter+1
	print("insturction classifcation progress" + str(counter/15061011))
	if (instruction.taken == "T"):
		btaken = btaken + 1
	elif(instruction.taken == "N"):
		bntaken = bntaken + 1

print("Taken: " + str(btaken))
print("Not Taken: " + str(bntaken))
		

