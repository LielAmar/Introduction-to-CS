# === LOGIC ===
BOARD_SIZE = 4

ROW_INDEX    = 0        # Index of row in a coordinate tuple
COLUMN_INDEX = 1        # Index of col in a coordinate tuple

MAX_ROW_DISTANCE    = 1 # Max distance between 2 coordinates in the same column
MAX_COLUMN_DISTANCE = 1 # Max distance between 2 coordinates in the same row

SCORE_INDEX = 0         # Index of row in a path_score tuple
PATH_INDEX  = 1         # Index of col in a path_score tuple


# === DEFAULTS ===
TIMER_DURATION      = 180 # Default duration of the timer in seconds
DEFAULT_BUTTON_TEXT = "?" # Default text of a button


# === PROPERTIES ===
PROP_TEXT                = "text"
PROP_COMMAND             = "command"
PROP_SELECTED            = "selected"
PROP_CURSOR              = "cursor"
PROP_WIDTH               = "width"
PROP_HEIGHT              = "height"
PROP_BACKGROUND          = "background"
PROP_FOREGROUND          = "foreground"
PROP_DISABLED_FOREGROUND = "disabledforeground"
PROP_ANCHOR              = "anchor"
PROP_FONT                = "font"
PROP_ENABLED             = "state"
PROP_HIGHLIGHTTHICKNESS  = "highlightthickness"

# === WIDGETS ===
SCORE       = "score"
ACTION      = "action"
TIMER       = "timer"
BUTTONS     = "buttons"
USED_WORDS  = "used_words"


# === STYLING ===
GUI_WIDTH  = 500
GUI_HEIGHT = 650
GUI_MARGIN = 50

TOP_FRAME_HEIGHT  = 75
MID_FRAME_HEIGHT  = 300
ACT_FRAME_HEIGHT  = 50
ACT_FRAME_PAD     = (25, 10)
BANK_FRAME_HEIGHT = 200

C1 = "#496878"
C2 = "#0F4C75"
C3 = "#3282B8"
C4 = "#BBE1FA"
C5 = "#000000"
C6 = "#ffffff"

GUI_BACKGROUND = C4

BUTTON_FONT = ('Helvetica', 14)
BUTTON_TEXT_COLOR = C5

ACTION_BUTTON_FONT = ('Helvetica', 16, 'bold')

BUTTON_NORMAL_BG_COLOR   = C3
BUTTON_NORMAL_FG_COLOR   = C5
BUTTON_DISABLED_BG_COLOR = C1
BUTTON_DISABLED_FG_COLOR = C6
BUTTON_SELECTED_BG_COLOR = C2
BUTTON_SELECTED_FG_COLOR = C6

LABEL_FONT = ('Helvetica', 16, 'bold', 'underline')
LABEL_FONT_UNFOCUSED = ('Helvetica', 12)
LABEL_TEXT_COLOR = C5

UP    = "n"
DOWN  = "s"
LEFT  = "w"
RIGHT = "e"