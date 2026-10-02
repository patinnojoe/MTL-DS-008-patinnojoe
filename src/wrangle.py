import pandas as pd



# load all excel files, set header and drop any columns with null all values 
def wrangle(filepath):
    df = pd.read_excel(filepath, header=13)
    df = df.dropna(axis=1, how='all')
    # extract the period from the file names and save to a new column
    period = filepath.stem.replace("incomplete_provider_", "")
    df['period'] = pd.to_datetime(period, format="%B_%Y")
    
    return df
    