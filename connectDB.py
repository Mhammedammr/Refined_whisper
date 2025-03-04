import pyodbc
import pandas as pd

# Define connection parameters
server = '10.24.105.209'  # Replace with your server IP or name
database = 'AMH.Env.HCMS.Prelive'  # Replace with your database name
username = 'readuser'  # Replace with your username
password = 'readP@ssw0rd'  # Replace with your password

# Create the connection string
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # Establish a connection
    conn = pyodbc.connect(conn_str)
    print("✅ Successfully connected to SQL Server!")

    # Define your SQL query
    query = """
    SELECT TOP 100 *  -- Replace with your table name and query
    FROM [CS].PatientClinicalSheet;  -- Replace with your schema and table name
    """

    # Load data into a pandas DataFrame
    df = pd.read_sql(query, conn)

    # Display the first few rows of the DataFrame
    print("Data extracted successfully:")
    print(df.head())

    # Optionally, save the data to a CSV file
    df.to_csv('extracted_data.csv', index=False)
    print("Data saved to 'extracted_data.csv'.")

    # Close the connection
    conn.close()

except pyodbc.Error as ex:
    print("❌ Connection failed:")
    print("SQLSTATE:", ex.sqlstate)
    print("Error message:", ex.args[1])
except Exception as e:
    print("❌ An unexpected error occurred:", e)