from config import *

prefix_path = "schema/"

for mode in GAME_MODES:
    with open(prefix_path + SCHEMAS[mode], mode='w') as file:
        file.write(f'''CREATE TABLE IF NOT EXISTS {TABLES[mode]}
    ('ranking' INTEGER PRIMARY KEY ASC NOT NULL,
    'country_name' TEXT NOT NULL,
    'active_users' INTEGER NOT NULL,
    'play_count' INTEGER NOT NULL,
    'avg_score' INTEGER NOT NULL,
    'performance' INTEGER NOT NULL,
    'avg_performance' INTEGER NOT NULL
);
''')
