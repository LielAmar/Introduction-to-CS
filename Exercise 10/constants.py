from direction import Direction

COLOR_GREEN  = "green"
COLOR_RED    = "red"
COLOR_ORANGE = "orange"
COLOR_BLACK  = "black"

# === Sets up directions and relationships between directions ===
DIRECTIONS = {
    "Up": Direction(0, 1),
    "Down": Direction(0, -1),
    "Left": Direction(-1, 0),
    "Right": Direction(1, 0)
}

DIRECTIONS["Up"].add_allowed_switch(DIRECTIONS["Left"])
DIRECTIONS["Up"].add_allowed_switch(DIRECTIONS["Right"])

DIRECTIONS["Down"].add_allowed_switch(DIRECTIONS["Left"])
DIRECTIONS["Down"].add_allowed_switch(DIRECTIONS["Right"])

DIRECTIONS["Left"].add_allowed_switch(DIRECTIONS["Up"])
DIRECTIONS["Left"].add_allowed_switch(DIRECTIONS["Down"])

DIRECTIONS["Right"].add_allowed_switch(DIRECTIONS["Up"])
DIRECTIONS["Right"].add_allowed_switch(DIRECTIONS["Down"])

# === OTHER ===
AMOUNT_OF_APPLES = 3
SNAKE_GROWTH_FOR_APPLE = 3

KEEP_PLAYING = "keep_playing"
LOSE = "lost"
WIN = "won"