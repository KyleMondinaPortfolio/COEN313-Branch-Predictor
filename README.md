#COEN 313 Branch Predictor
Final Class Project for Santa Clara University's COEN 313: Advance Computer Architecture Fall 202

##Phase 1

given a branch trace text file, program will output: 
	*number of branches taken
	*number of branches not taken
	*number of distinct branches

###Usage
`py parser.py <branchTrace.txt>`

###Branch Trace Format
1.) Address of branch instruction in Hexadecimal
2.) Taken (T) or not taken (N)
3.) Address of branch instruction target in Hexadecimal
4.) Instruction Name: String, not used in analysis at this moment

Example

48c30c T 48c1de JMP_REG


