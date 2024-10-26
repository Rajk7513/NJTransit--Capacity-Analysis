import json
import os
import numpy as np

def load_train_data(train_json_files):
    """Loads all JSON files from the given folder and returns a NumPy array of train data."""
    train_data = []
    for filename in os.listdir(train_json_files):
        if filename.endswith(".json"):
            with open(os.path.join(train_json_files, filename), 'r') as f:
                data = json.load(f)
                train_data.append(data)

    # Convert the list of dictionaries to a NumPy array
    train_data_np = np.array(train_data)

    return train_data_np