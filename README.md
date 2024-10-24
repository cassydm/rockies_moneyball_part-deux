# rockies_moneyball_part-deux
DU AI Bootcamp Project 1, 2 and 3.
Created by: Liz Cooney, Howard Dixon, Cassy Miller, & Sandokan Stage.
![Rockies Logo](https://upload.wikimedia.org/wikipedia/en/c/c0/Colorado_Rockies_full_logo.svg)

# Contents:
> Project 1: Moneyball  
> Project 2: Machine Learning  
> Project 3: Neural Networks and Transformers



# Project 1: Exploratory Data Analysis, "Moneyball Part Deux"

## Overview

This analysis seeks to rejuvenate the Colorado Rockies by applying a "Moneyball" strategy, which involves a rigorous statistical analysis comparing the current players' performance metrics with those of the 2007 World Series team. By meticulously evaluating player statistics and identifying critical performance indicators, we aim to pinpoint strengths and weaknesses in the current lineup. Through this process, we will recommend targeted changes such as potential trades or acquisitions to optimize team composition and improve overall performance. 

Our objective is to strategically position the Rockies for a return to the World Series, drawing on historical successes of the 2007 team and modern analytics to guide our decisions. With a focus on continuous monitoring and adaptive strategies, we envision a revitalized team that excels in the competitive landscape of Major League Baseball.


## Data Overview

Data was collected for the Rockies 2007 and 2024 rosters from Baseball Reference resource online. The team both scraped tables from the website and downloaded excel documents to perform our analysis. 

The team took a 4-pronged approach to dividing and reviewing the data. Each team member looked at a specific subset of player statistics, including batting, pitching, and fielding. Additionally our team looked at appearance and salary data to help us determine whether certain players contribute their “worth”  to the Rockies. 

Each team member performed several statistical analysis and visualizations to better understand how the 2007 and 2024 teams performed relative to each other and identify areas for the 2024 Rockies to improve. 

## Questions to Answer

1. How do the batters in 2024 compare to 2007, and what needs to change in order to improve the team?

2. How do Starting Pitchers, Relief Pitchers, and Closing Pitchers in 2024 compare to the 2007 roster, and what needs to change in order to improve the team?

3. How do does the Rockies fielding compare between the 2007 and 2024 seasons?

4. What changes should be made to the 2024 Rockies player roster to get them to the World Series?

## Usage Instructions

To replicate or extend this analysis:

1. **Setup:** Install Python, Jupyter Notebook, and necessary libraries (including Pandas, requests, BeautifulSoup, Links,numpy,and matplotlib.pyplot.)
2. **Data:** Ensure access to relevant baseball reference files. 
3. **Code:** Refer to the provided Python scripts or notebooks for implementation details.
4. **Execution:** Run the code to analyze and visualize results.

## Analysis

### Batting
The 2024 Rockies team struggles heavily with their On Base Percentage (OBP), which is a very important stat when it comes to Moneyball Statistics. 2007 players at the Left Field, Right Field and Short Stop positions outpaced the players in 2024 in OBP, RBIs (Runs Batted in), and other important metrics. 

*Recommendation:*  
This analysis walks through a varaiety of those and identifies the batters who play LF, RF, and SS as areas of improvement when it comes to improving the Rockies record this season in hopes of a World Series push in the future.

### Pitching
2007 pitching roster out-performed the 2024 team in terms of preventing earned runs, striking-out batters and reducing the number of walks. 2024 closing pitchers and relief pitchers performed worse relative to the 2007 roster. 2024 starting pitchers showed fewer deficiencies regarding Home Runs Allowed, ERA and Strike-out to Ball Ratio. 

*Recommendation:*  
*Improving ERA and K/BB Ratio, while focusing on identifying CL and RP players for trades*

### Fielding
The 2007 Colorado Rockies team did out perform the 2024 team in terms of overall team fielding percentage and assist. There is a significant difference in the team fieling percentage for the left field postion.

*Recommendation:*  
*Improving fielding percentage for left field position, while focusing on identifying possible trades for this position*
### Performance vs. Salary
Boxplot of Salary vs. WAR by Year:
1. 2007 Data:
    1. Salaries: Generally lower compared to 2024.
    2. WAR Values: More evenly distributed, with fewer outliers and a balanced spread across the roster.
    3. Callouts: Most players were likely paid less but contributed a solid performance to the team. The 2007 roster made it to the World Series, indicating a good return on investment.
2. 2024 Data:
    1. Salaries: Noticeably higher overall.
    2. WAR Values: Higher variability with more significant outliers, indicating some players have much higher or lower performance compared to others.
    3. Callouts: Some high-paid players have low WAR, indicating overpayment and underperformance. Conversely, there may be underpaid but highly performing players, showing possible inefficiencies in salary allocation.

Clustering Analysis: 2007 and 2024 Roster Comparison

1. 2007 Data:
    1. Cluster 1: Low salary, high WAR
        1. Players in this cluster are underpaid but highly performing. These players provide excellent value and are crucial to the team's success.
        2. Action: Recognize these players and consider future salary adjustments to retain their talent.
    2. Cluster 2: Low salary, low WAR
        1. Players in this cluster are both underpaid and underperforming. These players might be younger or less experienced, contributing less to the team's success.
        2. Action: Monitor their development and consider training or potential trades if performance doesn't improve.
    3. Cluster 3: High salary, high WAR
        1. Players in this cluster are paid well and perform well, indicating fair compensation for their contributions.
        2. Action: Maintain and support these players as they are valuable assets to the team.

2. 2024 Data:
    1. Cluster 1: Low salary, high WAR
        1. Similar to 2007, these players are underpaid but highly performing. They provide excellent value and are critical to the team's success.
        2. Action: Consider renegotiating contracts to ensure they stay with the team and continue performing well.
    2. Cluster 2: High salary, low WAR
        1. Players in this cluster are overpaid and underperforming. They represent inefficiencies in salary allocation and do not contribute as expected.
        2. Action: Evaluate the reasons for their underperformance and consider trades or releases to free up salary for more effective players.
    3. Cluster 3: High salary, high WAR
        1. These players are both highly paid and high performing, indicating fair compensation and valuable contributions to the team.
        2. Action: Maintain and support these players, ensuring they continue to perform at a high level.

Analysis of the Heatmap of Average WAR by Position and Year
    1. Decline in Pitching Performance:
        1. The significant decrease in average WAR for pitchers in 2024 compared to 2007 is concerning. Addressing this decline should be a priority, potentially through trades, drafting, or training.
    2. Weakness in Infield:
        1. The drop in WAR values for infield positions in 2024 highlights a potential area of weakness. Strengthening these positions through targeted acquisitions or player development can help improve the team's overall performance.
    3. Stable Outfield Performance:
        1. The outfield positions have maintained relatively stable performance levels, which is a positive sign. Continuing to support and develop these players will ensure this remains a strength for the team.
    4. Improvement in Catcher Position:
        1. The slight improvement in WAR for the catcher position in 2024 indicates progress. Ensuring continued development and support for catchers will be beneficial.


## Conclusion
In conclusion, the 2024 Rockies are struggling in a variety of key metrics that were much better during their 2007 World Series Campaign. The Rockies need to look at their Left and Right Field as well as their closing and relief pitchers and reassess their value on the team.


DU AI Bootcamp Project 2.
Created by: Liz Cooney, Howard Dixon, Cassy Miller, & Sandokan Stage.

# Project 2:  Predicting the Rockies 2024 remaining season using Machine Learning Models, ​"Moneyball Part Deux"

## Overview
This proposal seeks to continue our Money Ball analysis with the Colorado Rockies by using ML to predict the remaining 2024 season. 

Data was cleansed and prepped to be used in six different Machine Learing Models. The team downloaded excel documents to perform our analysis and leveraged pystats to scrape the website.

The team took a 6-pronged approach to utilize the ML model for Project 2.  Each team member looked at the same final datase (model_df). 

Each team member performed scaling of the dataset, applied the model, and provided visualizations to better understand how well each model did against the relevant input. 

## Question to Answer

1. How will the Colorado Rockies perform the rest of the season?

## Machine Learning Models
Tree-Based Models:​

1. Decision Trees: Used to explore the branching possibilities of game outcomes based on specific conditions (e.g., opponent strength, game location). This model provides a clear, visual representation of how       different factors contribute to winning or losing.​

2. Random Forests: An ensemble method that aggregates multiple decision trees to improve prediction accuracy. This model is particularly useful for capturing more nuanced relationships between variables and generalizing well across different scenarios.​

Regression Models:​

3. Linear Regression: Applied to identify linear relationships between game metrics (like hits or home runs) and outcomes. This model helped establish a baseline understanding of how individual variables impact performance.​

4. Logistic Regression: Used to model the probability of categorical outcomes (win or loss). This approach provides a probabilistic perspective, estimating the likelihood of various game results based on historical data.​

Advanced and Proximity-Based Models:​

5. Support Vector Machines (SVM): Employed to handle more complex, non-linear relationships by finding the optimal boundary that separates different classes (win or loss). SVM is particularly effective in distinguishing outcomes when data points are not linearly separable.​

6. K-Nearest Neighbors (KNN): Used for its intuitive approach to predicting outcomes based on the similarity of past games. KNN relies on proximity, comparing current games with similar historical games to make predictions.​
## Usage Instructions

To replicate or extend this analysis:

1. **Setup:** Install Python, Jupyter Notebook, and necessary libraries (including Pandas, requests, pybaseball, numpy, and matplotlib.pyplot).  
2. **Data:** Ensure access to relevant baseball reference csv files. The model_df dataframe was leveraged from the mega.py file, which was the foundation for all the models.
4. **Code:** Refer to the provided Python scripts or notebooks for implementation details.
5. **Execution:** Run the code to analyze and visualize results.

## Conclusion
The majority of the models did not perform well for predicting wins and losses. The method has a large flaw in using average season data for unplayed games which limits the usefulness of a model to very few factors, that don't necessarily contribute heavily to the outcome of a game like the statistics. In the future, it would be better to analyze player level information or use statistics to predict other factors besides wins and losses. Available data for future games is limited and there is not enough nuance to differentiate win/loss outcomes when the same team matchups perform back-to-back.

DU AI Bootcamp Project 3. Created by: Liz Cooney, Howard Dixon, Cassy Miller, & Sandokan Stage.

# Project 3:  Colorado Rockies Pitch App, "Moneyball Part III, The Trilogy"

## Overview
This proposal seeks to develop an innovative app for the Colorado Rockies that leverages advanced analytics and ML —specifically utilizing transformer models in Python—to revolutionize pitching strategy.  

Data was cleansed and prepped to be used with Gradio, which allowed us to set up web-based interfaces to showcase our  model. The team downloaded existing Excel documents to compile information on the various Rockies pithchers and perform our analysis.

The team took a 6-pronged approach to utilize the ML model for Project 3.  Each team member looked at the same final datase (model_df). 

Each team member performed scaling of the dataset, applied the model, and provided visualizations to better understand how well each model did against the relevant input. 

## Question to Answer

1. What pitch type should the pitcher throw?

## Neural Network Models
Recurrent Neural Networks (RNN):​

1. LSTM (Long Short-Term Memory): Designed to remember information for long periods, often used in language modeling.
2. GRU (Gated Recurrent Unit): A simplified version of LSTM that is computationally efficient while maintaining performance.  
   
Transformers:​

3. BERT (Bidirectional Encoder Representations from Transformers): Used for a variety of NLP tasks, focuses on understanding context.
4. GPT (Generative Pre-trained Transformer): A model designed for generating human-like text based on prompts​

## Usage Instructions

To replicate or extend this analysis:

1. **Setup:** Install Python, Jupyter Notebook, and necessary libraries (including Pandas, requests, pybaseball, nump, gradio and LangChain and it's various components).  
2. **Data:** Ensure access to relevant baseball reference csv files. The pitchers_df dataframe was leveraged from the five (5) Colorado starting pitchers data frames , which was the foundation for all the models.
4. **Code:** Refer to the provided Python scripts or notebooks for implementation details.
5. **Execution:** Run the code to analyze and visualize results.

## Conclusion
