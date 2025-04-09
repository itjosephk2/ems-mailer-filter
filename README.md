# EMS Mailer Filter

This is a Python script designed to filter and display emails from a CSV file that reference **"probation"** and a **90-day period**. It helps teams identify automated messages about probationary periods for review, auditing, or debugging purposes.

---

## Features

-    Loads email data from a CSV file
-    Case-insensitive search in both subject and body
-    Filters for emails that mention:
     -    The word **"probation"**
     -    And either **"90 days"** or **"ninety days"**
-    Outputs matching email subjects and bodies to the console

---

## Project Structure

```
ems-mailer-filter/
├── script.py
├── ems_mailer_results.csv
├── README.md
└── venv/ (optional)
```

---

## Requirements

-    Python 3.7+
-    `pandas` library

Install `pandas` using pip:

```bash
pip install pandas
```

---

## How to Use the Project

### 1. Clone the repository

```bash
git clone https://github.com/itjosephk2/ems-mailer-filter.git
cd ems-mailer-filter
```

### 2. Place your CSV file

Ensure you have a CSV file named `ems_mailer_results.csv` in the project directory.

The file should contain at least two columns:

-    `Email Subject`
-    `Email Body`

If your column names are different, update them in `script.py`.

### 3. Run the script

```bash
python script.py
```

This will output any email records that mention "probation" and "90 days" or "ninety days".

---

## Sample Output

```
Emails mentioning 'probation' and '90 days':

   Email Subject                             Email Body
0  Welcome to the Team     Your probation period is 90 days from today.
1  Reminder: Probation     Just a quick reminder: ninety days probation applies.
```

If no matches are found, you'll see:

```
No emails found mentioning 'probation' and '90 days'.
```

---

## Troubleshooting

### KeyError: 'EMAIL_BODY'

Make sure the column names in your CSV match the ones used in the script. Use:

```python
print(df.columns)
```

...to inspect and update them accordingly.

---

## License

This project is for internal or personal use. No specific license is currently applied.

---

## Author

-    **Joseph Keane**
-    GitHub: [@itjosephk2](https://github.com/itjosephk2)
