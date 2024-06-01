CREATE TABLE IF NOT EXISTS {table_name}
    ('ranking' integer primary key not null,
     'country_name' text not null,
     'active_users' text not null,
     'play_count' text not null,
     'avg_score' text not null,
     'performance' text not null,
     'avg_performance' text not null
)