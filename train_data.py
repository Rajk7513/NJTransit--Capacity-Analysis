def load_train_data(train_json_files):
    """Load all JSON files from the given folder and return train data."""
    train_data = []
    for filename in os.listdir(train_json_files):
        if filename.endswith(".json"):
            with open(os.path.join(train_json_files, filename), 'r') as f:
                data = json.load(f)
                train_data.append(data)
    return train_data