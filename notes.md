# Cheat Sheet: Importing Data Sets

| Package/Method | Description | Code Example |
|----------|-------------|--------------|
| Read CSV data set | Read the CSV file containing a data set into a pandas DataFrame. | ```python\n# Load without header\ndf = pd.read_csv(<CSV_path>, header=None)\n\n# Load using first row as header\ndf = pd.read_csv(<CSV_path>, header=0)\n``` |
| Print first few entries | Print the first few entries (default is 5) of the pandas DataFrame. | ```python\ndf.head(n)  # n = number of entries; default = 5\n``` |
| Print last few entries | Print the last few entries (default is 5) of the pandas DataFrame. | ```python\ndf.tail(n)  # n = number of entries; default = 5\n``` |
| Assign header names | Assign appropriate header names to the DataFrame. | ```python\ndf.columns = headers\n``` |
| Replace "?" with NaN | Replace the entries `"?"` with `NaN` from the NumPy library. | ```python\ndf = df.replace("?", np.nan)\n``` |
| Retrieve data types | Retrieve the data types of the DataFrame columns. | ```python\ndf.dtypes\n``` |
| Retrieve statistical description | Retrieve the statistical description of the dataset. By default, only numerical columns are included. Use `include="all"` for all variables. | ```python\ndf.describe()              # Default\n\ndf.describe(include="all") # All columns\n``` |
| Retrieve data set summary | Retrieve a summary of the dataset from the DataFrame. | ```python\ndf.info()\n``` |
| Save data frame to CSV | Save the processed DataFrame to a CSV file with a specified path. | ```python\ndf.to_csv(<output_CSV_path>)\n``` |

