CREATE TABLE IF NOT EXISTS fruits_country_rankings
    ('ranking' INTEGER PRIMARY KEY ASC NOT NULL,
    'country_name' TEXT NOT NULL,
    'active_users' INTEGER NOT NULL,
    'play_count' INTEGER NOT NULL,
    'avg_score' INTEGER NOT NULL,
    'performance' INTEGER NOT NULL,
    'avg_performance' INTEGER NOT NULL
);
