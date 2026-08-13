# Havi Online Store Reports

This project contains three Python reports for the Havi Online Store MySQL database.

## Files

- `report1.py` - Product Information Report
- `report2.py` - Product Vendor Information Report
- `report3.py` - Product Lookup Report
- `Havi.sql` - Creates the database and sample data
- `setup_havi_user.sql` - Creates the MySQL user

## Requirements

- Python 3
- MySQL Server
- MySQL Connector for Python

Install the required Python package:

```bash
python3 -m pip install mysql-connector-python
```

## Database Setup

Run these commands from the project folder:

```bash
sudo mysql < Havi.sql
sudo mysql < setup_havi_user.sql
```

## Login

```text
Username: havi_user
Password: havi_pass
Database: Havi
```

## Report 1 - Product Information

Displays the product ID, name, price, and stock quantity.

```bash
python3 report1.py
```

## Report 2 - Product Vendor Information

Uses an `INNER JOIN` between the `Product` and `Vendor` tables to display product and vendor information.

```bash
python3 report2.py
```

## Report 3 - Product Lookup

Searches for a product using a Product ID.

```bash
python3 report3.py
```

Example input:

```text
Username [havi_user]: havi_user
Password: havi_pass
Enter Product ID: 12321
```
