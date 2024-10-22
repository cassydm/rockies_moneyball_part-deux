## Columns derived from pybaseball library: 
1. `pitch_type`: Type of pitch thrown (e.g., FF for four-seam fastball, SL for slider)
2. `game_date`: Date of the game
3. `release_speed`: Velocity of the pitch at release point (mph)
4. `release_pos_x`: Horizontal position of pitch at release (feet)
5. `release_pos_z`: Vertical position of pitch at release (feet)
6. `player_name`: Name of the pitcher
7. `batter`: MLB ID of the batter
8. `pitcher`: MLB ID of the pitcher
9. `events`: Outcome of the play (e.g., single, strikeout, home_run)
10. `description`: Detailed description of pitch result (e.g., ball, called_strike)
11. `spin_dir`: Direction of pitch spin (deprecated)
12. `spin_rate_deprecated`: Spin rate of the pitch (deprecated, use release_spin_rate)
13. `break_angle_deprecated`: Angle of pitch break (deprecated)
14. `break_length_deprecated`: Length of pitch break (deprecated)
15. `zone`: Strike zone location of the pitch
16. `des`: Description of play outcome
17. `game_type`: Type of game (e.g., R for regular season, P for playoffs)
18. `stand`: Batter's stance (L for left, R for right)
19. `p_throws`: Pitcher's throwing arm (L for left, R for right)
20. `home_team`: Home team's abbreviation
21. `away_team`: Away team's abbreviation
22. `type`: Classification of pitch (S for strike, B for ball, X for in play)
23. `hit_location`: Location where ball was hit (if applicable)
24. `bb_type`: Type of batted ball (e.g., ground_ball, fly_ball)
25. `balls`: Number of balls in the count
26. `strikes`: Number of strikes in the count
27. `game_year`: Year of the game
28. `pfx_x`: Horizontal movement of pitch (inches)
29. `pfx_z`: Vertical movement of pitch (inches)
30. `plate_x`: Horizontal position of pitch at home plate (feet)
31. `plate_z`: Vertical position of pitch at home plate (feet)
32. `on_3b`: MLB ID of runner on third base (if any)
33. `on_2b`: MLB ID of runner on second base (if any)
34. `on_1b`: MLB ID of runner on first base (if any)
35. `outs_when_up`: Number of outs when batter came to plate
36. `inning`: Inning number
37. `inning_topbot`: Top or bottom of the inning
38. `hc_x`: Hit coordinate X (horizontal position of batted ball)
39. `hc_y`: Hit coordinate Y (vertical position of batted ball)
40. `tfs_deprecated`: Time from start (deprecated)
41. `tfs_zulu_deprecated`: Time from start in Zulu time (deprecated)
42. `fielder_2`: MLB ID of the catcher
43. `umpire`: Home plate umpire's MLB ID
44. `sv_id`: Unique identifier for each pitch
45. `vx0`: Initial velocity of pitch in x-direction
46. `vy0`: Initial velocity of pitch in y-direction
47. `vz0`: Initial velocity of pitch in z-direction
48. `ax`: Acceleration of pitch in x-direction
49. `ay`: Acceleration of pitch in y-direction
50. `az`: Acceleration of pitch in z-direction
51. `sz_top`: Top of batter's strike zone
52. `sz_bot`: Bottom of batter's strike zone
53. `hit_distance_sc`: Projected hit distance (feet)
54. `launch_speed`: Exit velocity of batted ball (mph)
55. `launch_angle`: Launch angle of batted ball (degrees)
56. `effective_speed`: Perceived speed of pitch to batter
57. `release_spin_rate`: Spin rate of pitch at release (rpm)
58. `release_extension`: Extension of pitcher at release (feet)
59. `game_pk`: Unique identifier for the game
60. `pitcher.1`: Duplicate of pitcher MLB ID
61. `fielder_2.1`: Duplicate of catcher MLB ID
62. `fielder_3`: MLB ID of first baseman
63. `fielder_4`: MLB ID of second baseman
64. `fielder_5`: MLB ID of third baseman
65. `fielder_6`: MLB ID of shortstop
66. `fielder_7`: MLB ID of left fielder
67. `fielder_8`: MLB ID of center fielder
68. `fielder_9`: MLB ID of right fielder
69. `release_pos_y`: Forward distance of release point from mound
70. `estimated_ba_using_speedangle`: Estimated batting average based on launch speed and angle
71. `estimated_woba_using_speedangle`: Estimated weighted on-base average based on launch speed and angle
72. `woba_value`: Weighted on-base average value for the play
73. `woba_denom`: Denominator used in wOBA calculation
74. `babip_value`: Batting average on balls in play value
75. `iso_value`: Isolated power value
76. `launch_speed_angle`: Combined metric of launch speed and angle
77. `at_bat_number`: Number of the at-bat in the game
78. `pitch_number`: Number of the pitch in the at-bat
79. `pitch_name`: Full name of the pitch type
80. `home_score`: Home team's score before the play
81. `away_score`: Away team's score before the play
82. `bat_score`: Batting team's score before the play
83. `fld_score`: Fielding team's score before the play
84. `post_away_score`: Away team's score after the play
85. `post_home_score`: Home team's score after the play
86. `post_bat_score`: Batting team's score after the play
87. `post_fld_score`: Fielding team's score after the play
88. `if_fielding_alignment`: Infield fielding alignment (e.g., Standard, Shift)
89. `of_fielding_alignment`: Outfield fielding alignment (e.g., Standard, Strategic)
90. `spin_axis`: Axis of pitch spin (degrees)
91. `delta_home_win_exp`: Change in home team's win expectancy
92. `delta_run_exp`: Change in run expectancy
93. `bat_speed`: Speed of bat at contact (if available)
94. `swing_length`: Length of batter's swing (if available)

## The following columns were created by the team: 
95. `pitch_count` - (int) running total of pitches by that particular player in a single game
96. `trailing_pitch` - (str) the type of pitch that was previously thrown against the current batter up. 