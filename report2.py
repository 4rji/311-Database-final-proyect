"""Report 2 for the Havi Online Store database."""

from datetime import date
from getpass import getpass

try:
    import mysql.connector
except ModuleNotFoundError:
    print("Missing mysql connector. Run: amiga")
    raise SystemExit(1)


STUDENT_NAME = "Your Name"


def print_report(products):
    """Display product and vendor information in a simple table."""
    print("\nHAVI ONLINE STORE")
    print(f"Student: {STUDENT_NAME}")
    print("Report 2 - Product Vendor Information")
    print(f"Date: {date.today().strftime('%m/%d/%Y')}")
    print("-" * 86)
    print(
        f"{'Product ID':<12}"
        f"{'Product Name':<20}"
        f"{'Vendor':<20}"
        f"{'Contact':<18}"
        f"{'Phone':>12}"
    )
    print("-" * 86)

    for product_id, product_name, vendor_name, vendor_contact, vendor_phone in products:
        print(
            f"{product_id:<12}"
            f"{product_name:<20}"
            f"{vendor_name:<20}"
            f"{vendor_contact:<18}"
            f"{vendor_phone:>12}"
        )

    print("-" * 86)
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
            SELECT
                Product.prod_code,
                Product.prod_desc,
                Vendor.vend_name,
                Vendor.vend_contact,
                Vendor.vend_phone
            FROM Product
            INNER JOIN Vendor
                ON Product.vend_code = Vendor.vend_code
            ORDER BY Product.prod_code
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
