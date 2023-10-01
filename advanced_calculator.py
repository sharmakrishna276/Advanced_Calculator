from simple_calculator import SimpleCalculator
from stack import Stack

class AdvancedCalculator(SimpleCalculator):

	def __init__(self):
		super().__init__()
		self.newhistory=[]
		self.brackets=[]
		pass

	def evaluate_expression(self, input_expression):
		l=input_expression
		ans=""
		k=0
		m=[]
		for i in range(len(l)):
			if l[i]=="0" or l[i]=="1" or l[i]=="2" or l[i]=="3" or l[i]=="4" or l[i]=="5" or l[i]=="6" or l[i]=="7" or l[i]=="8" or l[i]=="9":
				ans+=l[i]
				k+=1
			else:
				if k!=0:
					m.append(int(ans))
					k=0
					ans=""
				if l[i]!=" ":
					m.append(l[i])
		if k!=0:
			m.append(int(ans))
		a=self.tokenize(input_expression)
		b=self.check_brackets(a)
		ans=self.evaluate_list_tokens(a)
		if a!=m or b==False:
			self().newhistory.append((input_expression,"Error"))
			return "Error"
		if type(ans)==str:
			self.newhistory.append((input_expression,"Error"))
			return "Error"
		self.newhistory.append((input_expression,(ans/1.0)))
		return (ans/1.0)

	def tokenize(self, input_expression):
		l=input_expression
		ans=""
		k=0
		m=[]
		for i in range(len(l)):
			if l[i]=="0" or l[i]=="1" or l[i]=="2" or l[i]=="3" or l[i]=="4" or l[i]=="5" or l[i]=="6" or l[i]=="7" or l[i]=="8" or l[i]=="9":
				ans+=l[i]
				k+=1
			else:
				if k!=0:
					m.append(int(ans))
					k=0
					ans=""
				m.append(l[i])
		if k!=0:
			m.append(int(ans))
		s=m
		w=[]
		for i in range(len(s)):
			if type(s[i])==int or s[i]=="+" or s[i]=="/" or s[i]=="*" or s[i]=="-" or s[i]=="(" or s[i]==")" or s[i]=="{" or s[i]=="}":
				w.append(s[i])
		return w		

	def check_brackets(self, list_tokens):
		x=list_tokens
		for i in range(len(x)):
			if x[i]=="{" or x[i]=="}" or x[i]=="(" or x[i]==")":
				self.brackets.append(x[i])
		b1open=0
		b2open=0
		ket=self.brackets
		if len(ket)%2!=0:
			return False
		i=0
		while i<len(ket):
			if (ket[i]=="(" and ket[i+1]=="{") or ((ket[i]=="(" and ket[i+1]=="}")):
				return False
			elif ket[i]=="(" and ket[i+1]=="(":
				b1open+=2
				i+=2
			elif ket[i]=="(" and ket[i+1]==")":
				i+=2
			elif ket[i]==")":
				if b1open>0:
					b1open-=1
					i+=1
				else:
					return False
			elif ket[i]=="}":
				if b2open>0:
					b2open-=1
					i+=1
				else:
					return False
			elif ket[i]=="{" and ket[i+1]=="{":
				b2open+=2
				i+=2
			elif ket[i]=="{" and ket[i+1]=="(":
				b1open+=1
				b2open+=1
				i+=2
			elif ket[i]=="{" and ket[i+1]==")":
				return False
			elif ket[i]=="{" and ket[i+1]=="}":
				i+=2
		if b1open==0 and b2open==0:
			return True
		return False

	def high_priority(op1, op2):
		operator=['/','*','+','-']
		if operator.index(op1)<operator.index(op2):
			return True
		return False

	def evaluate_list_tokens(self, list_tokens):
		Alisttokens=list_tokens
		try:
			def bracket_cheking(Alisttokens):
				if len(Alisttokens)==1:
					return Alisttokens[0]
				for i in range(len(Alisttokens)):
					if Alisttokens[i]=='/':
						temp=Alisttokens[i-1]/Alisttokens[i+1]
						Alisttokens.insert(i,temp)
						Alisttokens.pop(i+1)
						Alisttokens.pop(i+1)
						Alisttokens.pop(i-1)
						return bracket_cheking(Alisttokens)
				for i in range(len(Alisttokens)):
					if Alisttokens[i]=='*':
						temp=Alisttokens[i-1]*Alisttokens[i+1]
						Alisttokens.insert(i,temp)
						Alisttokens.pop(i+1)
						Alisttokens.pop(i+1)
						Alisttokens.pop(i-1)
						return bracket_cheking(Alisttokens[:i-1]+[temp]+Alisttokens[i+2:])
				for i in range(len(Alisttokens)):
						if Alisttokens[1]=='+':
							temp=Alisttokens[0]+Alisttokens[2]
							return bracket_cheking([temp]+Alisttokens[3:])
						else:
							temp=Alisttokens[0]-Alisttokens[2]
							return bracket_cheking([temp]+Alisttokens[3:])
			def evaluateexpression(Alisttokens):
				left=-1
				right=-1
				for i in range(len(Alisttokens)):
					if Alisttokens[i] in ["(","{"]:
						left=i
					elif Alisttokens[i] in [')','}']:
						right=i
						break
				if left==right:
					return bracket_cheking(Alisttokens)
				ans=bracket_cheking(Alisttokens[left+1:right])
				return evaluateexpression(Alisttokens[:left]+[ans]+Alisttokens[right+1:])
			return float(evaluateexpression(list_tokens))
		except:
			return "Error"

	def get_history(self):
		return self.newhistory