# Factor Models and Types of Factors

## Linear Factor Model

A linear factor model relates the return on an asset (be it a stock, bond, mutual fund or something else) to the values of a limited number of factors, with the relationship described by a linear equation as described below -<br><br>
<img src="./Images/1. linear factor model.png" width=350 height=400></img><br><br>


## Latent Variable
In statistics, latent variables are variables that are not directly observed but are rather inferred from other variables that are observed. 

## Assumptions in Factor Model
The common factor model has several key assumptions:

* Unique variances (disturbances) have a mean of zero: E(εi)=0
* Latent factors have mean zero, E(ηi)=0
* Latent factors have a variance of one, var(ηi)=1 (Standardized solution)
* Unique variances are uncorrelated with each other: cov(εi,ε∖i)=0 (Conditional independence)
* Latent factors are independent of each other: cov(ηi,η∖i)=0
* Latent factors are uncorrelated with unique variances: cov(ε,η)=0

These assumptions are necessary to obtain unique solutions to the model parameters (i.e., identification).

## Covariance Matrix Using a Factor Model

1. First we take the following assumptions before deducing the covariance matrix.
<br><br><img src="./Images/2. assumptions.png" width=300 height=200></img><br><br>

2. Substract mean from each asset random variable such that mean of this shifted return distribution is 0. Taking into consideration, the factor model of stock return and if there are N companies and k being the number of factors -
<br><br><img src="./Images/5. matrix representation.png" width=400 height=200></img><br><br>

3. Covariance of 2 random variable can be expressed as below. Since means of those 2 random variables are 0 (assumption 1), the covariance can be refactored as expected value of their product -
<br><br><img src="./Images/6. covariance.png" width=250 height=100></img><br><br>

4. Covariance can hence be written as `expectation value of asset returns times asset returns transpose` -
<br><br><img src="./Images/7. covariance and expected returns.png" width=250 height=100></img><br><br>

5. Based on our assumption, `expectation value of asset returns times asset returns transpose` can be further written as -
<br><br><img src="./Images/9. covariance matrix of residuals.png" width=500 height=250></img><br><br>

# Risk Factors v/s Alpha Factors

| S.No. | Risk Factor                                                                                                                                                                                                                                                                                                                                                                                                                            | Alpha Factor                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.    | Risk factors are significant contributors to the variance of asset returns, and less predictive of the mean of returns. Risk factors are identified to control risk.<br> One way to do control an asset's exposure to a risk factor is to hold an equal amount long as short.<br> For instance, a dollar neutral portfolio with equal amounts long and short is controlling for risks that the overall market may move up or down.<br> | Factors that are significant in describing the mean of asset returns can be candidates for alpha factors. <br> Alpha factors are used to give some indication of whether each stock in the portfolio may have positive expected returns or negative expected returns.<br>  For example, a former alpha factor was the market capitalization of a stock. <br> Small cap stocks tend to have higher future returns compared to large cap stocks. |
| 2.    | Risk factors as a whole account for more of the overall movement of stocks.                                                                                                                                                                                                                                                                                                                                                            | Alpha factors contribute to smaller movements of stocks, which is okay, because we seek to identify these alpha factors because they give some indication of the direction of expected returns, even if they're small compared to risk factors.                                                                                                                                                                                                |
| 3.    | Risk factors are well-known by the investment community, so investors will track those factors when optimizing their portfolios. <br> This also means that it's unlikely that any one investor can gain a competitive advantage (higher than normal returns) using risk factors.                                                                                                                                                       | Alpha factors are less well-known by the investment community, because they're generated by in-house research to help the fund generate higher than normal returns. <br> So alpha factors are said to be drivers of the mean of returns because they're used to help push a portfolio's overall returns higher than what would be expected from a passive buy and hold strategy.                                                               |











