# Quant Workflow

## Overview

A hypothesis is an idea for a way to profit from trading. This hypothesis goes through a several phases of rigrous testing. After coming up with a hypothesis, next comes the research phase. In the research phase, we decide what set of positions to enter, on which assets and at what times in order to get positive future returns. After this phase, comes the testing phase which decides how much money to invest in each asset, in what conditions to exit positions and what are the risks. This is called *back-testing*.
<br><br><img src="./images/1. Quant workflow.png" width="420" height="250"></img><br><br>

## Types of Trading Strategies

### Single Asset Strategies

An example of *Single asset Strategy* is to just trade on S&P 500 and track its performance. If S&P 500 has been doing well for a while, then you might assume a long position assuming it has momentum.
<br><br><img src="./images/2. Single Asset Strategies.png" width="420" height="250"></img><br><br>

### Pairwise Strategies

Another strategy where you find pairs of assets that seem to be related and trade based on their relative movements. This is called *pair-wise strategy*.
<br><br><img src="./images/3. Pairwise Strategies.png" width="420" height="250"></img><br><br>

### Cross-sectional Strategies
Extending pairwise strategy, *cross-sectional strategy* extends this idea to groups of stocks. This type of strategy is also known as *equity statistical arbitrage, equity market neutral investing.* This strategy involves comparing hundreds and thousands of stocks to determine which ones to hold for long and short portfolios.
<br><br><img src="./images/4. Cross-sectional strategies.png" width="420" height="250"></img><br><br>

### Alternative Data Based Strategies
Class of strategies based on new type of data such as satelite imagery, social media, geolocation or consumer transaction data. 

## Anatomy of Strategy

Figure below describes an anatomy of strategies discussed in last topic.

<br><br><img src="./images/5. Anatomy of trading strategy.png" width="420" height="250"></img><br><br>

* In the first stage, decide which dataset(s) you want to use.
* In the second stage, *universe definition*, create your own sub-set of stocks (exclude the ones with less volume and include the ones that have similar features) with which you want to potentially trade. 
* *Alpha* is an expression that is applied at the cross-section over your universe of stocks that returns vector of real numbers whose *values are porpotional to the size of your position you will take on each asset.*
<br><br><img src="./images/6. Aplha defintion.png" width="420" height="250"></img><br><br>

Considering a cross-sectional momentum strategy, we rank the stocks based on their momentum and then decide which stocks to put in long portfolio and which one in short portfolio. In this case, *the logic producing the rank is alpha and ranks themselves are alpha vectors.*
<br><br><img src="./images/7. Alpha and alpha vector.png" width="420" height="250"></img><br><br>

* A *trading signal* is a numerical signal that informs the trade. For example *alpha*.
* In reality, it is usually not the case where a single alpha can be the sole basis of an investment strategy.
* *Model Stacking/Ensembling* is the term which represents combining several alphas to generate an *overall alpha* that has better performance than best individual alphas.
* Alphas can be combined using simple logic, for example combining price-driven alpha (momentum alpha) and alphas based on company's fundamental information.

<br><br><img src="./images/8. Combining alpha.png" width="420" height="250"></img><br><br>

* *Portfolio construction stage* is the stage where we think about using combined alpha vector to generate and update actual portfolio.
* The term *risk* in finance refers to the uncertainity or variablity in returns. There are various types of risks :
  * *Systematic Risks* : Risk inherent to the entire market.
    * Systematic risks contain another category of risks which are inherent to individual sectors like technology sector or energy sector. This risk is called *sector-specific risk*
  * *Idiosyncratic Risk* : Risks inherent to individual stocks.





