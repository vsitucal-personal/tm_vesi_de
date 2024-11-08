import psycopg2
from decouple import config
from app.logger import Logger
from app.models.model import CheckinsModel


class DBConnect:
    def __init__(self):
        self.logger = Logger.get_logger()
        try:
            # Initialize the database connection
            self.conn = psycopg2.connect(
                host=config("DB_HOST"),
                port=config("DB_PORT"),
                database=config("DB_NAME"),
                user=config("DB_USER"),
                password=config("DB_PASS")
            )
            print("Database connection successful!")
        except Exception as e:
            self.logger.info("Failed to connect to the database:", e)
            self.conn = None

    def get_checkins_records(self, user: str, page: int, page_size: int):
        query = """
            SELECT * FROM checkins
            WHERE "user" = %s
            ORDER BY date DESC
            LIMIT %s OFFSET %s;
        """
        cursor = self.conn.cursor()
        cursor.execute(query, (user, page_size, (page-1)*page_size))
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        result = [CheckinsModel(**dict(zip(columns, row))) for row in rows]
        return result, len(result)

    def get_checkins_count(self, user: str):
        query = """
            SELECT COUNT(*) FROM checkins
            WHERE "user" = %s;
        """

        cursor = self.conn.cursor()
        cursor.execute(query, (user,))
        
        # Fetch the result
        row = cursor.fetchone()
        
        # The count will be the first element of the row
        count = row[0] if row else 0
        return count


