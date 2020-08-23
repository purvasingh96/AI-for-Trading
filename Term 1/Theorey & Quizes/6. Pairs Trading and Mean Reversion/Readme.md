# Pairs Trading and Mean Reversion

## Mean Reversion

The two most popular types of trading strategies are momentum and mean reversion. A mean reversion trading strategy involves betting that *prices will revert back towards the mean or average.* Momentum predicts prices will continue in the same direction. 

A simplistic example of a mean reversion strategy is to buy a stock after it has had an unusually large fall in price. When a stock has seen a big drop, there’s usually a good chance that it will bounce back to a more normal level.

## Pairs Trading

Pairs Trading is a trading strategy that matches a long position in one stock/asset with an offsetting position in another stock/asset that is statistically related. Pairs Trading can be called a mean reversion strategy where we bet that the prices will revert to their historical trends.

<img src="./images/1. pairs trading.png" width=450 height=250></img>

### Spread and Hedge Ratio

A hedge ratio is the comparative value of an open position's hedge to the aggregate size of the position itself. It is expressed as a decimal or fraction and is used to quantify the amount of risk exposure one has assumed through remaining active in an investment or trade.

The formula for the hedge ratio is:
```
Hedge Ratio = Value of the Hedge / Total Position Value
```

To explain this, consider we have a long position in stock A and short position in stock B. The positons are in a certain propotion so that overall positon remains constant throughout the time. The propotion that helps us create this *neutral position* is called *hedge ratio.* Hedge ratio can be calculated as follows - <br>
<br><br><img src="./images/2. hedge ratio.png" width=350 height=200></img><br><br>

Spread can be calculated after we have the values for *hedge*:
<br><br><img src="./images/3. spread.png" width=350 height=200></img><br><br>


## Correlation and Cointegration
### Correlation
Correlation is quantified by the correlation coefficient ρ, which ranges from -1 to +1. The correlation coefficient indicates the degree of correlation between the two variables. The value of +1 means there exists a perfect positive correlation between the two variables, -1 means there is a perfect negative correlation and 0 means there is no correlation.

A perfect positive correlation is when one variable moves in either up or down direction, the other variable also moves in the same direction with the same magnitude while a perfect negative correlation is when one variable moves in the upward direction, the other variable moves in the downward (i.e. opposite) direction with the same magnitude.

The correlation coefficient for the two variables is given by
```
Correlation(X,Y) = ρ = COV(X,Y) / SD(X).SD(Y)
```
where, cov (X, Y) is the covariance between X & Y while SD (X) and SD(Y) denotes the standard deviation of the respective variables.

If the correlation is high, say 0.8, traders may choose that pair for pairs trading. This high number represents a strong relationship between the two stocks. So if A goes up, the chances of B going up are also quite high. Based on this assumption a market neutral strategy is played where A is bought and B is sold; bought and sold decisions are made based on their individual patterns.

### Cointegration

The most common test for Pairs Trading is the cointegration test. Cointegration is a statistical property of two or more time-series variables which indicates if a linear combination of the variables is stationary.

The two-time series variables, in the above case, are the log of prices of stocks A and B. Linear combination of these variables can be a linear equation defining the spread:

As you know, Spread = log(a) – nlog(b), where ‘a’ and ‘b’ are prices of stocks A and B respectively.

<br><br><img src="./images/4. Cointegration.png" width=450 height=250></img><br><br>

For each stock of A bought, you have sold n stocks of B.


If A and B are cointegrated then it implies that this equation above is stationary. A stationary process has very valuable features which are required to model Pairs Trading strategies. For instance, in this case, if the equation above is stationary, that suggests that the mean and variance of this equation remains constant over time. So if we start with ‘n’, which is called the hedge ratio, so that spread = 0, the property of stationary implies that the expected value of spread will remain as 0. Any deviation from this expected value is a case for statistical abnormality, hence a case for pairs trading!

### Engle-Granger Test

The method to test if two series are co-integrated is called *Engle-Granger Test.*:<br>

1. Get the hedge ratio from linear regression
2. Calculate spread and check if spread is stationary.
    * if spread is staionary -> two series are cointegrated.





