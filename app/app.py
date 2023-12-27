from .db import create_db_and_tables

# from .models import Document, Issue, Token


def main():
    create_db_and_tables()
    # Additional application logic can be added here.


if __name__ == "__main__":
    main()
