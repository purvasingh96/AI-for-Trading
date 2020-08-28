# Factor Models and Types of Factors

## Linear Factor Model

A linear factor model relates the return on an asset (be it a stock, bond, mutual fund or something else) to the values of a limited number of factors, with the relationship described by a linear equation as described below -<br><br>
<img src="./Images/1. linear factor model.png" width=350 height=400></img><br><br>

1. Factor returns may be called :
* macro-economic variables
* returns on pre-specified portfolios,
* returns on zero-investment strategies (long and short positions of equal value) giving maximum exposure to fundamental or macro-economic factors,
* returns on benchmark portfolios representing asset classes,

2. The *bij* coefficients may be called:
* factor exposures,
* factor sensitivities,
* factor loadings,
* factor betas,
* asset exposures
* style

3. The *si* term may be called:
* idiosyncratic return,
* security-specific return,
* non-factor return,
* residual return,
* selection return

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


