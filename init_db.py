import sqlite3
from config import *

conn = sqlite3.connect("osu.db")
cursor = conn.cursor()
prefix_path = "schema/"

for mode in GAME_MODES:
    table_name = TABLES[mode]
    schema = prefix_path + SCHEMAS[mode]

    # delete table
    print(f"Delete: {TABLES[mode]}")
    conn.execute(f"DROP TABLE IF EXISTS {TABLES[mode]}")

    # create table
    with open(schema) as f:
        exe = f.read()
        conn.executescript(exe)
        print(f"Create: {TABLES[mode]}", end="\n\n")


    # test_id = 1000
    # insert_exe = f"INSERT INTO {table_name} VALUES({test_id},'Gensoukyo', '300', '24512', '353', '256,353', '3521')"
    # cursor.execute(insert_exe)
    # delete_exe = f"DELETE FROM {table_name} WHERE ranking = {test_id}"
    # cursor.execute(delete_exe)

conn.commit()
conn.close()


