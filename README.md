# rockies_moneyball_part-deux
DU AI Bootcamp Project 1.
Created by: Liz Cooney, Howard Dixon, Cassy Miller, & Sandokan Stage.
![Rockies Logo](https://upload.wikimedia.org/wikipedia/en/c/c0/Colorado_Rockies_full_logo.svg)
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

## Usage Instructions

To replicate or extend this analysis:

1. **Setup:** Install Python, Jupyter Notebook, and necessary libraries (including Pandas, requests, BeautifulSoup, Links,numpy,and matplotlib.pyplot.)
2. **Data:** Ensure access to relevant baseball reference files. 
3. **Code:** Refer to the provided Python scripts or notebooks for implementation details.
4. **Execution:** Run the code to analyze and visualize results.

## Conclusion
In conclusion, the Colorado Rockies expect to finish the remaining 28 games with a -----------------------------------------------------------------------------------------
