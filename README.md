# Havi Online Store Reports

This project contains three simple Python reports for the Havi Online Store MySQL database.

## Files Included

- `report1.py` - Product Information Report
- `report2.py` - Product Vendor Information Report
- `report3.py` - Product Lookup Report
- `Havi.sql` - Creates the Havi database and sample tables/data
- `setup_havi_user.sql` - Creates the MySQL user used by the reports

## Login Information

Use this login when running the reports:

```text
Username: havi_user
Password: havi_pass
Database: Havi
```

When the program asks for the username, you can press Enter to use the default username `havi_user`.

Do not type `havi_pass` as the username. `havi_pass` is the password.

## Before Running the Reports

These reports require:

- Python 3
- MySQL Server
- The Python MySQL connector package
- The `Havi` database already loaded in MySQL

If the database has not been created yet, run these commands from the project folder:

```bash
sudo mysql < Havi.sql
sudo mysql < setup_havi_user.sql
```

If the database already exists, you only need to run the report files.

## How to Run Report 1

Report 1 displays basic product information from the `Product` table.

Run:

```bash
python3 report1.py
```

Then enter:

```text
Username [havi_user]: havi_user
Password: havi_pass
```

This report displays:

- Product ID
- Product Name
- Price
- Stock Quantity

## How to Run Report 2

Report 2 displays information from more than one table. It joins the `Product` and `Vendor` tables.

Run:

```bash
python3 report2.py
```

Then enter:

```text
Username [havi_user]: havi_user
Password: havi_pass
```

This report displays:

- Product ID
- Product Name
- Vendor Name
- Vendor Contact
- Vendor Phone

The report uses an `INNER JOIN` so each product is shown with its matching vendor.

## How to Run Report 3

Report 3 is divided into two parts.

First, the program asks the user to enter a Product ID. Then it uses that Product ID to search the database and display the matching product information.

Run:

```bash
python3 report3.py
```

Then enter:

```text
Username [havi_user]: havi_user
Password: havi_pass
Enter Product ID: 12321
```

You can use any Product ID that exists in the database. Example Product IDs include:

- `12321`
- `12322`
- `12333`
- `34256`
- `65781`

This report displays:

- Product ID
- Product Name
- Price
- Stock Quantity
- Vendor Name
- Vendor Phone

If the Product ID does not exist, the report will display a message saying that no product was found.

## Common Problems

If you see this error:

```text
Access denied for user 'havi_pass'@'localhost'
```

It means the password was typed into the username field. Run the report again and use:

```text
Username: havi_user
Password: havi_pass
```

If you see a MySQL connection error, make sure MySQL Server is running and that the `Havi` database has been created.
