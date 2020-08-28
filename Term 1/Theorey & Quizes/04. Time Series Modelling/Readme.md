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

Usually, autoregressive models are applied to stationary time series only. This constrains the range of the parameters phi.
For example, an AR(1) model will constrain phi between -1 and 1. Those constraints become more complex as the order of the model increases, but they are automatically considered when modelling in Python.

## Moving Average Models (MA Models)
In MA models, we start with average *mu*, to get the value at time t, we add a linear combination of *residuals* from previous time stamps. In finance, *residual* refers to new unpredictable information that can't be captured by past data points. The residuals are *difference between model's past prediction and actual values.* <br>
Moving average models are defined as *MAQ* where *Q is the lag.*
<br><br><img src="./images/2. MA model.png" width="590" height="80"></img><br><br>

## Auto Regressive Moving Average Model (ARMA)
The ARMA model is defined with a *p and q*. *p* is the lag for autoregression and *q* is lag for moving average. Regression based training models require data to be *stationary*. For a non-stationary dataset, the mean, variance and co-variance may change over time. This causes difficulty in predicting future based on past.

### Extracting stationary data

One way to get stationary time-series is by taking difference between points in time-series. This time difference is called *rate of change.*<br>
```python
rate_of_change = current_price / previous_price
```
<br>
The corresponding log return will become : <br>

```python

log_returns = log(current_price) - log(previous_price)

```

## Autoregressive Integrated Moving Average (ARIMA)
Below figure shows the workflow to run *Augmented Dickey Test* to check if data is stationary or not.

<br><br><img src="./images/6. ARIMA.png" width="450" height="250"></img><br><br>



## Important libraries

```python

from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.stats.diagnostic import acorr_ljungbox
```

