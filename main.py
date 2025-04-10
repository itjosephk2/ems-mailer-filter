import pandas as pd

def scan_csv_fields(csv_path='ems_mailer_results.csv'):
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"File not found: {csv_path}")
        return
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    # Print the column names
    print("\n✅ Detected Columns in the CSV:")
    for col in df.columns:
        print(f" - {col}")

    # Optional: show the first few rows
    print("\n🔍 Sample Data:")
    print(df.head())

if __name__ == "__main__":
    scan_csv_fields()
