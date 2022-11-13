from psycopg2 import Error
import psycopg2.extras

try:
    connection = psycopg2.connect(user="",
                                  password="",
                                  host="",
                                  port="",
                                  database="")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM hwid")
    record = cursor.fetchone()
    print("You are connected to base")

except (Exception, Error) as error:
    raise TypeError("Error while connecting to PostgreSQL", error)


async def add_hwid(id, hwid, name):
    cursor.execute(f"SELECT uuid FROM hwid WHERE uuid={id}")
    if not cursor.fetchone() is None:
        cursor.execute(f"UPDATE hwid SET hwid='{hwid}' WHERE uuid={id}")
        connection.commit()
        return 1

    cursor.execute(f"INSERT into hwid VALUES ({id},'{hwid}','{name}')")
    connection.commit()
    return 0


async def check_hwid(hwid):
    cursor.execute(f"SELECT name FROM hwid WHERE hwid='{hwid}'")
    result = cursor.fetchone()
    if not result is None:
        return result[0]