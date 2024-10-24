import pandas as pd
from pybaseball import statcast, team_batting, team_batting_bref, schedule_and_record
from datetime import datetime
import sklearn as skl
import tensorflow as tf
"""Note: functions were developed with the assistance of ChatGPT"""




"""function calculates team batting average for a single game"""
def team_batting_avg(team, date):

    # Convert input date to string and ensure it's in the correct format
    game_date = pd.to_datetime(date).strftime('%Y-%m-%d')
    if pd.to_datetime(game_date) >= pd.to_datetime(datetime.today().strftime('%Y-%m-%d')):
        return -1
    else:
        try:
            # Pull all Statcast data for that date
            data = statcast(start_dt=game_date, end_dt=game_date, team=team)

            # Filter data for the specific team (e.g., New York Yankees)
            team_data = data

            # Calculate hits and at-bats
            # 'events' column can be used to determine hits ('single', 'double', 'triple', 'home_run')
            hits = team_data['events'].isin(['single', 'double', 'triple', 'home_run']).sum()
            at_bats = team_data['events'].isin(['single', 'double', 'triple', 'home_run', 'strikeout', 'field_out', 'grounded_into_double_play']).sum()

            # Calculate batting average
            batting_average = hits / at_bats if at_bats > 0 else 0
            return batting_average
        
        except Exception:
            return "error"


"""function calculates team's on base percentage per single game"""
def team_obp(team, date):

    # Define the date of the game
    game_date = pd.to_datetime(date).strftime('%Y-%m-%d')
    if pd.to_datetime(game_date) >= pd.to_datetime(datetime.today().strftime('%Y-%m-%d')):
        return -1
    else:
        try:
            # Pull all Statcast data for that date
            data = statcast(start_dt=game_date, end_dt=game_date, team=team)

            # Filter data for the specific team (e.g., Miami Marlins)
            team_data = data

            # Calculate components for OBP
            hits = team_data['events'].isin(['single', 'double', 'triple', 'home_run']).sum()
            walks = team_data['events'].isin(['walk']).sum()
            hit_by_pitch = team_data['events'].isin(['hit_by_pitch']).sum()
            at_bats = team_data['events'].isin(['single', 'double', 'triple', 'home_run', 'strikeout', 'field_out', 'grounded_into_double_play']).sum()
            sacrifice_flies = team_data['events'].isin(['sac_fly']).sum()

            # Calculate OBP
            obp = (hits + walks + hit_by_pitch) / (at_bats + walks + hit_by_pitch + sacrifice_flies) if (at_bats + walks + hit_by_pitch + sacrifice_flies) > 0 else 0
            return obp
        
        except Exception:
            return "error"


'''function calculates various team stats per single game. run this functioun multiple times with different stat names'''
def team_stats(team, date, stat_name):

    # Define the date of the game
    game_date = pd.to_datetime(date).strftime('%Y-%m-%d')
    if pd.to_datetime(game_date) >= pd.to_datetime(datetime.today().strftime('%Y-%m-%d')):
        return -1
    else:
        try:
            # Pull all Statcast data for that date
            data = statcast(start_dt=game_date, end_dt=game_date, team=team)

            # Filter data for the specific team (e.g., Miami Marlins)
            team_data = data

            # Calculate various stats
            hits = team_data['events'].isin(['single', 'double', 'triple', 'home_run']).sum()
            walks = team_data['events'].isin(['walk']).sum()
            at_bats = team_data['events'].isin(['single', 'double', 'triple', 'home_run', 'strikeout', 'field_out', 'grounded_into_double_play']).sum()
            home_runs = team_data['events'].isin(['home_run']).sum()
            strikeouts = team_data['events'].isin(['strikeout', 'strikeout_double_play']).sum()

            # return stat
            if stat_name == "hits":
                return hits
            elif stat_name == "walks":
                return walks
            elif stat_name == "at bats":
                return at_bats
            elif stat_name == "home runs":
                return home_runs
            elif stat_name == "strikeouts":
                return strikeouts
            else:
                return "UNKNOWN"
            
        except Exception:
            return "error"
        

