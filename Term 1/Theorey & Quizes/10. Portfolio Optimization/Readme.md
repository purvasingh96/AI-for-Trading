# Portfolio Optimization


## Derivation of Optimal Weights on a Two-Asset Portfolio

Considering 2 stocks A and B, We want to solve for the weight on each asset. Our objective function for this problem is the expression for the portfolio variance:

<img src="./images/1. main equation.png" width=500 height=60></img><br>

We have to minimize equation (1). We have the following constraint : <br>

<img src="./images/2. constraint.png" width=200 height=60></img><br>

It turns out that this is a problem we can solve analytically. If we substitute (2) into (1), we will get a function of a single variable:

<img src="./images/3. variance.png" width=400 height=60></img><br>

Now, if we plot the graph for σ2p in terms of Xa, we will get a parabola : 

<img src="./images/4. plot.png" width=450 height=400></img><br>

<img src="./images/5. derivation.png" width=500 height=400></img><br>

Now we know the portfolio weights. You can see that they are only dependent on the standard deviations of Stock A and B, and their covariance. If we wanted to know the expected portfolio mean, we only have to remember that it is the weighted sum of the individual portfolio means:

<img src="./images/6. mean.png" width=200 height=60></img><br>

## Formulating Portfolio Optimization Problems

### Common Constraints

1. No short selling. (All the enteries must be positive).

<img src="./images/1. no short selling.png" width=450 height=40></img><br>

2. Limit sectors.

<img src="./images/2. sector limits.png" width=550 height=40></img><br>

3. Minimum acceptable portfolio return.

<img src="./images/3. min acceptable retusn.png" width=550 height=40></img><br>

4. Maximizing portfolio returns.

<img src="./images/4. max portfolio return.png" width=550 height=75></img><br>

5. Maximizing portfolio returns and minimizing variance.

<img src="./images/6. maximize return and min risk.png" width=550 height=40></img><br>

6.  One way to formulate an optimization problem is to use the L2 norm and minimize the difference between your vector of portfolio weights and a set of predefined target portfolio weights x star.

<img src="./images/7. min distance.png" width=550 height=50></img><br>

7. Minimizing the difference between your portfolio weights and the weights on the assets in the index, and minimize portfolio variance at the same time. The tradeoff between these goals would be determined by a parameter,λ.

<img src="./images/8. lambda tradeoff.png" width=590 height=50></img><br>





