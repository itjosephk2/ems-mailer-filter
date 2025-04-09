import pandas as pd

def find_probation_emails(csv_path='ems_mailer_results.csv'):
    # Load the CSV file
    df = pd.read_csv(csv_path)

    # Ensure the email fields are strings and lowercase for case-insensitive search
    df['EMAIL_BODY'] = df['EMAIL_BODY'].astype(str).str.lower()
    df['EMAIL_SUBJECT'] = df['EMAIL_SUBJECT'].astype(str).str.lower()

    # Filter for rows containing "probation" and either "90 days" or "ninety days"
    filtered = df[
        df['EMAIL_BODY'].str.contains('probation') & 
        (df['EMAIL_BODY'].str.contains('90 days') | df['EMAIL_BODY'].str.contains('ninety days'))
    ]


    # Show results or a message if none found
    if not filtered.empty:
        print("Emails mentioning 'probation' and '90 days':\n")
        print(filtered[['EMAIL_SUBJECT', 'EMAIL_BODY']])
    else:
        print("No emails found mentioning 'probation' and '90 days'.")

# Run the function
find_probation_emails()