'''calculate a team's batting average for the season so far'''
def team_ba_season(team):
    from mega import model_df

    if team == "COL":
        avg_ba_pergame = (model_df["COL_ba"].sum()) / (model_df["COL_ba"].count())
        return avg_ba_pergame
    else:
        team_stats = team_batting_bref(team, 2024)
        batting_avg_column = 'BA'        
        avg_obp_pergame_ba = team_stats[batting_avg_column].values[0]
        return avg_obp_pergame_ba


'''calculate a team's on base percentage average for the season so far'''
def team_obp_season(team, df):
    model_df = df.copy()

    if team == "COL":
        avg_obp_pergame = (model_df["COL_obp"].sum()) / (model_df["COL_obp"].count())
        return avg_obp_pergame
    else:
        team_stats = team_batting(2024)
        opp_team = team
        team_stats = team_stats[team_stats['Team'] == opp_team]
        avg_obp_pergame_opp = team_stats['OBP'].values[0]
        return avg_obp_pergame_opp



'''calculate a team's cumulative average statistic for the season so far'''
def team_avg_stats_pergame(team, stat, df):

    if team == "COL":
        model_df = df.copy()
        # at bat calcs
        avg_at_bats_pergame = (float(model_df["COL_at_bats"].sum())) / (float(model_df["COL_at_bats"].count()))
        # hits calcs
        avg_hits_per_game = (float(model_df["COL_hits"].sum())) / (float(model_df["COL_hits"].count()))
        # walks calcs
        avg_walks_per_game = (float(model_df["COL_walks"].sum())) / (float(model_df["COL_walks"].count()))
        # home runs calcs
        avg_hr_per_game = (float(model_df["COL_hr"].sum())) / (float(model_df["COL_hr"].count()))
        # strikeouts calcs
        avg_kk_per_game = (float(model_df["COL_kk"].sum())) / (float(model_df["COL_kk"].count())) 

        # return stat
        if stat == "hits":
            return avg_hits_per_game
        elif stat == "walks":
            return avg_walks_per_game
        elif stat == "at bats":
            return avg_at_bats_pergame
        elif stat == "home runs":
            return avg_hr_per_game
        elif stat == "strikeouts":
            return avg_kk_per_game
        else:
            return "COL STAT UNKNOWN"   
        
    else:
        team_stats = team_batting_bref(team, 2024)
        team_schedule = schedule_and_record(2024, team)
        games_played = len(team_schedule[team_schedule['Streak'].notnull()])

        # return stat
        if stat == "hits":
            stat_abb = "H"    
        
        elif stat == "walks":
            stat_abb = "BB"    

        elif stat == "at bats":
            stat_abb = "AB"    
        
        elif stat == "home runs":
            stat_abb = "HR"    
        
        elif stat == "strikeouts":
            stat_abb = "SO"    

        else:
            return "OPPONENT STAT UNKNOWN"  
        
        # get and clean stat data
        stat_pergame = pd.Series(team_stats[stat_abb])
        stat_pergame_df = pd.DataFrame(stat_pergame.head(21))
        stat_pergame_df = stat_pergame_df.reset_index(drop=True)

        # calculate average per game
        num_values = pd.to_numeric(stat_pergame_df[stat_abb], errors = 'coerce')
        total = num_values.sum()
        avg_pergame = total/games_played

        return avg_pergame


"""create function to hypertune the deep learning model - function below is modified from MOdule 18, Day 2 assignment 4"""
# Create a method that creates a new Sequential model with hyperparameter options
def create_model(hp):
    nn_model = tf.keras.models.Sequential()

    # Allow kerastuner to decide which activation function to use in hidden layers
    activation = hp.Choice('activation',['relu','tanh','sigmoid'])

    # Allow kerastuner to decide number of neurons in first layer
    nn_model.add(tf.keras.layers.Dense(units=hp.Int('first_units',
        min_value=1,
        max_value=10,
        step=2), activation=activation, input_dim=len(X_train.columns)))

    # Allow kerastuner to decide number of hidden layers and neurons in hidden layers
    for i in range(hp.Int('num_layers', 1, 6)):
        nn_model.add(tf.keras.layers.Dense(units=hp.Int('units_' + str(i),
            min_value=1,
            max_value=10,
            step=2),
            activation=activation))

    nn_model.add(tf.keras.layers.Dense(units=1, activation="sigmoid"))

    # Compile the model
    nn_model.compile(loss="binary_crossentropy", optimizer='adam', metrics=["accuracy"])

    return nn_model