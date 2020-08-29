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

## HML (High Minus Low)

Research show that *stocks that have high book value relative to their market price, tends to outperform stocks with lower book value.* book value of a company is the total value of the company's assets, minus the company's outstanding liabilities.

<img src="./Images/5. HML.png" width=480 height=310></img>

## Famma French 3 Factor Model
The Fama and French model has three factors: size of firms, book-to-market values and excess return on the market. In other words, the three factors used are SMB (small minus big), HML (high minus low) and the portfolio's return less the risk free rate of return.

<img src="./Images/6. Famma French 3 factor model.png" width=480 height=310></img> <img src="./Images/7. SMB and HML.png" width=480 height=310></img>

### Formula for calculating SMB and HML

<img src="./Images/8. SMB and HML formula.png" width=480 height=130></img>

## Time Series Risk Model

<img src="./Images/9. Time series risk model.png" width=480 height=330></img>

### Matrix of Factor Returns
Calculate the covariance matrix using the time series of factor returns.

<img src="./Images/10. matrix of factor returns.png" width=430 height=130></img>

### Matrix of Factor Exposures
Use a multiple regression to estimate the factor exposures.

<img src="./Images/11. factor exposure.png" width=430 height=330></img>

### Specific Variance
Calculate the actual minus estimated returns as the specific return. The variance of that time series is an estimate of specific variance.

<img src="./Images/12. specific return.png" width=450 height=330></img>

# Cross Sectional Models

## Overview
A cross-section means that we use multiple stocks for a single time period in a calculation. In contrast, a time series is looking at a single stock over multiple time periods.

A cross-sectional model calculates the factor exposure first, and then uses that information to estimate the factor return.

<img src="./Images/14. time series v:s cross sectional model.png" width=450 height=330></img>

## Estimating Factor Return

If we collect a cross-section of multiple stocks for a single time period, then we'll have pairs of stock returns and factor exposures. We can use regression to estimate the factor return for that single time period. Then repeat over multiple time periods to get a time series of factor returns.

<img src="./Images/13. estimating factor return.png" width=450 height=330></img>

## Specific Return

For each time period, we can calculate the specific return as the difference between actual stock return and estimated stock return (using the estimated factor return). Do this for multiple time periods to get a time series of specific return.

<img src="./Images/15. specific return for cross-sectional model.png" width=450 height=330></img>

## Fundamental Factors
In a cross-sectional risk model, the fundamental data calculated on a company, based on its financials, can be used as the factor exposure of that company, to that factor. We can use regression on a cross-section of stocks to estimate the factor return.

<img src="./Images/14. Fundamental factors.png" width=450 height=330></img>

