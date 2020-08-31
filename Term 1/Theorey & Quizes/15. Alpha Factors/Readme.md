# Alpha Factors

## Reference Links

1. [Zipline data ingestion](https://www.zipline.io/bundles.html#ingesting-data-from-csv-files)
2. [Demeaning portfolio to make it sector/dollar neutral](https://www.zipline.io/_modules/zipline/pipeline/factors/factor.html#Factor.demean)
3. [Ranking in zipline](https://www.zipline.io/appendix.html#zipline.pipeline.factors.Factor.rank)
4. [Scipy's rankdata for handling ties](https://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.stats.rankdata.html)

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
