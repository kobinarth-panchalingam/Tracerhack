stock_prices_week = input('Input stock prices of the week: ') 
stock_prices = stock_prices_week.split(' ')

for i in stock_prices:                                         #removing empty elements
    if i == ' ':
        stock_prices.remove(i)
        
try:
    stock_prices = list(map(float, stock_prices))              #converting strings to numbers
except ValueError:
    print('Input a number only')
else:
    for k in stock_prices:
        if k<0:
            raise Exception('Stock price can not be negative') #for negative input
                
    average_stock_price = round(sum(stock_prices)/7, 1)        # finding average stock price
    reference_price = 10 + average_stock_price
    valued_days = 0
    for j in stock_prices:
        if j > reference_price:
            valued_days += 1
    print('Number of valued days: %s'%valued_days)
    if valued_days >=3 :
        print('RECOMMENDED')
    else:
        print('NOT RECOMMENDED')


