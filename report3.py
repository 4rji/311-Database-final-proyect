"""Report 3 for the Havi Online Store database."""

from datetime import date
from getpass import getpass

try:
    import mysql.connector
except ModuleNotFoundError:
    print("Missing mysql connector. Run: amiga")
    raise SystemExit(1)


STUDENT_NAME = "Your Name"


def print_report(product_id, product):
    """Display one product selected by the user."""
    print("\nHAVI ONLINE STORE")
    print(f"Student: {STUDENT_NAME}")
    print("Report 3 - Product Lookup")
    print(f"Date: {date.today().strftime('%m/%d/%Y')}")
    print(f"Product ID entered: {product_id}")
    print("-" * 92)
    print(
        f"{'Product ID':<12}"
        f"{'Product Name':<20}"
        f"{'Price':>12}"
        f"{'Stock':>10}  "
        f"{'Vendor':<20}"
        f"{'Phone':>12}"
    )
    print("-" * 92)

    if product is None:
        print("No product found for that Product ID.")
    else:
        prod_code, prod_desc, prod_price, prod_quant, vend_name, vend_phone = product
        print(
            f"{prod_code:<12}"
            f"{prod_desc:<20}"
            f"${prod_price:>11.2f}"
            f"{prod_quant:>10}  "
            f"{vend_name:<20}"
            f"{vend_phone:>12}"
        )

    print("-" * 92)


def main():
    print("MySQL Login")
    username = input("Username [havi_user]: ").strip() or "havi_user"
    password = getpass("Password: ")

    print("\nReport Input")
    product_id = input("Enter Product ID: ").strip()

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
                Product.prod_price,
                Product.prod_quant,
                Vendor.vend_name,
                Vendor.vend_phone
            FROM Product
            INNER JOIN Vendor
                ON Product.vend_code = Vendor.vend_code
            WHERE Product.prod_code = %s
            """,
            (product_id,),
        )
        print_report(product_id, cursor.fetchone())
    except mysql.connector.Error as error:
        print(f"Database error: {error}")
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    main()
