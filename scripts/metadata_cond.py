# Custom function that creates matrix of all possible conditions across the metadata

import numpy as np
import pandas as pd

def metadata_cond(dic_input):
   
    mt_dic = dic_input
    mt_keys = mt_dic.keys()
    mt_keys_len = np.array([len(mt_dic[i]) for i in mt_keys])

    n_columns = len(mt_keys)
    n_rows = np.prod(mt_keys_len)
    meta_df = pd.DataFrame(np.zeros((n_rows,n_columns)), columns = mt_keys)

    for i,v,l in zip(range(0,len(mt_keys)), mt_keys, mt_keys_len):
        array_length = n_rows
        unique_val = v
        
        if i == 0:          
            reps_numbers = np.prod(mt_keys_len[i+1:])

            temp_array = []
            for val_i in mt_dic[unique_val]:
                temp_array+=[val_i for i in range(1,reps_numbers+1)]

            meta_df[v] = temp_array

        else:
            reps_numbers = np.prod(mt_keys_len[i+1:])
            temp_array = []
            
            for val_i in mt_dic[unique_val]:
                temp_array += [val_i for k in range(1,reps_numbers+1)]

            final_array = temp_array.copy()
            for num in range(1,int(array_length/len(temp_array))):
                final_array += temp_array.copy()

            meta_df[v] = final_array   
                
    return meta_df