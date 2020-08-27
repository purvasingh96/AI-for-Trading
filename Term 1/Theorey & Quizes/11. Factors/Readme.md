# Factors

## Overview
Factors are a list of numerical values, one for each stock, potentially predictive of an aspect of the performance of these stocks in the future. Below figure shows an example of factor-<br>

<img src="./Images/1. factor_example.png" width=450 height=250></img><br>

Here, we are assigning larger weights to the company that has greater return and lower weights to the company with lower returns.

## Standardizing Factors

The below 2 figures show how to standardize a factor and the coresponding example.<br>

<img src="./Images/2. Standardized factor.png" width=450 height=250></img> <img src="./Images/3. standardizing factor example.png" width=450 height=250></img>

## Why do we need to standardize factors?

* We need to standardize factors in order to make the portfolio *dollar neutral*.

<img src="./Images/4. demean for dollar neutral.png" width=450 height=250>

* Dollar Neutral implies a portfolio has *dollar amount of long positions equals dollar amount of short positions.*
* If a portfolio is *dollar neutral,* then it is less influenced by overall market movement as shown in the figure below.

<img src="./Images/5. dollar neural.png" width=450 height=250>

* *Notional* : A portfolio's notional is the number we can multiply the stock weights by in order to get a dollar value for each stock's position. When all the positions add up to 0, it is called *dollar neutral*.<br>

<img src="./Images/6. dollar neutral example.png" width=450 height=250>
