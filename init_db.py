import sqlite3

conn = sqlite3.connect("osu.db")
cursor = conn.cursor()
table_name = "country_rankings"
sql_path = "sql/country_schema.sql"

with open(sql_path) as f:
    exe = f.read().replace("{table_name}", table_name)
    conn.executescript(exe)


# test_id = 1000
# insert_exe = f"INSERT INTO {table_name} VALUES({test_id},'Gensoukyo', '300', '24512', '353', '256,353', '3521')"
# cursor.execute(insert_exe)

# delete_exe = f"DELETE FROM {table_name} WHERE ranking = {test_id}"
# cursor.execute(delete_exe)

conn.commit()
conn.close()


