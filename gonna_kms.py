import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()
print("right before the insert")
test_var = "test_var"
cursor.execute(f"INSERT INTO comments VALUES ('{test_var}')")
print("right before the insert")
connection.commit()
cursor.close()
connection.close()


print("POGGERS")

