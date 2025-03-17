# gets your gross wage and gives back your net wage

def net_monthly_wage(wage):
	tax_rate = 0.15
	pension_fund_rate = 0.1	
	    
	return wage - (wage * (tax_rate + pension_fund_rate))

net_monthly_wage(7000)