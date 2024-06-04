GAME_MODES = ["osu", "taiko", "mania", "fruits"]
SCHEMAS = { mode : f"{mode}_schema.sql" for mode in GAME_MODES}
SCHEMA_LIST = [SCHEMAS[mode] for mode in GAME_MODES]
TABLES = { mode : f"{mode}_country_rankings" for mode in GAME_MODES}
CURRENT_MODE = "osu"

CRAWLER_NAME = "country_rankings"

START_PAGE = 1
END_PAGE = 2
DATABASE = "osu.db"

COUNTRY_RANKINGS_ENTRIES = [
     'ranking',
     'country_name',
     'active_users',
     'play_count',
     'avg_score',
     'performance',
     'avg_performance'
]

PAGES = {

    "titles": [
        'Table',
        'Active Users',
        'Play Count',
        'Avg Score',
        'Performance',
        'Avg Performance',

        'Scatter Chart1',
        'Scatter Chart2',
        'Scatter Chart3',
        'Scatter Chart4',
    ],

    "routes": [
        '',
        'active_users',
        'play_count',
        'avg_score',
        'performance',
        'avg_performance',

        'scatter?x=play_count&y=avg_performance',
        'scatter?x=play_count&y=avg_score',
        'scatter?x=active_users&y=avg_performance',
        'scatter?x=active_users&y=avg_score',
    ]

}

CONSTANT_OBJ = {
    "GAME_MODES": GAME_MODES,
    "COUNTRY_RANKINGS_ENTRIES": COUNTRY_RANKINGS_ENTRIES,
    "PAGES":PAGES,
    "SCHEMAS": SCHEMAS,
    "SCHEMA_LIST": SCHEMA_LIST
}

def change_current_mode(mode):
    CURRENT_MODE = mode


