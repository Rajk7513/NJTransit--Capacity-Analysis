import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load the JSON files
with open('station_list.json') as f:
    station_list = json.load(f)

with open('station_messages.json') as f:
    station_messages = json.load(f)

with open('station_schedule.json') as f:
    station_schedule = json.load(f)

# Inspecting the station list
print(station_list[:5])  # First 5 entries

# Inspecting the station messages
print(station_messages[:5])  # First 5 messages

# Inspecting the station schedule
print(station_schedule[:5])  # First 5 schedules
