import pandas as pd

# ------------------------------------------------------------------------
# ------------------------ Numerical -------------------------------------
# ------------------------------------------------------------------------

def extract_float(df) -> pd.DataFrame:
    '''
    Extracts sub-DataFrame with float data only
    '''
    # Define float data
    float_types = ['float16', 'float32', 'float64']
    
    # return sub DataFrame where dtype is in float_types
    return df.select_dtypes(include=float_types)

def extract_int(df) -> pd.DataFrame:
    '''
    Extracts sub-DataFrame with int data only
    '''
    # Define float data
    int_types = ['int16', 'int32', 'int64']
    
    # return sub DataFrame where dtype is in int_types
    return df.select_dtypes(include=int_types)

def extract_num(df) -> pd.DataFrame:
    '''
    Extracts sub-DataFrame with numerical data only
    '''
    # Define float and int DataFrame
    _df_float = extract_float(df)
    _df_int = extract_int(df)
    
    _df_num = pd.merge(
        left=_df_float, 
        right=_df_int, 
        left_index=True,
        right_index=True,
    )
    
    # return sub DataFrame where dtype is in float_types
    return _df_num


# ------------------------------------------------------------------------
# ------------------------ Categorical -----------------------------------
# ------------------------------------------------------------------------

def extract_cat(df) -> pd.DataFrame:
    '''
    Extracts sub-DataFrame with categorical data only
    '''
    # Define categorical data
    cat_types = ['object', 'category', 'bool']
    
    # return sub DataFrame where dtype is in numerics
    return df.select_dtypes(include=cat_types)


# ------------------------------------------------------------------------
# ------------------------ Dates ----------------------------------------
# ------------------------------------------------------------------------

def extract_dates(df) -> pd.DataFrame:
    '''
    Extracts sub-DataFrame with date data only
    '''
    # Define categorical data
    date_types = ['datetime64', 'timedelta']
    
    # return sub DataFrame where dtype is in numerics
    return df.select_dtypes(include=date_types)