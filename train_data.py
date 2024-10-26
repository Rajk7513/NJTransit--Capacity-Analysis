def load_train_data(folder_path):
    """Load all JSON files from the given folder and return train data."""
    train_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            with open(os.path.join(folder_path, filename), 'r') as f:
                data = json.load(f)
                train_data.append(data)
    return train_data