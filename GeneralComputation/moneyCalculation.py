class moneyCalc:
	''' A simple class to find out how much money goes where '''
	def __init__(self,val):
		self.income = val
		self.savings =  0.10*val
		self.loans = 0.40*val
		self.food = 0.10*val
		self.remain = 0.50*val
	#10pc needs to go to the savings	
	
x = float(raw_input("Enter the total money you have: "))
money = moneyCalc(x)
print "Total income is: ",money.income
print "Money you should save: ",money.savings
print "Money you should send for loans: ",money.loans
print "Money you should spend on food: ",money.food
print "Money left with you now: ",money.remain
	
