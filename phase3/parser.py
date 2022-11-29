import sys
from BranchRegister import BranchRegister, BranchPatterns

#prediction
miss_predict = 0

progress = 0

branch_register = BranchRegister()

with open(sys.argv[1]) as f:
	lines = f.readlines()
	for line in lines:
		progress+=1
		print("parsing in progress: " + str(round(progress/len(lines) * 100.0,2)) + " %")

		attributes = line.split(" ")
		
		is_taken = 0	
		is_taken_raw = attributes[1]
		if (is_taken_raw == "T"):
			#1 Denotes T
			is_taken = 1
		
		#Read the Branch Register and Check The Predicted Value
		prediction = branch_register.predict()

		#Compare the Actual Value Vs Predicted Value
		if (is_taken != prediction):
			miss_predict +=1

		#Update The Branch Register
		branch_register.update(is_taken)
		 

print("-------Parsing Complete-------")
print ("(5,1) Global Predictor Miss Rate: " + str(round( miss_predict/progress * 100.0,2)) + "%")
