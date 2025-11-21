# Creating custom function to pull metadata from metadata_df

import pandas as pd

def assign_metadata(sample_id, meta_df):
    meta_list = meta_df.columns[1:]
    meta_sample = meta_df.loc[meta_df["sample_id"]==sample_id, meta_list].values.flatten()
    return meta_sample