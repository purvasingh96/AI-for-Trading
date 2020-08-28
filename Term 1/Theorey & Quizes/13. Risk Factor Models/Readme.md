# Risk Factor Models

## Overview

A factor risk model is a method used by investors to estimate the riskiness and relationship between securities. In particular, a factor risk model allows investors to construct the covariance matrix of the assets in the portfolio.<br><br>
<img src="./Images/1. risk factor model overview.png" width=400 height=250></img>
<img src="./Images/2. volatility.png" width=400 height=250></img>

## Factor model of an asset return

An asset's return can be modeled as the contribution from a set of factors, plus the specific return (the part that isn't explained by the factors).

### Factor model formula to calculate return of 1 stock and 1 factor

<img src="./Images/3. 1 stock 1 factor.png" width=350 height=250></img>


### Factor model formula to calculate return of 1 stock and 2 factors

<img src="./Images/4. 1 stock 2 factors.png" width=350 height=250></img>

### Generalized formula for factor model of return

<img src="./Images/5. generalized factor return formula.png" width=350 height=250></img>

## Factor model of a portfolio return

### Factor exposure of portfolio
A portfolio's *factor exposure*, is a weighted average of the exposures from its individual stocks. For each stock in portfolio, multiply each stock's portfolio weight by its exposure and sum up all the Betas.<br>

<img src="./Images/6. factor exposure of portfolio.png" width=350 height=250></img>

### Contibutions of factors to portfolio return

To calculate contributions of factors in portfolio return, we simply add the exposures of each factor in the model -<br>

<img src="./Images/7. contributions of factors to portfolio return.png" width=500 height=250></img>

### Specific return of portfolio
Specific return of a portfolio is the weighted sum of specific return of each stock.<br>

<img src="./Images/8. specific return.png" width=400 height=150></img>

### Factor model of portfolio variance

<img src="./Images/9. factor model of portfolio varience.png" width=400 height=250></img>



