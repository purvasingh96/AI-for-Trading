# Alpha Factor Research Methods

## Research Paper 1 : [Overnight Returns and Firm-Specific Investor Sentiment](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2554010)

[Download Paper](https://github.com/purvasingh96/AI-for-Trading/blob/master/Term%201/Theorey%20%26%20Quizes/16.%20Alpha%20Factor%20Research%20Methods/Research%20Papers/Overnight%20Returns%20and%20Firm-Specific%20Investor%20Sentiment.pdf)

### Abtract
We explore the possibility that overnight returns can serve as a measure of firm-specific investor sentiment by analyzing whether they exhibit characteristics expected of a sentiment measure. First, we document short-term persistence in overnight returns, consistent with existing evidence of short-term persistence in share demand of sentiment-influenced retail investors. Second, we find that short-term persistence is stronger for harder-to-value firms, consistent with evidence that sentiment plays a larger role when there is less objective data available for valuation. Third, we show that stocks with high (low) overnight returns underperform (outperform) over the longer-term, consistent with evidence of temporary sentiment-driven mispricing.  

### p 1
The recent work of Berkman, Koch, Tuttle, and Zhang (2012) suggests that a stock’s
overnight (close-to-open) return can serve as a measure of firm-level sentiment.

### p 2
Specifically, Berkman et al. (2012) find that attention-generating events (high absolute returns or
strong net buying by retail investors) on one day lead to higher demand by individual investors,
concentrated near the open of the next trading day...This creates temporary price pressure at the
open, resulting in elevated overnight returns that are reversed during the trading day.

### p 3
We conduct three sets of analyses. **In the first
we test for short-run persistence in overnight returns.** The basis for expecting this from a
measure of sentiment is the evidence in Barber et al. (2009) that the order imbalances of retail
investors, who are the investors most likely to exhibit sentiment, persist for periods extending
over several weeks...In the third analysis we
examine whether stocks with high overnight returns underperform those with low overnight
returns over the long term.

Exercise on overnight returns can be found [here](https://github.com/purvasingh96/AI-for-Trading/blob/master/Term%201/Theorey%20%26%20Quizes/16.%20Alpha%20Factor%20Research%20Methods/Quizzes/overnight_returns.ipynb)

## Research Paper 2 : [The Formation Process of Winners and Losers in Momentum Investing](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2610571)

[Download Paper](https://github.com/purvasingh96/AI-for-Trading/blob/master/Term%201/Theorey%20%26%20Quizes/16.%20Alpha%20Factor%20Research%20Methods/Research%20Papers/The%20Formation%20Process%20of%20Winners%20and%20Losers%20in%20Momentum%20Investing.pdf)

### Abstract:
Previous studies have focused on which stocks are winners or losers but have paid little attention to the formation process of past returns. This paper develops a model showing that past returns and the formation process of past returns have a joint effect on future expected returns. The empirical evidence shows that the zero-investment portfolio, including stocks with specific patterns of historical prices, improves monthly momentum profit by 59%. Overall, the process of how one stock becomes a winner or loser can further distinguish the best and worst stocks in a group of winners or losers.

<img src="./Images/1. trajectory.png" width=450 height=300></img> <img src="./Images/2. relative trajectory.png" width=450 height=300></img>

### p. 1
Intermediate-term (3–12 months) momentum has been documented by Jegadeesh and Titman (1993, 2001, hereafter JT), while short-term (weekly) and long-term (3–5 years) reversals have been documented by Lehmann (1990) and Jegadeesh (1990) and by DeBondt and Thaler (1985), respectively. Various models and theories have been proposed to explain the coexistence of intermediate-term momentum and long-term reversal. However, most studies have focused primarily on which stocks are winners or losers; they have paid little attention to how those stocks become winners or losers. This paper develops a model to analyze whether the movement of historical prices is related to future expected returns.

<img src="./Images/3. convex cocave formula.png" width=250 height=300></img>

### p. 2
This paper captures the idea that past returns and the formation process of past returns have a joint effect on future expected returns. We argue that how one stock becomes a winner or loser—that is, the movement of historical prices—plays an important role in momentum investing. Using a polynomial quadratic model to approximate the nonlinear pattern of historical prices, the model shows that as long as two stocks share the same return over the past n-month, the future expected return of the stock whose historical prices are convex shaped is not lower than one whose historical prices are concave shaped. In other words, when there are two winner (or loser) stocks, the one with convex-shaped historical prices will possess higher future expected returns than the one with concave-shaped historical prices.

<img src="./Images/4. graphs - 1.png" width=450 height=300></img> <img src="./Images/5. graphs - 2.png" width=450 height=300></img>

### p. 3 
To test the model empirically, we regress previous daily prices in the ranking period on an ordinal time variable and the square of the ordinal time variable for each stock. The coefficient of the square of the ordinal time variable is denoted as gamma. Exercise notebook for regression against time can be found [here](https://github.com/purvasingh96/AI-for-Trading/blob/master/Term%201/Theorey%20%26%20Quizes/16.%20Alpha%20Factor%20Research%20Methods/Quizzes/regression_against_time.ipynb)

<img src="./Images/6. gain and accelerate.png" width=250 height=300></img> <img src="./Images/7. gain acc alpha.png" width=250 height=300></img>

## Research Paper 3 : [Expected Skewness and Momentum](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2600014)

[Download Paper](https://github.com/purvasingh96/AI-for-Trading/blob/master/Term%201/Theorey%20%26%20Quizes/16.%20Alpha%20Factor%20Research%20Methods/Research%20Papers/Expected%20Skewness%20and%20Momentum.pdf)

### Abstract:
Motivated by the time-series insights of Daniel and Moskowitz (2016), we investigate the link between expected skewness and momentum in the cross-section. The alpha of skewness-enhanced (-weakened) momentum is about twice (half) as large as the traditional alpha. These findings are driven by the short leg. Portfolio sorts, Fama-MacBeth regressions, and the market reaction to earnings announcements suggest that expected skewness is an important determinant of momentum. Due to the simplicity of the approach, its economic magnitude, its existence among large stocks, and the success of risk management, the results are difficult to reconcile with the efficient market hypothesis.

<img src="./Images/8. skews.png" width=450 height=300></img> <img src="./Images/9. momentum and skew.png" width=250 height=300></img>

### Momentum and Skew as Joint Alpha Factor

<img src="./Images/10. skew momentum joint factor.png" width=450 height=300></img>

### p1
In this paper, we comprehensively explore a new dimension in firm-level momentum profitability. More precisely, we document a strong relation between expected idiosyncratic skewness and cross-sectional momentum profits, in particular with respect to past loser stocks. The impact of skewness is economically large, statistically highly significant, holds among large firms, in international markets, and after controlling for a large set of firm characteristics previously linked to momentum profitability (e.g., past returns, idiosyncratic volatility, continuously arriving information, credit ratings).

### p2
Based on this thought, momentum should be particularly pronounced if losers (winners) have a strong (weak) positive skew. Conversely, high (low) positive skewness on the winner (loser) leg is expected to reduce the profitability of momentum.

### p3
As a proxy for expected skewness, our baseline analysis relies on the measure proposed by Bali et al. (2011) because of its simplicity, its economic persuasiveness, and its ability to predict realized skewness. It is calculated as the maximum daily return during the preceding month.


## Reseacrh Paper 4 : [Arbitrage Asymmetry and the Idiosyncratic Volatility Puzzle](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2155491) 

[Download Paper](https://github.com/purvasingh96/AI-for-Trading/blob/master/Term%201/Theorey%20%26%20Quizes/16.%20Alpha%20Factor%20Research%20Methods/Research%20Papers/Arbitrage%20Asymmetry%20and%20the%20Idiosyncratic%20Volatility%20Puzzle.pdf)

### Abstract
Many investors purchase stock but are reluctant or unable to sell short. Combining this arbitrage asymmetry with the arbitrage risk represented by idiosyncratic volatility (IVOL) explains the negative relation between IVOL and average return. The IVOL-return relation is negative among overpriced stocks but positive among underpriced stocks, with mispricing determined by combining 11 return anomalies. Consistent with arbitrage asymmetry, the negative relation among overpriced stocks is stronger, especially for stocks less easily shorted, so the overall IVOL-return relation is negative. Further supporting our explanation, high investor sentiment weakens the positive relation among underpriced stocks and, especially, strengthens the negative relation among overpriced stocks.

### p1
Here we use the famous value factor which is described in many place (e.g., Value and Momentum Everywhere http://pages.stern.nyu.edu/~lpederse/papers/ValMomEverywhere.pdf): p. 8 "For individual stocks, we use the common value signal of the ratio of the book value of equity to market value of equity, or book-to-market ratio,"; in this study we use the Sharadar ratio Price/Book. We use this as an anomaly to create a refined factor as described in the "Arbitrage Asymmetry and the Idiosyncratic Volatility Puzzle". p. 2 This study presents an explanation for the observed negative relation be- tween IVOL and expected return. We start with the principle that [idiosyncratic volatility] IVOL rep- resents risk that deters arbitrage and the resulting reduction of mispricing. In keeping with previous literature, we refer to risk that deters arbitrage as arbi- trage risk.3 We then combine this familiar concept with what we term arbitrage asymmetry: many investors who would buy a stock they see as underpriced are reluctant or unable to short a stock they see as overpriced.

### p2
Combining the effects of arbitrage risk and arbitrage asymmetry implies the observed negative relation between IVOL and expected return. To see this, first note that stocks with greater IVOL, and thus greater arbitrage risk, should be more susceptible to mispricing that is not eliminated by arbitrageurs [my emphasis added]. Among overpriced stocks, the IVOL effect in expected return should therefore be negative—those with the highest IVOL should be the most overpriced.

### p3
We compute individual stock IVOL, following Ang et al. (2006), as the stan- dard deviation of the most recent month’s daily benchmark-adjusted returns.




