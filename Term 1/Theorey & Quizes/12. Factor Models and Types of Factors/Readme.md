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


