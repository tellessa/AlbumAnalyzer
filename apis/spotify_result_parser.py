import os
import json

import pandas as pd

# is_valid = os.path.isfile("../switchfoot_results/track 1.json")
in_path = "c:\\Users\\Stephen's PC\\Desktop\\desktopBin\\Programming resources\\data_engineering\\django_data_engineering\\track 1.json"
# path = ".\\track 1.json"
is_valid = os.path.isfile(in_path)
# how do we load json from a file with json library?

# Opening JSON file


def read_json_with_json(path):
    with open(path) as f:
        # f = open('data.json')
        # returns JSON object as
        # a dictionary
        track_1_json = json.load(f)
    return track_1_json

# track_1_json = read_json_with_json(path)

#  working til here

# absolute path
# out_path = "c:\\Users\\Stephen's PC\\Desktop\\desktopBin\\Programming resources\\data_engineering\\django_data_engineering\\track 1.csv"


track_1_df = pd.read_json(in_path)
# relative path
out_path = "django_data_engineering\\track 1 b.csv"
track_1_df.to_csv(out_path)
# print(track_1_df)
# print(track_1_df.to_string())
