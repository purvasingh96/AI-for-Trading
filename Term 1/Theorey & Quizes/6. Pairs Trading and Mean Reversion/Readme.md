# Pairs Trading and Mean Reversion

## Mean Reversion

The two most popular types of trading strategies are momentum and mean reversion. A mean reversion trading strategy involves betting that *prices will revert back towards the mean or average.* Momentum predicts prices will continue in the same direction. 

A simplistic example of a mean reversion strategy is to buy a stock after it has had an unusually large fall in price. When a stock has seen a big drop, there’s usually a good chance that it will bounce back to a more normal level.

## Pairs Trading

Pairs Trading is a trading strategy that matches a long position in one stock/asset with an offsetting position in another stock/asset that is statistically related. Pairs Trading can be called a mean reversion strategy where we bet that the prices will revert to their historical trends.

<img src="./images/1. pairs trading.png" width=450 height=250></img>

### Spread and Hedge Ratio

A hedge ratio is the comparative value of an open position's hedge to the aggregate size of the position itself. It is expressed as a decimal or fraction and is used to quantify the amount of risk exposure one has assumed through remaining active in an investment or trade.

The formula for the hedge ratio is:
```
Hedge Ratio = Value of the Hedge / Total Position Value
```

To explain this, consider we have a long position in stock A and short position in stock B. The positons are in a certain propotion so that overall positon remains constant throughout the time. The propotion that helps us create this *neutral position* is called *hedge ratio.* Hedge ratio can be calculated as follows - <br>
<br><br><img src="./images/2. hedge ratio.png" width=350 height=200></img><br><br>

Spread can be calculated after we have the values for *hedge*:
<br><br><img src="./images/3. spread.png" width=350 height=200></img><br><br>
