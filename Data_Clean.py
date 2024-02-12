# Function to remove rows with missing values and columns with more than 10% missing values
def remove_missing_value(df):
    # Displaying the original shape of the Hotel dataset
    H_Shape = df.shape
    print(f"The shape of the original Hotel dataset is {H_Shape}") 

    # Identifying columns with missing values and printing the count of missing values for each
    missing_column_list = []
    missing_values = df.isnull().sum()
    for i in range(df.shape[1]):
        if missing_values[i] != 0:
            print("Missing Values:", missing_values.index[i], missing_values[i])
            missing_column_list.append(missing_values.index[i])

    # Calculating and displaying the percentage of missing values for each identified column
    missing_values = df[missing_column_list].isnull().sum()
    total_samples = len(df)
    missing_percentage = round(missing_values / total_samples * 100, 3)
    missing_percentage_with_sign = missing_percentage.astype(str) + '%'
    print(missing_percentage_with_sign, "\n")

    # Removing columns with more than 10% missing values
    high_missing_columns = missing_percentage[missing_percentage > 10].index
    original_rows, original_columns = df.shape
    df = df.drop(columns=high_missing_columns)
    new_rows, new_columns = df.shape
    columns_removed = original_columns - new_columns
    print(f"{columns_removed} columns were removed.")

    # Removing rows with any missing values
    df = df.dropna()
    new_rows, new_columns = df.shape
    rows_removed = original_rows - new_rows
    print(f"{rows_removed} rows were removed.")

    # Displaying the shape of the Hotel dataset after removal of missing rows and columns
    H_Shape = df.shape
    print(f"After removing those missing rows and columns, the shape of the Hotel dataset is {H_Shape}")

    return df

# Function to remove duplicate rows from the dataset
def remove_duplicates_data(df):
    # Counting and displaying the number of duplicated rows
    Dup_number = df.duplicated().sum()
    df.drop_duplicates(inplace=True)
    H_Shape = df.shape
    print(f"The Hotel dataset had {Dup_number} duplicated rows. After removing those duplicated rows, \nthe shape of the Hotel dataset is {H_Shape}")

    return df

# Function to remove rows where the counts of adults, children, and babies are all zero
def remove_zero_people_booking(df):
    # Filtering out rows where the counts of adults, children, and babies are all zero
    filter = (df.adults == 0) & (df.children == 0) & (df.babies == 0)
    df = df[~filter]
    H_Shape = df.shape
    print(f"After filtering out rows where the counts of adults, children, and babies are all zero, \nthe Hotel dataset has been streamlined to a new shape of {H_Shape}")

    return df
