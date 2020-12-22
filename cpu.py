import sys
sys.setrecursionlimit(2500)

from ram import ram, ram_fetch, ram_store, core_dump

# XXtttuuuvvv : name ================| description
# 00000000000 : halt ================| end program
# 01ttt000000 : read ================| [ttt] <- read
# 02000uuu000 : display =============| display <- [uuu]
# 03tttuuu000 : copy ================| [ttt] <- [uuu]
# 04tttuuu000 : fetch ===============| [ttt] <- [[uuu]]
# 05tttuuu000 : store ===============| [[ttt]] <- [uuu]
# 06ttt000000 : add1 ================| [ttt] <- [ttt] + 1
# 07tttuuuvvv : add =================| [ttt] <- [uuu] + [vvv]
# 08ttt000000 : subtract1 ===========| [ttt] <- max([ttt] - 1, 0)
# 09tttuuuvvv : subtract ============| [ttt] <- max([uuu] - [vvv], 0)
# 10tttuuuvvv : multiply ============| [ttt] <- [uuu] * [vvv]
# 11tttuuuvvv : divide ==============| [ttt] <- floor([uuu] / [vvv]) if [vvv] != 0
# 12tttuuu000 : if zero add1 ========| [ttt] <- [ttt] + 1 if [uuu] === 0
# 13tttuuuvvv : if equal add1 =======| [ttt] <- [ttt] + 1 if [uuu] === [vvv]
# 14tttuuuvvv : if greater add1 =====| [ttt] <- [ttt] + 1 if [uuu] > [vvv]

# add1 : [ttt] = [ttt] + 1
def add1(ram, target_address):
	target_value = ram_fetch(ram, target_address)
	new_ram = ram_store(ram, target_address, target_value + 1)
	return new_ram

# add : [ttt] = [uuu] + [vvv]
def add(ram, target_address, source_address_1, source_address_2):
	source_value_1 = ram_fetch(ram, source_address_1)
	source_value_2 = ram_fetch(ram, source_address_2)
	new_ram = ram_store(ram, target_address, source_value_1 + source_value_2)
	return new_ram

# sub1 : [ttt] = max([ttt] - 1, 0)
def sub1(ram, target_address):
	target_value = ram_fetch(ram, target_address)
	subtraction = target_value - 1
	if subtraction < 0:
		new_ram = ram_store(ram, target_address, 0)
		return new_ram
	else:
		new_ram = ram_store(ram, target_address, subtraction)
		return new_ram

# sub : [ttt] = max([uuu] - [vvv], 0)
def sub(ram, target_address, source_address_1, source_address_2):
	source_value_1 = ram_fetch(ram, source_address_1)
	source_value_2 = ram_fetch(ram, source_address_2)
	subtraction = source_value_1 - source_value_2
	if subtraction < 0:
		new_ram = ram_store(ram, target_address, 0)
		return new_ram
	else:
		new_ram = ram_store(ram, target_address, subtraction)
		return new_ram

# mult : [ttt] = [uuu] * [vvv]
def mult(ram, target_address, source_address_1, source_address_2):
	source_value_1 = ram_fetch(ram, source_address_1)
	source_value_2 = ram_fetch(ram, source_address_2)
	new_ram = ram_store(ram, target_address, source_value_1 * source_value_2)
	return new_ram

# div : [ttt] = floor([uuu] / [vvv]) if [vvv] != 0, else, ERROR
def div(ram, target_address, source_address_1, source_address_2):
	source_value_1 = ram_fetch(ram, source_address_1)
	source_value_2 = ram_fetch(ram, source_address_2)
	if source_value_2 == 0:
		return "DIVISION BY 0"
	division = source_value_1 // source_value_2
	new_ram = ram_store(ram, target_address, division)
	return new_ram

# copy : [ttt] = [uuu]
def copy(ram, target_address, source_address):
	source_value = ram_fetch(ram, source_address)
	new_ram = ram_store(ram, target_address, source_value)
	return new_ram

# fetch : [ttt] = [[uuu]]
def fetch(ram, target_address, source_pointer_address):
	source_address = ram_fetch(ram, source_pointer_address)
	return copy(ram, target_address, source_address)

# store [[ttt]] = [uuu]
def store(ram, target_pointer_address, source_address):
	target_address = ram_fetch(ram, target_pointer_address)
	return copy(ram, target_address, source_address)

# if_zero_add1 : [ttt] = [ttt] + 1 if [uuu] === 0
def if_zero_add1(ram, target_address, source_address):
	source_value = ram_fetch(ram, source_address)	
	if source_value == 0:
		target_value = ram_fetch(ram, target_address)
		new_ram = ram_store(ram, target_address, target_value + 1)
		return new_ram
	else:
		return ram

# if_equal_add1 : [ttt] = [ttt] + 1 if [uuu] === [vvv]
def if_equal_add1(ram, target_address, source_address_1, source_address_2):
	source_value_1 = ram_fetch(ram, source_address_1)
	source_value_2 = ram_fetch(ram, source_address_2)
	if source_value_1 == source_value_2:
		target_value = ram_fetch(ram, target_address)
		new_ram = ram_store(ram, target_address, target_value + 1)
		return new_ram
	else:
		return ram

