import os
import json

import pandas as pd


def read_json_with_json(path):
    with open(path) as f:
        # f = open('data.json')
        # returns JSON object as
        # a dictionary
        track_1_json = json.load(f)
    return track_1_json


def get_first_track_and_schema(track_index):
    in_path = f"django_data_engineering\\switchfoot_results\\track {track_index}.json"
    out_path = f"django_data_engineering\\csvs\\track {track_index}.csv"
# relative path
# path = ".\\track 1.json"
    track_df = pd.read_json(in_path)
    track_df.to_csv(out_path)
    return track_df


first_track_df = get_first_track_and_schema(1)
track_index = 2
for index in range(2, 15):
    # in_path = f"c:\\Users\\Stephen's PC\\Desktop\\desktopBin\\Programming resources\\data_engineering\\django_data_engineering\\switchfoot_results\\track {track_index}.json"
    in_path = f"django_data_engineering\\switchfoot_results\\track {track_index}.json"
    # relative path
    # path = ".\\track 1.json"
    is_valid = os.path.isfile(in_path)
    current_track_df = pd.read_json(in_path)
    first_track_df = pd.concat([first_track_df, current_track_df])
    track_index += 1
# out_path = f"django_data_engineering\\csvs\\track {track_index}.csv"
out_path = "django_data_engineering\\csvs\\album.csv"
first_track_df.to_csv(out_path)
#  working til here

# absolute path
# out_path = "c:\\Users\\Stephen's PC\\Desktop\\desktopBin\\Programming resources\\data_engineering\\django_data_engineering\\track 1.csv"

# print(track_1_df)
# print(track_1_df.to_string())
