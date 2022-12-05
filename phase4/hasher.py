def hex2Bin(hex_value):
	int_value = int(hex_value, base=16)
	return str(bin(int_value))[2:]

def hasher5(bi_addr):
	#the bin value
	bv = hex2Bin(bi_addr)
	return bv[8] + bv[12] + bv[14] + bv[17] + bv[20]

def hasher10(bi_addr):
	#the bin value
	bv = hex2Bin(bi_addr)
	return bv[7] + bv[8] + bv[10] + bv[12] + bv[13] + bv[14] + bv[16] + bv[17] + bv[18] + bv[20]