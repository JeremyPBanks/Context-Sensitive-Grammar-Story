class wordQueue:
	def __init__(self):
		self.paragraph = []

    	def enqueue(self, node):
        	self.paragraph.append(node)

    	def dequeue(self):
        	return self.paragraph.pop(0)

	def isEmpty(self):
	        if self.paragraph == []:
			return True
		else:
			return False
