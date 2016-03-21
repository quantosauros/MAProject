'''
Created on 2016. 3. 8.

@author: jayjl
'''

from yahoo_finance import Share

from Parser.models import EtfInfo, EtfData, StockInfo, StockDetail



etfResult = StockInfo.objects.values('ticker', 'name')

#for etfIdx in range(0, len(etfResult)) :
tickerStr = etfResult[0]['ticker']

share = Share(tickerStr)

dateStr = share.get_trade_datetime()[0:11].replace('-','')
ma_200Str = convert(share.get_200day_moving_avg())
ma_50Str = convert(share.get_50day_moving_avg())
book_valueStr = convert(share.get_book_value())
volume_avgStr = convert(share.get_avg_daily_volume())
ebitdaStr = convert(share.get_ebitda())
dividend_yieldStr = convert(share.get_dividend_yield())
market_capStr = convert(share.get_market_cap())
year_highStr = convert(share.get_year_high())
year_lowStr = convert(share.get_year_low())

print tickerStr, dateStr, ma_200Str, ma_50Str, book_valueStr, volume_avgStr, ebitdaStr, dividend_yieldStr, market_capStr, year_highStr, year_lowStr


# print share.get_change()
# print share.get_days_high()
# print share.get_days_low()
# print share.get_dividend_share()
# print share.get_info()
# print share.get_open()
# print share.get_prev_close()
# print share.get_price()
# print share.get_price_book()
# print share.get_price_earnings_growth_ratio()
# print share.get_price_earnings_ratio()
# print share.get_price_sales()    
# print share.get_short_ratio()
# print share.get_stock_exchange()
# print share.get_volume()

    
p = StockDetail(dt = dateStr, ticker = tickerStr,
                ma_200 = ma_200Str, ma_50 = ma_50Str,
                book_value = book_valueStr,
                volume_avg = volume_avgStr,
                ebitda = ebitdaStr,
                dividend_yield = dividend_yieldStr,
                market_cap = market_capStr,
                year_high = year_highStr,
                year_low = year_lowStr)

p.save()

    