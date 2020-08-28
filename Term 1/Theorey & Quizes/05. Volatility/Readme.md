# Volatility

## Overview

*Volatility* is the standard deviation of probability distribution of log returns. It is the measure of the spread of this particular distribution. Volatility gives a sense of range of values log returns are likely to fall into. <br>

Volatility can be used for : <br>
* Measuring risks
* Defining position sizes
* Designing alpha factors
* Pricing options
* Trading volatility directly

## Historical Volatility
Calculating standard deviation of log returns of past data is known as *historical volatility.*

<img src="./images/1. volatility.png" width=250 height=300></img>

## Annualized Volatility
Annualizing volatility means extrapolating standard deviations of log returns calculated at some time frequency to standard deviations of log returns calculated an an anual frequency.
<br><br><img src="./images/2. annualized volatility.png" width=450 height=250></img><br><br>

Python implementation of calculating which company has the maximum volatility based on its prices can be found [here](https://github.com/purvasingh96/AI-for-Trading/blob/master/Term%201/Theorey%20%26%20Quizes/5.%20Volatility/volatility.py)

### Conversion between monthly/daily log returns to anual log returns
<br><br><img src="./images/3. conversion.png" width=200 height=100></img><br><br>

## Rolling Window
If we want to check how volatility is changing over-time, we use the option of *rolling window.*
<br><br><img src="./images/4. rolling_window.png" width=400 height=250></img><br><br>
Python implementation of using rolling-windows to calculate average can be found [here](https://github.com/purvasingh96/AI-for-Trading/blob/master/Term%201/Theorey%20%26%20Quizes/5.%20Volatility/rolling_windows.ipynb)


## Exponentially Weighted Moving Average
For estimating volatility, we can increase the influence of the more recent past. One common way to do this is to weigh the observation from yesterday, the highest, and then decrease the weights exponentially. This is called *exponentially weighted moving average.*
<br><br><img src="./images/5. EWMA.png" width=400 height=250></img><br><br>

The formula for calculating exponentially weighted moving average is as follows :
<br><br><img src="./images/6. weighted log returns.png" width=500 height=100></img>
<br><img src="./images/7. description_ewma.png" width=560 height=100></img><br><br>


## ARCH and GARCH Models

Sometimes, traders try to forecast volatility before it happens. When trying to model volatility, we can use a special form of autoregressive model called *ARCH*.<br>
* *ARCH : Autoregressive Conditional Heteroscedastic*<br>
  - Autoregressive : Current values are somehow related to recent past values.
  - Heteroscedastic : Variable that we are trying to model, may have different magnitudes of variability at different time points. Magnitude of variablity is measured using *variance*.

ARCH models can be expressed as : <br>

<br><img src="./images/8. ARCH.png" width=420 height=250></img><br><br>


* *GARCH : Generalised ARCH*
  - We can add terms to ARCH model to make current variance depended on previous estimates of variance. This is known as GARCH and can be expressed as :
  <br><br><img src="./images/9. GARCH.png" width=450 height=250></img><br><br>
  
  


