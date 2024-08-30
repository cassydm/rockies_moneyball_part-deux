import pandas as pd
from pybaseball import statcast
"""Note: functions were developed with the assistance of ChatGPT"""

"""function calculates team batting average for a single game"""
def team_batting_avg(team, date):
    # Define the date of the game
    game_date = str(date)

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
    #print(f"Team Batting Average for {game_date}: {batting_average:.3f}")


"""function calculates team's on base percentage per single game"""
def team_obp(team, date):
    # Define the date of the game
    game_date = str(date)

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
    # print(f"Team OBP for {game_date}: {obp:.3f}")


'''function calculates various team stats per single game'''
def team_stats(team, date, stat_name):
    # Define the date of the game
    game_date = str(date)

    # Pull all Statcast data for that date
    data = statcast(start_dt=game_date, end_dt=game_date, team=team)

    # Filter data for the specific team (e.g., Miami Marlins)
    team_data = data

    # Calculate components for OBP
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
