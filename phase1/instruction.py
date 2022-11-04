class Instruction:
	def __init__(self, bi_addr, taken, tbi_addr, instr_name):
		self.bi_addr = bi_addr
		self.taken = taken
		self.tbi_addr = tbi_addr
		self.instr_name = instr_name
		
