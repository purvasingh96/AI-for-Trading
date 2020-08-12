# Stock Prices

# Terminologies

## Basics

1. **Stock** : An asset that represents ownership in a company. A claim on part of a corportation's assets and earnings. There are two main types, common and preferred.

2. **Share** : A single share represents partial ownership of a company relative to the total number of shares in existence.

3. **Common Stock** : One main type of stock; entitles the owner to receive dividends and to vote at shareholder meetings.

4. **Preferred Stock** : The other main type of stock; generally does not entail voting rights, but entitles the owner to a higher claim on the assets and earnings of a company.

5. **Dividend** : A partial distribution of a company's profits to shareholders.

6. **Capital Gains** : Profits that result from the sale of an asset at a price higher than the purchase price.

7. **Security** : A tradable financial asset.

8. **Debt Security** : Money that is owed and must be repaid, like government or corporate bonds, or certificates of deposit. Also called fixed-income securities.

9. **Derivative Security** : A financial instrument whereby its value is derived from other assets.

10. **Equity** : The value of an owned asset minus the amount of all debts on that asset.

11. **Equity Security** : A security that represents fractional ownership in an entity, such as stock.

12. **Option Contract** : A contract which gives the buyer the right, but not the obligation, to buy or sell an underlying asset at a specified price on or by a specified date

13. **Futures Contract** : A contract that obligates the buyer to buy or the seller to sell an asset at a predetermined price at a specified time in the future

## Buy and Sell Side
1. *Buyers and sellers* are those who go through the stock exchange to buy a stock that they think will do well, or sell a stock that they wish to remove from their investments. <br>
2. *Market maker*, is the one who serves as the counterparty of these buyers or sellers. Since every buyer needs a seller, and every seller needs a buyer, a market maker plays the role of seller to those who wish to buy, and plays the role of buyer for those who wish to sell and by convention they are known as *sell side of the finance industry*. The sell side usually includes investment banks such as *Goldman Sachs, Morgan Stanley*.<br>
3. The *buy side* refers to individual investors, and investment funds such as mutual funds and hedge funds.

## Liquidity

*Liquidity* refers to a property of a financial asset which is meant to be bought or sold without causing sharp changes in its price.

## Tick Data
Stock exchange publishes a stream of data that includes each individual trade. This is known as *tick data*. Ticks are an intuitive way to check the health of a stock. Tick data can also forms the basis of all market data available for analysis and help you make better intraday decisions.<br>
<img src="./images/1. tick_data.png" width="350" height="250"></img>

## OHLC : Open, High, Low, Close
The most common terms used in practice are *Open, High, Low, Close (OHLC)*. Below is an example of how we represent OHLC: <br>

<img src="./images/2. OHLC.png" width="350" height="200"></img>
<img src="./images/3. OHLC Chart.png" width="350" height="200"></img>

* Open is the stock price at the begining of the period.
* High and Low capture its range of movement 
* Close is where it ends. 
* Daily closing price is the one that is quoted most often. This is usually used by casual traders and investors interested in long term gains.
* Opening price is where the first trade of the day to take place. There might be a gap from last day's closing price due to pre-market trading or trading in other markets.
* High-Low captures the movement of the stocks

## Volume
Another valuable metric is the number of shares traded over a period of time known as *Volume*. Sum of *unit_price times volume* gives an accurate description of total amount of money moving around. Volume can also decide how sharply the price may rise or fall.<br>
In general:<br>
* *large volume of buy order tends to increased stock price*. 
* *large volume of net sell orders tends to decreased stock price*. 

### Intraday Volume
Stocks that are of active interest will see a lot of trading at the begining of the day. All the investors engage in a process called *price discovery* where they analyze all the new information gathered since the previous day's market close. This process of *price discovery* helps buyers and sellers agree on a mutually accpetable market price value for the stock.<br><br>
<img src="./images/4. OHLC - Volume.png" width="400" height="200"></img><br><br>
Then the volume falls as the day proceeds.<br>
Finally, towards the end of the trading day, activity tends to increase a little, resulting in higher volume. This can happen due to day-traders wanting to close out any open positions and funds that typically update their holdings at the end of the day.<br><br>
<img src="./images/5. Intraday Volume.png" width="350" height="200"></img><br>


# Data Processing

## Stock Splits
The set of data related to an event that a company an take which may affect the shareholders are called *coroporate actions.* Some of the corporate actions are-<br>
1. Stock Splits
2. Divident

When a company decides to split its stocks into two, *its price drops by half.* This makes sure that total market capitalization has not changed by the split. *Market Capitalization* is the dollar value of a company's outstanding shares.<br>

```
Market Capitalization = Stock Price X Total number of shares outstanding
```
<br>
<img src="./images/6. Stock Split.png" width="350" height="200"></img>

Now when stock split happens (2:1), there are *twice as many outstanding shares*. In order to neutralize the market capitalization, the *stock price has to drop by half.*<br>
One of the reasons as to why companies perform *stock split* is to make the stock more liquid in order to maintain healthy volume of transactions.

### Stock Split Normalization
If we look at the graph of a company's stock price that has recently performed stock split, it may look like that company's stock has reduced drastically, which *is not the case*. The value of the company has not changed since the split. In order to correct this, we need to normalize the data to mitigate the sudden changes. <br><br>
<img src="./images/7. Stock drops.png" width="350" height="200"></img><br>
One of the ways to normalize stock-split data is to half the price before 2:1 split, thirds the price before any 3:1 split and so on. Stock prices normalized in such manner are called *adjusted prices.*<br><br>
<img src="./images/8. Adjusted Prices.png" width="350" height="200"></img>




















