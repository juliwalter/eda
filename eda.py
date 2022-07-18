from eda.sub_df import * 

if __name__ == '__main__':
    # Read titanic test dataset
    df = pd.DataFrame(
        {
            'int': [1, 2, 3],
            'float': [1.1, 2.2, 3.3],
            'str': ['one', 'two', 'three'],
            'dt': [pd.datetime(2001,1,1), pd.datetime(2002,2,2), pd.datetime(2003,3,3)],
            'td': [pd.Timedelta(minutes=1), pd.Timedelta(minutes=2), pd.Timedelta(minutes=3)]
        }    
    )
    
    # Call functions for testing
    print('num -----------')
    print(extract_num(df))
    print('float -----------')
    print(extract_float(df))
    print('int -----------')
    print(extract_int(df))
    print('cat -----------')
    print(extract_cat(df))
    print('dates -----------')
    print(extract_dates(df))