# if_greater_add1 : [ttt] = [ttt] + 1 if [uuu] > [vvv]
def if_greater_add1(ram, target_address, source_address_1, source_address_2):
	source_value_1 = ram_fetch(ram, source_address_1)
	source_value_2 = ram_fetch(ram, source_address_2)
	if source_value_1 > source_value_2:
		target_value = ram_fetch(ram, target_address)
		new_ram = ram_store(ram, target_address, target_value + 1)
		return new_ram
	else:
		return ram

# display : output [uuu]
def display(ram, source_address):
	source_value = ram_fetch(ram, source_address)
	print("< " + str(source_value))
	return ram

# read : [ttt] = input
def read(ram, target_address):
	user_input = int(input("> "))
	new_ram = ram_store(ram, target_address, user_input)
	return new_ram

# load list of instructions into ram
def ram_load(ram, load_address, lst):
	if len(lst) == 0:
		return ram
	else:
		next_ram = ram_store(ram, load_address, lst[0])
		next_load_address = load_address + 1
		next_lst = lst.copy()
		next_lst.pop(0)
		return ram_load(next_ram, next_load_address, next_lst)

# XXtttuuuvvv
def extract_instructions(instruction):
	operation_code = instruction // 1000000000
	target_address = (instruction // 1000000) % 1000
	source_address_1 = (instruction // 1000) % 1000
	source_adderss_2 = instruction % 1000
	return [operation_code, target_address, source_address_1, source_adderss_2]

# cpu fetch-eval cycle
def cpu(ram, IPA):
	def cycle(ram):
		instruction_pointer = ram_fetch(ram, IPA)
		instruction = ram_fetch(ram, instruction_pointer)
		extracted_instructions = extract_instructions(instruction)

		# XXtttuuuvvv
		# XX
		operation_code = extracted_instructions[0]
		# ttt
		target_address = extracted_instructions[1]
		# uuu
		source_address_1 = extracted_instructions[2]
		# vvv
		source_address_2 = extracted_instructions[3]

		next_ram = add1(ram, IPA)

		# 0  : halt ================| end program
		if operation_code == 0:
			return next_ram
		# 1  : read ================| [ttt] <- read
		elif operation_code == 1:
			return cycle(read(next_ram, target_address))
		# 2  : display =============| display <- [uuu]
		elif operation_code == 2:
			return cycle(display(next_ram, source_address_1))
		# 3  : copy ================| [ttt] <- [uuu]
		elif operation_code == 3:
			return cycle(copy(next_ram, target_address, source_address_1))
		# 4  : fetch ===============| [ttt] <- [[uuu]]
		elif operation_code == 4:
			return cycle(fetch(next_ram, target_address, source_address_1))
		# 5  : store ===============| [[ttt]] <- [uuu]
		elif operation_code == 5:
			return cycle(store(next_ram, target_address, source_address_1))
		# 6  : add1 ================| [ttt] <- [ttt] + 1
		elif operation_code == 6:
			return cycle(add1(next_ram, target_address))
		# 7  : add =================| [ttt] <- [uuu] + [vvv]
		elif operation_code == 7:
			return cycle(add(next_ram, target_address, source_address_1, source_address_2))
		# 8  : subtract1 ===========| [ttt] <- max([ttt] - 1, 0)
		elif operation_code == 8:
			return cycle(sub1(next_ram, target_address))
		# 9  : subtract ============| [ttt] <- max([uuu] - [vvv], 0)
		elif operation_code == 9:
			return cycle(sub(next_ram, target_address, source_address_1, source_address_2))
		# 10 : multiply ============| [ttt] <- [uuu] * [vvv]
		elif operation_code == 10:
			return cycle(mult(next_ram, target_address, source_address_1, source_address_2))
		# 11 : divide ==============| [ttt] <- floor([uuu] / [vvv]) if [vvv] != 0
		elif operation_code == 11:
			return cycle(div(next_ram, target_address, source_address_1, source_address_2))
		# 12 : if zero add1 ========| [ttt] <- [ttt] + 1 if [uuu] === 0
		elif operation_code == 12:
			return cycle(if_zero_add1(next_ram, target_address, source_address_1))
		# 13 : if equal add1 =======| [ttt] <- [ttt] + 1 if [uuu] === [vvv]
		elif operation_code == 13:
			return cycle(if_equal_add1(next_ram, target_address, source_address_1, source_address_2))
		# 14 : if greater add1 =====| [ttt] <- [ttt] + 1 if [uuu] > [vvv]
		elif operation_code == 14:
			return cycle(if_greater_add1(next_ram, target_address, source_address_1, source_address_2))
		
	return cycle(ram)
		
def run_and_return(instructions, load_address, instruction_pointer_address):
	return cpu(ram_load(ram, load_address, instructions), instruction_pointer_address)

def run_and_dump(instructions, load_address, instruction_pointer_address):
	core_dump(cpu(ram_load(ram, load_address, instructions), instruction_pointer_address))




