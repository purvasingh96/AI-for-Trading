# Time Series Modelling

Here we will cover the following -

1. Autoregression
2. Moving averages
3. Autoregressive Moving Averages
4. Autoregressive Integrated Moving Averages
5. Kalman and Particle Filters
6. Recurrent Neural Networks

## Autoregression Models (AR Models)

An auto-regressive models (AR Models) tries to fit in a line that is linear combination of previous values. It includes an *intercept*, that is indipendent of previous values. It also contains *error term* to represent movements that cannot be predicted by previous terms.

<br><br><img src="./images/1. AR models.png" width="450" height="250"></img><br><br>

An AR model is defined by its *lag*. If an AR model uses only yesterday's value and ignores the rest, its called *AR Lag 1*, if the model uses two previous days values and ignores the rest, its called *AR Lag 2* and so on.

<br><br><img src="./images/2. Lag.png" width="450" height="250"></img><br><br>

## Moving Average Models (MA Models)
In MA models, we start with average *mu*, to get the value at time t, we add a linear combination of *residuals* from previous time stamps. In finance, *residual* refers to new unpredictable information that can't be captured by past data points. The residuals are *difference between model's past prediction and actual values.* <br>
Moving average models are defined as *MAQ* where *Q is the lag.*
<br><br><img src="./images/2. MA model.png" width="590" height="80"></img><br><br>
