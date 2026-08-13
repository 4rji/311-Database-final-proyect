"""Report 1 for the Havi Online Store database."""

from datetime import date
from getpass import getpass

try:
    import mysql.connector
except ModuleNotFoundError:
    print("Missing mysql connector. Run: amiga")
    raise SystemExit(1)


STUDENT_NAME = "Your Name"


def print_report(products):
    """Display the product report in a simple table."""
    print("\nHAVI ONLINE STORE")
    print(f"Student: {STUDENT_NAME}")
    print("Report 1 - Product Information")
    print(f"Date: {date.today().strftime('%m/%d/%Y')}")
    print("-" * 72)
    print(f"{'Product ID':<12}{'Product Name':<25}{'Price':>12}{'Stock':>12}")
    print("-" * 72)

    for product_id, product_name, price, stock_quantity in products:
        print(
            f"{product_id:<12}"
            f"{product_name:<25}"
            f"${price:>11.2f}"
            f"{stock_quantity:>12}"
        )

    print("-" * 72)
    print(f"Total products: {len(products)}")


def main():
    print("MySQL Login")
    username = input("Username [havi_user]: ").strip() or "havi_user"
    password = getpass("Password: ")

    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user=username,
            password=password,
            database="Havi",
        )
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT prod_code, prod_desc, prod_price, prod_quant
            FROM Product
            ORDER BY prod_code
            """
        )
        print_report(cursor.fetchall())
    except mysql.connector.Error as error:
        print(f"Database error: {error}")
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    main()
