import sys
sys.setrecursionlimit(2500)


from trie import empty_trie, insert, fetch

# ram
# ram_store(ram, address, value)
# ram_fetch(ram, address)

ram = empty_trie

def ram_store(ram, address, value):
	return insert(ram, address, value)

def ram_fetch(ram, address):
	return fetch(ram, address)

def core_dump(ram):
	def helper(ram):
		for i in range(1001):
			fetched_value = fetch(ram, i)
			if fetched_value is not None:
				print(f"[{i}]: {fetched_value}")

	print("-----------------------")
	helper(ram)
	print("-----------------------")

