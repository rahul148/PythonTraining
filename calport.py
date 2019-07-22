
def portfolio(quantity,prize):
    amount=0
    
    for i in range(0,len(share)):
        amount=amount+(quantity[i]*prize[i])
    return amount
share=["idea","reliance","TATA"]
quantity=[10,5,25]
prize=[128,376,218]
result=portfolio(quantity,prize)

