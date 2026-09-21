import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    print("=" * 50)
    print("STEP 1 - DATA LOADED SUCCESSFULLY")
    print("=" * 50)
    print(f"Total Records : {len(df)}")
    print(f"Columns       : {list(df.columns)}")
    print("\nFirst 5 rows:")
    print(df.head())
    return df

def clean_data(df):
    print("\n" + "=" * 50)
    print("STEP 2 - DATA CLEANING")
    print("=" * 50)
    before = len(df)
    df.columns = df.columns.str.strip()
    df = df.drop_duplicates()
    df = df.fillna(0)
    df["Date"] = pd.to_datetime(df["Date"])
    after = len(df)
    print(f"Duplicate Rows Removed : {before - after}")
    print(f"Missing Values Filled  : Yes")
    print(f"Date Column Formatted  : Yes")
    print("Data Cleaned Successfully!")
    return df

def process_data(df):
    print("\n" + "=" * 50)
    print("STEP 3 - DATA PROCESSING")
    print("=" * 50)
    df["Total_Sales"] = df["Price"] * df["Quantity"]
    df["Month"] = df["Date"].dt.strftime("%B %Y")
    print("Total Sales Column Added!")
    print("Month Column Added!")
    print("\nProcessed Data:")
    print(df[["Product_Name","Price","Quantity","Total_Sales","Month"]])
    print("\nData Processed Successfully!")
    return df
