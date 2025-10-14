import streamlit as st
import psycopg2
import os
from dotenv import load_dotenv
import random

# Load environment variables
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
load_dotenv(f"{parent_dir}/.env")

postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_port_no = os.getenv("POSTGRES_PORT_NO")
host = os.getenv("POSTGRES_HOST")
database = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")


def get_db_connection():
    """Get a database connection."""
    return psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=postgres_password,
        port=postgres_port_no,
    )


def initialise_db():
    """Initialise the database to log clicks."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS clicks (
                    id SERIAL PRIMARY KEY,
                    timestamp TIMESTAMP,
                    product_id TEXT,
                    variant INT
                )
            """
            )
            conn.commit()


def get_products():
    """Get all products from the database."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT product_id, product_name, image_path FROM generated_products"
            )
            return cur.fetchall()


def log_click(product_id, variant):
    """Log a click in the database."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO clicks (timestamp, product_id, variant) VALUES (NOW(), %s, %s)",
                (product_id, variant),
            )
            conn.commit()


def select_variant(variant, product_id):
    """Randomly select a variant for the given product_id."""
    title = f"generated_title{variant}"
    description = f"generated_description{variant}"
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                f"SELECT {title}, {description}, image_path FROM generated_products WHERE product_id = %s",
                (product_id,),
            )
            return cur.fetchone()


def display_product(product_id, variant):
    """Display the product title and description."""
    title, description, image_path = select_variant(variant, product_id)

    col1, col2 = st.columns([1, 2])  # Adjust the column width ratio as needed

    with col1:
        st.image(image_path, width=200)  # Adjust the width as needed

    with col2:
        st.markdown(
            f"""
        <h1 style="font-size:24px; color:black;">
            🛒 {title}
        </h1>
        """,
            unsafe_allow_html=True,
        )
        st.markdown(
            f"""
        <h1 style="font-size:24px; color:black;">
            📝 Product Description: <br>
        </h1>
        <div style="font-size:16px; color:grey;">{description}</div>
        """,
            unsafe_allow_html=True,
        )


def main():
    initialise_db()
    st.title("🛍️ Products For You")
    products = get_products()

    if "variant" not in st.session_state:
        st.session_state.variant = random.choice([1, 2])

    variant = st.session_state.variant
    for product in products:
        product_id, product_name, image_path = product
        display_product(product_id, variant)
        if st.button("Click for more", key=product_id):
            log_click(product_id, variant)


if __name__ == "__main__":
    main()
