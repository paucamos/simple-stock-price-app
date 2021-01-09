import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google for example!
 

 #### Examples
 ```python
 ["GOOGL", "TSLA", "AAPL", ...]
 ```

""")
user_input = st.text_input("Name of the company (default google)", 'GOOGL')
tickerSymbol = user_input

tickerData = yf.Ticker(tickerSymbol)
if tickerData:
	tickerDf = tickerData.history(period='id', start="2010-5-31", end="2020-5-31")	
	
	st.write("""### Closing Price""")
	st.line_chart(tickerDf.Close)
	st.write("""### Volume Price""")
	st.line_chart(tickerDf.Volume)
else:
	st.write("""Your input does not match with an existing company.""")

