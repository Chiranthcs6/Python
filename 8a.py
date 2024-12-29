import random
import pandas as pd
from datetime import datetime, timedelta

end_date = datetime.now()
start_date = end_date - timedelta(days=180) 
date_range = pd.date_range(start_date, end_date, freq='D') 

company_a_prices = [random.uniform(50, 150) for _ in date_range]
company_b_prices = [random.uniform(30, 120) for _ in date_range]

stock_data = pd.DataFrame({
     'Date': date_range,
 'Company A Stock Price': company_a_prices,
 'Company B Stock Price': company_b_prices
})

stock_data.to_csv('stock_prices.csv', index=False)