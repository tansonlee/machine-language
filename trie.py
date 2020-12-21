import sys
sys.setrecursionlimit(2500)


class Node:
	def __init__(self, value=False, key=None, left=None, right=None):
		self.left = left
		self.right = right
		self.value = value
		self.key = key

empty_trie = Node()

def insert(trie, num, key):
	if num == 0 and trie is None:
		return Node(True, key)
	elif num == 0 and trie is not None:
		value = True
		left = trie.left
		right = trie.right
		new_trie = Node(value, key, left, right)
		return new_trie
	elif trie is None:
		return insert(Node(), num, key)
	elif num % 2 == 0:
		# insert into left
		value = trie.value
		left = insert(trie.left, num / 2, key)
		right = trie.right
		return Node(value, trie.key, left, right)
	elif num % 2 == 1:
		# insert into right
		value = trie.value
		left = trie.left
		right = insert(trie.right, (num - 1) / 2, key)
		return Node(value, trie.key, left, right)

def remove(trie, num):
	if trie is None:
		return None
	elif num == 0:
		value = False
		key = None
		left = trie.left
		right = trie.right
		return Node(value, key, left, right)
	elif num % 2 == 0:
		# remove from left
		value = trie.value
		key = trie.key
		left = remove(trie.left, num / 2)
		right = trie.right
		return Node(value, key, left, right)
	elif num % 2 == 1:
		# remove from right
		value = trie.value
		key = trie.key
		left = trie.left
		right = remove(trie.right, (num - 1) / 2)
		return Node(value, key, left, right)

def fetch(trie, num):
	if trie is None:
		return None
	elif num == 0:
		return trie.key
	elif num % 2 == 0:
		# search left
		return fetch(trie.left, num / 2)
	elif num % 2 == 1:
		# search right
		return fetch(trie.right, (num - 1) / 2)
