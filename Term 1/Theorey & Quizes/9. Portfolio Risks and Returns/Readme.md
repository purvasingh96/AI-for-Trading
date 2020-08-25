# Portfolio Risks and Returns

Consider a scenario where you are constructing a portfolio that comprises of 2 stocks -<br><br>

## Portfolio Variance
<img src="./images/1. portfolio variance.png" width=400 height=250></img><br><br>
The term *Cov* is covariance which is the measure of joint variablity of 2 random variables.

## Covariance
<img src="./images/3. correlation_coeff.png" width=450 height=250></img><br><br>

* *Covariance* is the correlation between the two variables times each of ther standard deviations.
* *Correlation coefficient* takes vallues between -1 and 1.

### When Covariance Coefficient is +1

<br><img src="./images/4. when ro +1.png" width=450 height=250></img><br><br>

### When Covariance Coefficient is -1

<br><img src="./images/5. when ro -1.png" width=450 height=250></img><br><br>

### Covariance 
*Screenshot taken by Udacity's Nanodegree program.*

<br><img src="./images/2. covariance matrix.png" width=450 height=650></img><br><br>

### Portfolio Return and Variance

<br><img src="./images/4. portfolio return and variance.png" width=400 height=250></img><br><br>

## Efficient Frontier

The efficient frontier for a given set of stocks gives us the set of portfolios that achieve the highest return for each level of risk. The efficient frontier also contains the set of portfolios that achieve the lowest level of risk for each level of return. We refer to these portfolios along the efficient frontier as market portfolios. As portfolio managers, we would be interested in finding the weights for each stock that create these market portfolios on the efficient frontier.<br><br>
<img src="./images/6. efficient frontier.png" width=400 height=250></img><br><br>

### Acheivable and Unacheivable Sides

<img src="./images/8. division.png" width=400 height=250></img><br><br>
The minimum variance portfolio is a single portfolio in the efficient frontier that has the lowest risk.

## Capital Market Line

The Capital Market Line is a graphical representation of all the portfolios that optimally combine risk and return. CML is a theoretical concept that gives optimal combinations of a risk-free asset and the market portfolio. The CML is superior to Efficient Frontier in the sense that it combines the risky assets with the risk-free asset.

<br><br><img src="./images/7. capital_market_line.png" width=400 height=250></img> <img src="./images/8. portfolio return.png" width=400 height=250></img><br><br>

*Slope of capital market line is called Sharpe Ratio.*

### Risk-free Assets
An asset that provides guarenteed rate of returns with no uncertainity. Usually entirely risk-free assets donot exist but rate of return on a 3 month treasury bill is called *risk-free rate.* 

### Sharpe Ratio

* The Sharpe ratio is the ratio of reward to volatility. It's a popular way to look at the performance of an asset relative to its risk.

<br><img src="./images/9. Sharpe ratio.png" width=370 height=80></img>

* The risk premium (which we’ll denote with _D_) equals the portfolio return minus risk free rate over a period of time:

<br><img src="./images/9. risk_premium.png" width=370 height=80></img>

* Then, calculate the mean and standard deviation of risk premium over the historical period from t=1 to T:

<br><img src="./images/10. final sharpe ratio.png" width=370 height=120></img>

* To convert the Sharpe ratio from daily to annual, we multiply by square root of 252 (number of trading days in a year)

<br><img src="./images/11. sharpe_ratio_year_to_day.png" width=370 height=60></img>

## Capital Asset Pricing Model
* The CAPM is a model that describes the relationship between systematic risk and expected return for assets. 
* The CAPM assumes that the excess return of a stock is determined by the market return and the stock’s relationship with the market’s movement. 
* It is the foundation of the more advanced multi-factor models used by portfolio managers for portfolio construction.
* β describes which direction and by how much a stock or portfolio moves relative to the market and can be calculated as :

<br><img src="./images/12. beta.png" width=340 height=200></img>


### Security Market Line
* The Security Market Line is the graphical representation of CAPM and it represents the relation between the risk and return of stocks. It is *not the same as Capital Market Line* as the y-axis is expected returns but the x-axis is beta.
* The Security Market Line is commonly used to evaluate if a stock should be included in a portfolio. 
* At time points when the stock is above the security market line, it is considered *undervalued* because the stock offers a greater return against its systematic risk. 
* In contrast, when the stock is below the line, it is considered *overvalued* because the expected return does not overcome the inherent risk.

<br><img src="./images/13. security market line.png" width=370 height=200></img>








