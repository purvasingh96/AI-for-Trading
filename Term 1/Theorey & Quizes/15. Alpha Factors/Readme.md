# Alpha Factors

## Reference Links

1. [Zipline data ingestion](https://www.zipline.io/bundles.html#ingesting-data-from-csv-files)
2. [Demeaning portfolio to make it sector/dollar neutral](https://www.zipline.io/_modules/zipline/pipeline/factors/factor.html#Factor.demean)
3. [Ranking in zipline](https://www.zipline.io/appendix.html#zipline.pipeline.factors.Factor.rank)
4. [Scipy's rankdata for handling ties](https://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.stats.rankdata.html)
5. [Z-score](https://www.zipline.io/appendix.html#zipline.pipeline.Factor.zscore)
6. [Simple Moving Average](https://www.zipline.io/appendix.html#zipline.pipeline.factors.SimpleMovingAverage)
7. [Exponential Weighted Moving Average](https://www.zipline.io/appendix.html#zipline.pipeline.factors.ExponentialWeightedMovingAverage)

## Terminologies

1. *Alpha model* is an algorithm that transforms data numbers associated with each stock.

2. *Alpha value* refers to a single value for a single stock, for a single time period.

3. *Alpha vector* has a number for each stock, and the number is proportional to the amount of money we wish to allocate for each stock. Alpha vector is standardized so that it has 0 mean and sum of absolute values adds up to 1.

4. *Alpha factor* : a time series of alpha vectors (over multiple time periods).

5. *Raw alpha factor* : a version of an alpha factor before additional processing.

6. *Stock universe* : set of stocks under consideration for the portfolio.

7. *Sector Neutral* : A sector neutral portfolio is a portfolio that is constructed in such a way that it does not take any active positions or 'active risk'. This means that the portfolio does not deviate from the benchmark weights to which the portfolio is compared.

8. *Dollar Neutral* : A dollar neutral strategy invests the same amount of money long and short without accounting for the volatility (risk) of either side. Depending on volatility you either end up positively or negatively correlated with the market.

9. *Dealing with outliers* :
    * *Winsorizing alpha vectors* : Replacing alpha values that exceeds 95th percentile by the alpha value at 95th percentile and replacing alpha values lower than 5th percentile by value at 5th percentile.
    * Set a maximum allowed weight for alpha vectors.

10. Z-score : Normalizing alpha factors by substracting mean and dividing by standard deviation for consitent range and distribution.

| S.No. | Ranking                                                                       | Z-scoring                                                                                                   |
|-------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| 1.    | Makes alpha factors more robust to outliers and noise.                        | Not robust against outliers and noise.                                                                      |
| 2.    | Best to use when all alpha vectors are generated from the same stock universe | Useful to apply ranking and then z-scoring when alpha vectors are generated from different stock universes. |

11. *Smoothing* : Data smoothing is done by using an algorithm to remove noise from a data set. This allows important patterns to stand out. Data smoothing can be used to help predict trends, such as those found in securities prices. For example : moving average, exponential weighted moving average.

12. *Leverage Ratio* : The sum of absolute values of all positions long and short divided by whatever capital we devote to support those positions.<br>
`
leverage_ratio = postion/capital
`
13. *Factor-weighted returns* : If you created a theoretical portfolio in which the weights for each stock were chosen based on the factor scores (the z-scores we calculated earlier), then we could calculate the daily returns of that theoretical portfolio.
The returns of this portfolio, in which its weights were determined by the alpha factor, are called the "factor-weighted returns", and also referred to as "factor returns."


14. *Sharpe Ratio* : A key metric for evaluating alpha factors. Sharpe ratio is the daily factor return divided by standard deviation of the return. Alpha factors with high sharpe ratio are preferred.

15. *Rank Information Coefficient (Rank IC)* : The information coefficient (IC) is a measure used to evaluate the skill an investment analyst or active portfolio manager. An IC of +1.0 indicates a perfect prediction of actual returns, while an IC of 0.0 indicates no linear relationship. In the below example, since the rank of alpha values and rank of forward asset returns are the same, Rank IC is 1.<br><br>
<img src="./Images/1. rank ic.png" width=250 height=250></img>

16. Steps to calculate Rank IC - 
   * Rank alpha values.
   * Rank forward returns.
   * Calculate Spearman correlation between ranked alpha values and ranked forward returns.
   * The Spearman correlation coefficient is defined as the Pearson correlation coefficient between the rank variables.<br><br>
   <img src="./Images/2. spearman coefficient.png" width=400 height=150></img>
   
17. *Information Ratio (IR)* : The information ratio (IR) is a measurement of portfolio returns beyond the returns of a benchmark, usually an index, compared to the volatility of those returns. The IR is often used as a measure of a portfolio manager's level of skill and ability to generate excess returns (specific/residual returns) relative to a benchmark, but it also attempts to identify the consistency of the performance by incorporating a tracking error, or standard deviation component into the calculation.

18. *Fundamental Law of Active Management* : <br><br>
   <img src="./Images/3. fundamental law of active management.png" width=230 height=100></img><br>
      * IR : Information Ratio
      * IC : Information Coefficient, improves alpha factor
      * Breadth : Number of *indipendent* trading opportunities per year.
 
19. *Real world constraints* - 
   * *Liquidity* : Liquidity refers to the ease with which an asset, or security, can be converted into ready cash without affecting its market price.
   * *Bid-ask spread* : The bid-ask spread is essentially the difference between the highest price that a buyer is willing to pay for an asset and the lowest price that a seller is willing to accept.
   * *Transaction Costs* : Transaction costs are expenses incurred when buying or selling a good or service. Transaction costs represent the labor required to bring a good or service to market, giving rise to entire industries dedicated to facilitating exchanges. In a financial sense, transaction costs include brokers' commissions and spreads, which are the differences between the price the dealer paid for a security and the price the buyer pays.

20. *Turnover* : turnover measures what fraction of portfolio's total value gets traded in a time period.<br>

  * `Turnover = Value of trades / Portfolio Value`
  * *Factor Rank Autocorrelation* : 
      * High FRA => Low Turnover
      * Low/Negative FRA => High Turnover
      * Lower turover helps us because it makes it more possible for us to execute trades if stocks are liquid and can reduce transaction costs.
      * If 2 alpha factors have similar Sharpe Ratio, similar quantile profile and similar factor returns, perfer the one with *lower turnover.*
      * Alpha factor with high sharpe ratio but very high turnover, check that alpha factor for back-testing.


21. *Quantile Analysis* - <br><br>
<img src="./Images/4. quantile analysis.png" width=550 height=300></img>

22. *Ideal Alpha Factors Quantile Performance* - Each successive quantile produces a higher return than the previous one. <br><br>
<img src="./Images/5. ideal quantil analysis.png" width=550 height=300></img>

23. *Transfer Coefficient* : Measures how closelythe optimized portfolio weights match the original alpha vector. <br>
`transger_coefficient = scipy.stats.stats.pearsonr(alpha_weights, optimized_portfolio_weights)`


# Life of an Alpha Factor

<img src="./Images/life of alpha/1. propose alpha factor.png" width=350 height=100></img><br>
<img src="./Images/life of alpha/7. arrow_new.png" width=175 height=60></img><br>
<img src="./Images/life of alpha/2. perform out of sample testing.png" width=350 height=100></img><br>
<img src="./Images/life of alpha/7. arrow_new.png" width=175 height=60></img><br>
<img src="./Images/life of alpha/3. paper trading.png" width=350 height=100></img><br>
<img src="./Images/life of alpha/7. arrow_new.png" width=175 height=60></img><br>
<img src="./Images/life of alpha/4. alpha to prod.png" width=350 height=100></img><br>
<img src="./Images/life of alpha/7. arrow_new.png" width=175 height=60></img><br>
<img src="./Images/life of alpha/5. alpha weight small.png" width=350 height=100></img><br>
<img src="./Images/life of alpha/7. arrow_new.png" width=175 height=60></img><br>
<img src="./Images/life of alpha/6. remove alpha.png" width=350 height=100></img><br>




