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
