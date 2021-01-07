from cpu import run_and_dump, run_and_return

# program that echos inputs and halts when the input is 0

instructions = [
	3,  # [0]: IPA, first instruction is at address 3
	0,  # [1]: address to store input
	6,  # [2]: literal 6 how much to go back in later instruction
	1001000000,  # [1] <- read               | read input and store at address 1 **
	12000001000, # [0] <- [0] + 1 if [1]===0 | if the input is 0, skip 1 instruction 
	6000000000,  # [0] <- [0] + 1            | skip 1 instruction
	0000000000,  # halt                      | end of program
	2000001000,  # display <- [1]            | display [1] which is the input
	9000000002   # [0] = [0] - 6             | go back 6 instructions to **
]

run_and_return(instructions, 0, 0)