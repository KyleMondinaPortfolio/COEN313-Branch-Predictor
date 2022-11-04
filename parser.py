import sys
from instruction import Instruction

if (len(sys.argv)<2):
	print("incorrect use of program, please supply a file to be parsed")
	exit()


instructions = []
btaken = 0

with open(sys.argv[1]) as f:
	lines = f.readlines()
	for line in lines:
		attributes = line.split(" ")
		bi_addr = attributes[0]
		taken = attributes[1]
		tbi_addr = attributes[2]
		instr_name = attributes[3]
		instructions.append(Instruction(attributes[0],attributes[1],attributes[2],attributes[3]))

for instruction in instructions:
	print(instruction.taken)
	if (instruction.taken == "T"):
		btaken = btaken + 1

print(btaken)

		

