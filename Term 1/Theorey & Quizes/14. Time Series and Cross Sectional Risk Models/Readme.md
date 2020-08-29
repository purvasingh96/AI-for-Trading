# Time Series Models

## Covariance Matrix of Factors

We'll collect a time series that represents the chosen factor. In this case, our factor is "market excess return", so we can use an index (such as the S&P500) and subtract a time series that represents the risk-free rate, such as the three-month US Treasury Bill rate. Calculating the variance of this market excess return helps us fill in the covariance matrix of factors.

<img src="./Images/1. market return.png" width=400 height=250></img>

## Factor Exposure
We can use regression to calculate the factor exposures in a time series model. We'll use the asset's excess return as the dependent "y" variable, and the factor return (in this case, market excess return) as the independent "x" variable. The estimated coefficient from the regression is an estimate of the asset's "exposure" to that factor.

<img src="./Images/2. factor exposure.png" width=400 height=290></img>

## Specific Variance

To get the specific return, take the difference between the actual return and estimated return.

<img src="./Images/3. specific return at time t.png" width=450 height=290></img>

## SMB (Small Minus Big)

To create a theoretical portfolio representing size, we could go long the bottom 10th percentile of stocks by market cap (long small cap stocks) and go short stocks above the 90th percentile (go short the large cap stocks). We could assume an equal dollar amount invested in each stock. In the above example, we are dividing by 2 to take the average return of going long small cap stocks and going short large cap stocks.

It's also common to compute the spread between two portfolios. One portfolio contains the small cap stocks, and the other portfolio contains the large cap stocks. In this case, we'd just take the difference between the returns of the two portfolios.

<img src="./Images/4. SMB.png" width=450 height=290></img>
