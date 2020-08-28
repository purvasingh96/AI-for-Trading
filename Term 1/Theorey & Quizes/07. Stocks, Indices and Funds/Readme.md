# Stocks, Indices and Funds

## Definitions

### Index 
* Aggregated value of a group of stocks as a single number. E.g. S&P500 and DJIA (Dow Jones Industrial Average) for USA. They are *virtual profiles* and are not actual funds that people invest in.
* Indices track subgroups of the market, and may be designed specifically to track stocks in the same stock exchange, same country, or same sector.
* Indices give investors a measure of the market’s status.
* Professional investment managers may use indices as benchmarks against which they can evaluate their own fund’s performance.

### Market Captialization

Market capitalization refers to the total dollar market value of a company's outstanding shares of stock. Commonly referred to as "market cap," it is calculated by multiplying the total number of a company's outstanding shares by the current market price of one share.

### Growth Stock v/s Value Stock

* Growth stock tends to have high growth is sales or earnings and have potential for future growth.
* Values stock tends to be a matured company that has stable sales, revenue and earnings.

### Ratios

* *Price to earnings ratio* : the stock price divided by the company’s earnings per share over the past four quarters. 
* *Price to sales ratio* : the the stock price divided by the sales per share over the past four quarters.
* *Price to book ratio* : the stock price divided by the book value per share.

* The book value is the company’s accounting value, which is assets minus liabilities

* Growth stocks tend to have high price to earnings, price to sales, and price to book ratios.
* Value stocks tend to have lower price to earnings, price to sales, and price to book ratios.


### Free Float
* Free float shares refers to the number of shares that are liquid and tradable on the stock exchange.
* Free float shares may be considered a better measure when calculating market cap because only free float shares can be bought or sold, which means only the trade of free float shares affects the market movement of the stock.

### Active vs. Passive Funds
* Actively Managed Fund: seeks to outperform its benchmark (such as an index).
* Passively Managed Fund: seeks to track its benchmark (such as an index).
* *Note:*  passively managed funds that track an index are also referred to ask “index funds”. An index fund is a fund, not an index.


## Smart Beta Portfolios

* When we use the universe of stocks from an index, and then apply some weighting scheme other than market cap weighting, it can be considered a type of smart beta fund.
* By contrast, a purely alpha fund may create a portfolio of specific stocks, not related to an index, or may choose from the global universe of stocks. The other characteristic that makes a smart beta portfolio "beta" is that it gives its investors a diversified broad exposure to a particular market.
* To calculate *dollar volume weights : *
   * Multiply close price and volume
   * Normalize this column by dividing it by its sum. You can use `divide()` method.

## Funds : Mutual Funds and Hedge Funds
### Mutual Funds
* Everyday investors
* Long Only
* No Lockup Period
* 2 types of mutual funds -
    * **Open-end** : New investments allowed after fund starts. Allows investors to withdraw money directly from fund.The total return of the fund is a weighted average of the portfolio return and the interest earned from the cash.
      * Holding cash : The total return of an open end fund is a weighted average of its portfolio return and the return on its cash holdings. 
      `The fraction invested in equities × return on equities + fraction invested in cash × return on cash = total return`
    * **Close-end** : Closed End Funds accept investors at the start of the fund, and do not take new investments nor handle redemptions afterward. This means that the closed end fund does not need to keep cash for liquidity purposes or to handle redemptions. Investors who wish to stop investing in the fund may sell their shares to other investors on a stock exchange, the same way they would sell stocks. 

### Hedge Funds

* Hedging refers to entering into a transaction in order to reduce exposure to price fluctuations by buying derivatives such as futures, options
* High Net Worth or Institutions (Pension Funds)
* Long and Short positions
* Trade Derivatives (Options, Futures)
* Lockup Periods in which investors cannot redeem their investments.


## Relative and Absolute Returns

### Relative Returns

Relative return is a fund’s return minus its benchmark’s return. For an actively managed fund, this is called the active return. For a passively managed fund, this is the tracking error.

### Tracking Error formula

<img src="./Images/1. TE formula.png" width=650 height=250></img>

### Absolute Returns
Absolute returns refer to a fund’s goal to target a certain return regardless of how the market performs. Hedge funds are usually evaluated by absolute returns.

### Net Asset Value (NAV)
```
NAV: Net Asset Value AUM: Assets Under Management NAV = (AUM - Expenses) / (number of shares)
```

### Expense Ratio
`AUM: Assets Under Management Gross Expense Ratio: Expenses / AUM Net Expense Ratio: (Expenses - Discounts) / AUM `

### Transaction Costs

Transaction costs are costs from buying or selling (trading) stocks or other assets. The main type of transaction cost for institutional investors (mutual funds, hedge funds) are the costs of moving the market price from large trades.
