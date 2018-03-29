
import pandas as pd
import numpy as np
import feather
import pickle

data_path = '../../../mnt/ssd/kaggle-talkingdata2/competition_files/'


def decompose_date(df, date_col, drop = True):
    date = df[date_col]
    date = pd.to_datetime(date)
    df['hour'] = date.apply(lambda x: x.hour).astype(np.uint16)
    df['minute'] = date.apply(lambda x: x.minute).astype(np.uint32)
    df['second'] = date.apply(lambda x: x.second).astype(np.uint32)
    df['weekday'] = date.apply(lambda x: x.dayofweek).astype(np.uint8)
    
    if drop:
        df = df.drop(date_col, axis = 1)
    
    return df

def process_data(chunk):
    chunk = decompose_date(chunk, 'click_time', drop = True)
    chunk.drop('attributed_time', inplace= True, axis = 1)
    
    dtypes = {'ip': np.uint32, 'app': np.uint8, 
          'device': np.uint8, 'os': np.uint8, 
          'channel': np.uint32, 'is_attributed': bool}
    
    chunk = chunk.astype(dtype = dtypes)
    return chunk

def read_data(chunksize, path, filename):
    data_list = []
    i = 0
    for chunk in pd.read_csv(path + filename, chunksize=chunksize):
        chunk = process_data(chunk)
        data_list.append(chunk)
        i+=1
        if i % 10 == 0:
            print("Loop nbr {}".format(i))
            print("Loaded {} rows\n".format(i*chunksize))
            print(chunk.info())
    try:
        df = pd.concat(data_list)
        df.to_feather(path + "data.feather")
        
        with open(path + "data_list.pickle", 'wb') as f:
            pickle.dump(data_list, f)
        
        return df
    except:
        return data_list

data = read_data(chunksize = 10**6, path = data_path, filename = 'train.csv')

