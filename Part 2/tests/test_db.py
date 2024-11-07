import pytest
from unittest import mock
from app.repository.db import DBConnect  # Assuming DBConnect is in the db_connect module
from app.models.model import CheckinsModel
from datetime import datetime
from unittest.mock import MagicMock


@pytest.fixture
def mock_db_connection():
    # Mock the psycopg2 connection and cursor
    mock_conn = mock.MagicMock()
    mock_cursor = mock.MagicMock()

    # Mock the cursor's methods
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = [
        ("2024-11-07 14:30:00", "user1", 5),  # example checkin data
        ("2024-11-07 14:35:00", "user1", 6)
    ]
    mock_cursor.description = [("date",), ("user",), ("checkin_count",)]

    # Mock psycopg2.connect
    with mock.patch("psycopg2.connect", return_value=mock_conn):
        yield mock_conn, mock_cursor


def test_db_connect_initialization(mock_db_connection):
    with mock.patch("psycopg2.connect") as mock_psycopg2_connect:
        db = DBConnect()

        # Ensure that the connection is established correctly
        mock_psycopg2_connect.assert_called_once()


def test_get_checkins_records(mock_db_connection):
    now = datetime.now()
    mock_conn, mock_cursor = mock_db_connection

    db = DBConnect()
    user = "testuser"
    page = 1
    page_size = 10

    mock_cursor.fetchall.return_value = [["testuser", 4.5, "xxx", now.date()]]
    mock_cursor.description = [("user", ), ("hours",), ("project",), ("date",)]
    mock_cursor.rowcount.return_value = 1

    # Call the method being tested
    records, records_len = db.get_checkins_records(user, page, page_size)

    # Verify the result
    assert len(records) == 1
    assert records_len == 1
    assert records[0].user == "testuser"
    assert records[0].hours == 4.5
    assert records[0].project == "xxx"
    assert records[0].date == now.date()
    mock_cursor.execute.assert_called_once()


def test_get_checkins_count(mock_db_connection):
    mock_conn, mock_cursor = mock_db_connection

    db = DBConnect()
    user = "user1"
    mock_cursor.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = (2, )

    # Call the method being tested
    count = db.get_checkins_count(user)

    # Verify the result
    assert count == 2  # The mocked query should return count = 2
