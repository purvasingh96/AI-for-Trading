# Time Series Models

## Covariance Matrix of Factors

We'll collect a time series that represents the chosen factor. In this case, our factor is "market excess return", so we can use an index (such as the S&P500) and subtract a time series that represents the risk-free rate, such as the three-month US Treasury Bill rate. Calculating the variance of this market excess return helps us fill in the covariance matrix of factors.

<img src="./Images/1. market return.png" width=400 height=250></img>

## Factor Exposure
We can use regression to calculate the factor exposures in a time series model. We'll use the asset's excess return as the dependent "y" variable, and the factor return (in this case, market excess return) as the independent "x" variable. The estimated coefficient from the regression is an estimate of the asset's "exposure" to that factor.

<img src="./Images/2. factor exposure.png" width=400 height=290></img>
