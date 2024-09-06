import pandas as pd
from pybaseball import statcast, team_batting
from datetime import datetime
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

    batting_data = team_batting(2024)

    if 'Team' in batting_data.columns:

        if 'Team' in batting_data.columns and team in batting_data['Team'].values:
            team_data = batting_data[batting_data['Team'] == str(team)]
            # Calculate the total hits and at-bats
            total_hits = team_data['H'].sum()
            total_at_bats = team_data['AB'].sum()

            # Calculate the batting average
            batting_average = total_hits / total_at_bats if total_at_bats > 0 else 0
            
            # Display the result
            return batting_average
        else:
            print("No Team Data")
    else:
        print("Team column error")


def team_obp_season(team):
    batting_data = team_batting(2024)

    if 'Team' in batting_data.columns:

        if 'Team' in batting_data.columns and team in batting_data['Team'].values:
            team_stats = batting_data[batting_data['Team'] == str(team)]
        else:
            return "No Team Data"
    else:
        return "No Team Column Found"
    
    hits_team = (team_stats['H'] + team_stats['BB'] + team_stats['HBP'])
    atbats_team = (team_stats['AB'] + team_stats['BB'] + team_stats['HBP'] + team_stats['SF'])
    OBP_team = hits_team / atbats_team

    return OBP_team



'''def team_stats_season(team, stat):'''