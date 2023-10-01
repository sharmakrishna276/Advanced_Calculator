class Stack:
	def __init__(self):
		self.items=[]
		pass
	
	def push(self, item):
		self.items.append(item)
		pass

	def peek(self):
		if len(self.items)==0:
			return "Error"
		else:
			return self.items[-1]
		pass

	def pop(self):
		if self.peek()!="Error":
			self.items.pop()
		pass

	def is_empty(self):
		if len(self.items)==0:
			return True
		return False
		pass

	def __str__(self):
		ans=""
		for i in range(len(self.items)-1,-1,-1):
			ans=ans+str(self.items[i])+" "
		return ans[:len(ans)-1]
		pass

	def __len__(self):
		return len(self.items)
		pass