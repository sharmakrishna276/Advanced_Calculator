from stack import Stack

class SimpleCalculator:
	def __init__(self):
		self.item=[]
		self.history=[]
		pass

	def evaluate_expression(self, input_expression):
		m=[]
		l=input_expression
		ans=""
		k=0
		for i in range(len(l)):
			if l[i]=="0" or l[i]=="1" or l[i]=="2" or l[i]=="3" or l[i]=="4" or l[i]=="5" or l[i]=="6" or l[i]=="7" or l[i]=="8" or l[i]=="9":
				ans+=l[i]
				k+=1
			else:
				if k!=0:
					m.append(float(ans))
					k=0
					ans=""
				m.append(l[i])
		if k!=0:
			m.append(float(ans))
		w=[]
		for i in range(len(m)):
			if m[i]!=" ":
				w.append(m[i])
		self.item=w
		if len(self.item)!=3:
			self.history.append((input_expression,"Error"))
			return "Error"
		else:
			a=self.item[0]
			b=self.item[1]
			c=self.item[2]
			try:
				a1=float(a)
			except:
				self.history.append((input_expression,"Error"))
				return "Error"
			try:
				c1=float(c)
			except:
				self.history.append((input_expression,"Error"))
				return "Error"
			if b=="*":
				self.history.append((input_expression,a1*c1))
				return a1*c1
			elif b=="+":
				self.history.append((input_expression,a1+c1))
				return a1+c1
			elif b=="-":
				self.history.append((input_expression,a1-c1))
				return a1-c1
			elif b=="/":
				if c1==0:
					self.history.append((input_expression,"Error"))
					return "Error"
				else:
					self.history.append((input_expression,a1/c1))
					return a1/c1
			else:
				self.history.append((input_expression,"Error"))
				return "Error"

	def get_history(self):
		return self.history[::-1]	