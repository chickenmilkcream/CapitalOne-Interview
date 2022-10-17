# Running in Pycharm
- Run `pip install -r requirements.txt`.  
- Go to `main.py`.  
- Right click, and select "Run File in Python Console".  
- Enter the transaction file path.  

# Solution
Followed this article:  
- https://mlabonne.github.io/blog/linearoptimization/
- https://mlabonne.github.io/blog/integerprogramming/

Generalized the problem into the following linear program:  

```{python}
Maximize points = rule1 * 500 + rule2 * 300 + rule3 * 200 + rule4 * 150 + rule5 * 75 + rule6 * 75
Subject to        
        75 * rule1 + 75 * rule2 + 75 * rule3 + 25 * rule4 + 25 * rule5 + 20 * rule6 <= Total spent on SportCheck
        25 * rule1 + 25 * rule2 + 10 * rule4 + 10 * rule5 <= Total spent on TimHortons
        25 * rule1 + 10 * rule4 <= Total spent on Subway
        rule1 to rule6 >= 0
        rule1 to rule6 are integers
```
Note the variables represent how many times to apply the rule.
After the optimization is finished, I take the remainder of money left and apply Rule 7.
- "Rule 7: 1 points for every $1 spend for all other purchases (including leftover amount)"
