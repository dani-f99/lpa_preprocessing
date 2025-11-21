# Defining custom function to get frequences of surviving non-syn clones

import pandas as pd

def get_output(df,cname,prange,method):
    df_output = pd.DataFrame({"pos_aa":prange})
    total_unique = len(df["clone_id"].unique())
    temp_num = df.groupby("pos_aa").agg({"clone_id":"nunique"}).reset_index()
    
    if method == "freq_unique":
        temp_freq = pd.DataFrame({"pos_aa":temp_num["pos_aa"],cname:temp_num["clone_id"]/total_unique})
     
    elif method == "nunique_count":
        tfreq_df = df.groupby("pos_aa").agg({"clone_id":"nunique"}).rename({"clone_id":"freq"},axis=1).reset_index()
        temp_freq = pd.DataFrame({"pos_aa":tfreq_df["pos_aa"], cname:tfreq_df["freq"]})

    elif method == "nunique_weight":
        tfreq_df = df.groupby("pos_aa").agg({"clone_id":"nunique"}).rename({"clone_id":"freq"},axis=1).reset_index()
        tfreq_df["freq"] = tfreq_df.freq/tfreq_df.freq.sum()
        temp_freq = pd.DataFrame({"pos_aa":tfreq_df["pos_aa"], cname:tfreq_df["freq"]})
   
    elif method == "type_count":
        tfreq_df = df.groupby("chane_type").agg({"clone_id":"nunique"}).rename({"clone_id":"freq"},axis=1).reset_index()
        temp_freq = pd.DataFrame({"pos_aa":tfreq_df["pos_aa"], cname:tfreq_df["freq"]})
    
    elif method == "count":
        temp_freq = pd.DataFrame({"pos_aa":temp_num["pos_aa"],cname:temp_num["clone_id"]}) 
 
    df_output = df_output.merge(temp_freq, on="pos_aa", how="left")
    df_output.fillna(0,inplace=True)               
    return df_output