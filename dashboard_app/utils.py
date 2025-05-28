def preprocess_data(df):
    df["Disaster Type"] = df["Disaster Type"].astype(str)
    df["Latitude"] = df["Latitude"].astype(float)
    df["Longitude"] = df["Longitude"].astype(float)
    return df