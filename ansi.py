"""
ANSI CONST LIB
This library contains a lot of functions and constants to use ANSI chars more easily
"""

__author__ = 'Ejilonh'

# ╔══════════════════════════════╗
# ║ Native Escape Characters     ║
# ╚══════════════════════════════╝
BACKSLASH = ANTISLASH = AS = '\\'
SINGLE_QUOTE = SQ = '\''
DOUBLE_QUOTE = DQ = '\"'
BELL = BEL = '\a'
BACKSPACE = BS = '\b'
TAB = HT = '\t'
VERTICAL_TAB = VT = '\v'
LINE_FEED = NEWLINE = LF = '\n'
FORM_FEED = FF = '\f'
CARRIAGE_RETURN = CR = '\r'
ESCAPE = ESC = '\33'
OCTAL = lambda x: f'{AS}o{x}'
HEX = lambda x: f'{AS}x{x}'

# ╔══════════════════════════════╗
# ║ FE Escape Sequence           ║
# ╚══════════════════════════════╝
SS2 = f'{ESC}N' # Single Shift Two
SS3 = f'{ESC}O' # Single Shift Three
DCS = f'{ESC}P' # Device Control String
CSI = f'{ESC}[' # Control Sequence Introducer
ST = f'{ESC}\\' # String Terminator
OSC = f'{ESC}]' # Operating System Command
SOS = f'{ESC}X' # Start Of String
PM = f'{ESC}^' # Privacy Message
APC = f'{ESC}_' # Application Program Command

# ╔══════════════════════════════╗
# ║ CSI Sequences                ║
# ╚══════════════════════════════╝
UP = CUU = lambda n = 1: f'{CSI}{n}A' # Cursor Up
DOWN = CUD = lambda n = 1: f'{CSI}{n}B' # Cursor Down
FORWARDS = CUF = lambda n = 1: f'{CSI}{n}C' # Cursor Forwards
BACKWARDS = CUB = lambda n = 1: f'{CSI}{n}D' # Cursor Backwards
NEXT_LINE = CNL = lambda n = 1: f'{CSI}{n}E' # Cursor Next Line
PREVIOUS_LINE = CPL = lambda n = 1: f'{CSI}{n}F' # Cursor Previous Line
CHA = lambda n = 1: f'{CSI}{n}G' # Cursor Horizontal Absolute
CURSOR_POS = CUP = lambda n, m: f'{CSI}{n};{m}H' # Cursor Position
ED = lambda n = 1: f'{CSI}{n}J' # Erase in Display 
EL = lambda n = 1: f'{CSI}{n}K' # Erase in Line
SU = lambda n = 1: f'{CSI}{n}S' # Scroll Up
SD = lambda n = 1: f'{CSI}{n}T' # Scroll Down
HVP = lambda n, m: f'{CSI}{n};{m}f' # Horizontal Vertical Position
SGR = lambda n = 1: f'{CSI}{n}m' # Select Graphic Rendition
AUXPORT_ON = f'{CSI}5i' # AUX Port ON
AUXPORT_OFF = f'{CSI}4i' # AUX Port OFF
DSR = f'{CSI}6n' # Device Status Report
SCP = SCOSC = f'{CSI}s' # Save Current Cursor Position
RCP = SCORC = f'{CSI}u' # Restore Saved Cursor Position

# ╔══════════════════════════════╗
# ║ Select Graphic Rendition     ║
# ╚══════════════════════════════╝
RESET = f'{CSI}0m' # Reset style
BOLD = f'{CSI}1m' # Bold
DIM = FAINT = f'{CSI}2m' # Faint/Dim
ITALIC = f'{CSI}3m' # Italic [Not Widely Supported]
UNDERLINE = f'{CSI}4m' # Underline
BLINK_SLOW = f'{CSI}5m' # Slow Blink
BLINK_RAPID = f'{CSI}6m' # Rapid Blink [Not Widely Supported]
INVERT = f'{CSI}7m' # Swap BG and FG colors
HIDE = f'{CSI}8m' # Invisible Text [Not Widely Supported]
STRIKETHROUGH = f'{CSI}9m' # Strikethrough [!Terminal App]
PRIMARY = f'{CSI}10m' # Default Font
AFONT_1 = f'{CSI}11m' # Alternative Font 1
AFONT_2 = f'{CSI}12m' # Alternative Font 2
AFONT_3 = f'{CSI}13m' # Alternative Font 3
AFONT_4 = f'{CSI}14m' # Alternative Font 4
AFONT_5 = f'{CSI}15m' # Alternative Font 5
AFONT_6 = f'{CSI}16m' # Alternative Font 6
AFONT_7 = f'{CSI}17m' # Alternative Font 7
AFONT_8 = f'{CSI}18m' # Alternative Font 8
AFONT_9 = f'{CSI}19m' # Alternative Font 9
FRACKTUR_FONT = f'{CSI}20m' # Fraktur Font [Rarely Supported]
DOUBLE_UNDERLINE = f'{CSI}21m' # Double Underline
DEFAULT_WEIGHT = f'{CSI}22m' # Default Wheight (not bold)
DEFAULT_TILT = f'{CSI}23m' # Default Tilt (not italic)
DEFAULT_LINE = f'{CSI}24m' # Default Line (not underline)
DEFAULT_BLINK = f'{CSI}25m' # Default Blink (not blinking)
EQUAL_SPACING = f'{CSI}26m' # Proportional spacing
UNINVERT = f'{CSI}27m' # Swap FG and BG colors
SHOW = f'{CSI}28m' # Not Invisible Text
DEFAULT_STRIKE = f'{CSI}29m' # Default Blink (not strikethrough)
FG_COLOR = lambda r, g, b: f'{CSI}38;2;{r};{g};{b}m' # Set RBG Foreground Color
FG_COLOR_32B = lambda n: f'{CSI}38;5;{n}m' # Set 32 Byte Foreground Color
DEFAULT_FG_COLOR = f'{CSI}39m' # Default FG color
BG_COLOR = lambda r, g, b: f'{CSI}48;2;{r};{g};{b}m' # Set RBG Background Color
BG_COLOR_32B = lambda n: f'{CSI}48;5;{n}m' # Set 32 Byte Background Color
DEFAULT_BG_COLOR = f'{CSI}49m' # Default BG color
DEFAULT_SPACING = f'{CSI}50m' # Default Spacing (not proportional spacing)
FRAMED = f'{CSI}51m' # Frames
ENCIRCLED = f'{CSI}52m' # Encircled
OVERLINED = f'{CSI}53m' # Overlined [!Terminal App]
DEFAULT_MINTTY = f'{CSI}54m' # Not Framed or Encircled
DEFAULT_OVERLINE = f'{CSI}55m' # Not Overlined
UL_COLOR = lambda r, g, b: f'{CSI}58;2;{r};{g};{b}m' # Set RBG Underline Color [Kitty, VTE, mintty, and iTerm2] NOT IN STANDARD
UL_COLOR_32B = lambda n: f'{CSI}58;5;{n}m' # Set 32 Byte Underline Color [Kitty, VTE, mintty, and iTerm2] NOT IN STANDARD
DEFAULT_UL_COLOR = f'{CSI}59m' # Default UL color
IDEOGRAM_UNDERLINE = RIGHT_SIDE_LINE = f'{CSI}60m' # Ideogram underline or right side line [Rarely Supported]
IDEOGRAM_DOUBLE_UNDERLINE = DOUBLE_RIGHT_SIDE_LINE = f'{CSI}61m' # Ideogram double underline, or double line on the right side [Rarely Supported]
IDEOGRAM_OVERLINE = LEFT_SIDE_LINE = f'{CSI}62m' # Ideogram overline or left side line [Rarely Supported]
IDEOGRAM_DOUBLE_OVERLINE = DOUBLE_LEFT_SIDE_LINE = f'{CSI}63m' # Ideogram double overline, or double line on the left side [Rarely Supported]
IDEOGRAM_STRESS_MARKING = f'{CSI}64m' # Ideogram stress marking [Rarely Supported]
DEFAULT_IDEOGRAM_ATTR = f'{CSI}65m' # No Ideogram Attributes
SUPERSCRIPT = f'{CSI}73m' # Superscript [Mintty]
SUBSCRIPT = f'{CSI}74m' # Subscript [Mintty]
DEFAULT_SCRIPT = f'{CSI}75m' # No superscript or subscript [Mintty]
BRIGHT_FG_COLOR = lambda r, g, b: f'{CSI}90;2;{r};{g};{b}m' # Set RBG Bright Foreground Color [AxTerm] NOT IN STANDARD
BRIGHT_FG_COLOR_32B = lambda n: f'{CSI}90;5;{n}m' # Set 32 Byte Bright Foreground Color [AxTerm] NOT IN STANDARD
BRIGHT_BG_COLOR = lambda r, g, b: f'{CSI}100;2;{r};{g};{b}m' # Set RBG Bright Background Color [AxTerm] NOT IN STANDARD
BRIGHT_BG_COLOR_32B = lambda n: f'{CSI}100;5;{n}m' # Set 32 Byte Bright Background Color [AxTerm] NOT IN STANDARD

# ╔══════════════════════════════╗
# ║ Colors                       ║
# ╚══════════════════════════════╝
# 3-BIT and 4-BIT
# Foreground
FG_BLACK = f'{CSI}30m'
FG_RED = f'{CSI}31m'
FG_GREEN = f'{CSI}32m'
FG_YELLOW = f'{CSI}33m'
FG_BLUE = f'{CSI}34m'
FG_MAGENTA = f'{CSI}35m'
FG_CYAN = f'{CSI}36m'
FG_WHITE = f'{CSI}37m'
FG_GRAY = FG_GREY = FG_BRIGHT_BLACK = f'{CSI}90m'
FG_BRIGHT_RED = f'{CSI}91m'
FG_BRIGHT_GREEN = f'{CSI}92m'
FG_BRIGHT_YELLOW = f'{CSI}93m'
FG_BRIGHT_BLUE = f'{CSI}94m'
FG_BRIGHT_MAGENTA = f'{CSI}95m'
FG_BRIGHT_CYAN = f'{CSI}96m'
FG_BRIGHT_WHITE = f'{CSI}97m'
# Background
BG_BLACK = f'{CSI}40m'
BG_RED = f'{CSI}41m'
BG_GREEN = f'{CSI}42m'
BG_YELLOW = f'{CSI}43m'
BG_BLUE = f'{CSI}44m'
BG_MAGENTA = f'{CSI}45m'
BG_CYAN = f'{CSI}46m'
BG_WHITE = f'{CSI}47m'
BG_GRAY = BG_GREY = BG_BRIGHT_BLACK = f'{CSI}100m'
BG_BRIGHT_RED = f'{CSI}101m'
BG_BRIGHT_GREEN = f'{CSI}102m'
BG_BRIGHT_YELLOW = f'{CSI}103m'
BG_BRIGHT_BLUE = f'{CSI}104m'
BG_BRIGHT_MAGENTA = f'{CSI}105m'
BG_BRIGHT_CYAN = f'{CSI}106m'
BG_BRIGHT_WHITE = f'{CSI}107m'

# 8-BIT
LOOKUP_8B_COLORS = {

      0: '#000000',   1: '#800000',   2: '#008000',   3: '#808000',   4: '#000080',   5: '#800080',   6: '#008080',   7: '#c0c0c0',
      8: '#808080',   9: '#ff0000',  10: '#00ff00',  11: '#ffff00',  12: '#0000ff',  13: '#ff00ff',  14: '#00ffff',  15: '#ffffff',
    
     16: '#000000',  17: '#00005f',  18: '#000087',  19: '#0000af',  20: '#0000d7',  21: '#0000ff',
     22: '#005f00',  23: '#005f5f',  24: '#005f87',  25: '#005faf',  26: '#005fd7',  27: '#005fff', 
     28: '#008700',  29: '#00875f',  30: '#008787',  31: '#0087af',  32: '#0087d7',  33: '#0087ff', 
     34: '#00af00',  35: '#00af5f',  36: '#00af87',  37: '#00afaf',  38: '#00afd7',  39: '#00afff', 
     40: '#00d700',  41: '#00d75f',  42: '#00d787',  43: '#00d7af',  44: '#00d7d7',  45: '#00d7ff', 
     46: '#00ff00',  47: '#00ff5f',  48: '#00ff87',  49: '#00ffaf',  50: '#00ffd7',  51: '#00ffff', 
     
     52: '#5f0000',  53: '#5f005f',  54: '#5f0087',  55: '#5f00af',  56: '#5f00d7',  57: '#5f00ff', 
     58: '#5f5f00',  59: '#5f5f5f',  60: '#5f5f87',  61: '#5f5faf',  62: '#5f5fd7',  63: '#5f5fff', 
     64: '#5f8700',  65: '#5f875f',  66: '#5f8787',  67: '#5f87af',  68: '#5f87d7',  69: '#5f87ff', 
     70: '#5faf00',  71: '#5faf5f',  72: '#5faf87',  73: '#5fafaf',  74: '#5fafd7',  75: '#5fafff', 
     76: '#5fd700',  77: '#5fd75f',  78: '#5fd787',  79: '#5fd7af',  80: '#5fd7d7',  81: '#5fd7ff', 
     82: '#5fff00',  83: '#5fff5f',  84: '#5fff87',  85: '#5fffaf',  86: '#5fffd7',  87: '#5fffff', 
     
     88: '#870000',  89: '#87005f',  90: '#870087',  91: '#8700af',  92: '#8700d7',  93: '#8700ff', 
     94: '#875f00',  95: '#875f5f',  96: '#875f87',  97: '#875faf',  98: '#875fd7',  99: '#875fff', 
    100: '#878700', 101: '#87875f', 102: '#878787', 103: '#8787af', 104: '#8787d7', 105: '#8787ff',
    106: '#87af00', 107: '#87af5f', 108: '#87af87', 109: '#87afaf', 110: '#87afd7', 111: '#87afff', 
    112: '#87d700', 113: '#87d75f', 114: '#87d787', 115: '#87d7af', 116: '#87d7d7', 117: '#87d7ff', 
    118: '#87ff00', 119: '#87ff5f', 120: '#87ff87', 121: '#87ffaf', 122: '#87ffd7', 123: '#87ffff', 
    
    124: '#af0000', 125: '#af005f', 126: '#af0087', 127: '#af00af', 128: '#af00d7', 129: '#af00ff', 
    130: '#af5f00', 131: '#af5f5f', 132: '#af5f87', 133: '#af5faf', 134: '#af5fd7', 135: '#af5fff', 
    136: '#af8700', 137: '#af875f', 138: '#af8787', 139: '#af87af', 140: '#af87d7', 141: '#af87ff', 
    142: '#afaf00', 143: '#afaf5f', 144: '#afaf87', 145: '#afafaf', 146: '#afafd7', 147: '#afafff', 
    148: '#afd700', 149: '#afd75f', 150: '#afd787', 151: '#afd7af', 152: '#afd7d7', 153: '#afd7ff', 
    154: '#afff00', 155: '#afff5f', 156: '#afff87', 157: '#afffaf', 158: '#afffd7', 159: '#afffff',
    
    160: '#d70000', 161: '#d7005f', 162: '#d70087', 163: '#d700af', 164: '#d700d7', 165: '#d700ff',
    166: '#d75f00', 167: '#d75f5f', 168: '#d75f87', 169: '#d75faf', 170: '#d75fd7', 171: '#d75fff', 
    172: '#d78700', 173: '#d7875f', 174: '#d78787', 175: '#d787af', 176: '#d787d7', 177: '#d787ff', 
    178: '#d7af00', 179: '#d7af5f', 180: '#d7af87', 181: '#d7afaf', 182: '#d7afd7', 183: '#d7afff', 
    184: '#d7d700', 185: '#d7d75f', 186: '#d7d787', 187: '#d7d7af', 188: '#d7d7d7', 189: '#d7d7ff',
    190: '#d7ff00', 191: '#d7ff5f', 192: '#d7ff87', 193: '#d7ffaf', 194: '#d7ffd7', 195: '#d7ffff',
    
    196: '#ff0000', 197: '#ff005f', 198: '#ff0087', 199: '#ff00af', 200: '#ff00d7', 201: '#ff00ff',
    202: '#ff5f00', 203: '#ff5f5f', 204: '#ff5f87', 205: '#ff5faf', 206: '#ff5fd7', 207: '#ff5fff', 
    208: '#ff8700', 209: '#ff875f', 210: '#ff8787', 211: '#ff87af', 212: '#ff87d7', 213: '#ff87ff', 
    214: '#ffaf00', 215: '#ffaf5f', 216: '#ffaf87', 217: '#ffafaf', 218: '#ffafd7', 219: '#ffafff', 
    220: '#ffd700', 221: '#ffd75f', 222: '#ffd787', 223: '#ffd7af', 224: '#ffd7d7', 225: '#ffd7ff', 
    226: '#ffff00', 227: '#ffff5f', 228: '#ffff87', 229: '#ffffaf', 230: '#ffffd7', 231: '#ffffff', 
    
    232: '#080808', 233: '#121212', 234: '#1c1c1c', 235: '#262626', 236: '#303030', 237: '#3a3a3a',
    238: '#444444', 239: '#4e4e4e', 240: '#585858', 241: '#626262', 242: '#6c6c6c', 243: '#767676', 
    244: '#808080', 245: '#8a8a8a', 246: '#949494', 247: '#9e9e9e', 248: '#a8a8a8', 249: '#b2b2b2', 
    250: '#bcbcbc', 251: '#c6c6c6', 252: '#d0d0d0', 253: '#dadada', 254: '#e4e4e4', 255: '#eeeeee'
}

# ╔══════════════════════════════╗
# ║ Other Escape Sequences       ║
# ╚══════════════════════════════╝

# Fs Sequences
RIS = f'{ESC}c' # Reset to Initial State

# Fp Sequences
DECSC = f'{ESC}7' # DEC Save Cursor
DECRC = f'{ESC}8' # DEC Restore Cursor

# nF Sequences
ACS6 = S7C1T = f'{ESC}SPF' # Announce Code Structure 6 and Send 7-bit C1 Control Character to the Host
ACS7 = S8C1T = f'{ESC}SPG' # Announce Code Structure 7 and Send 8-bit C1 Control Character to the Host
DECDHL_TOP =  f'{ESC}#3' # DEC Double-Height Letters, Top Half
DECDHL_BOTTOM =  f'{ESC}#3' # DEC Double-Height Letters, Bottom Half
DECSWL = f'{ESC}#3' # DEC Single-Width Line 
DECDWL = f'{ESC}#3' # DEC Double-Width Line

# ╔══════════════════════════════╗
# ║ Keys                         ║
# ╚══════════════════════════════╝
KEY = lambda key, mod = []: f'{ESC}{key};{sum(mod)}~'

# Modifiers
SHIFT = 1
LEFT_ALT = 2
CTRL = 4
META = 8

# Keys
VT_HOME = '1'
VT_INSERT = '2'
VT_DELETE = '3'
VT_END = '4'
VT_PGUP = '5'
VT_PGDN = '6'
VT_F0 = '10'
VT_F1 = '11'
VT_F2 = '12'
VT_F3 = '13'
VT_F4 = '14'
VT_F5 = '15'
VT_F6 = '17'
VT_F7 = '18'
VT_F8 = '19'
VT_F9 = '20'
VT_F10 = '21'
VT_F11 = '23'
VT_F12 = '24'
VT_F13 = '25'
VT_F14 = '26'
VT_F15 = '28'
VT_F16 = '29'
VT_F17 = '31'
VT_F18 = '32'
VT_F19 = '33'
VT_F20 = '34'
XTERM_UP = 'A'
XTERM_DOWN = 'B'
XTERM_RIGHT = 'C'
XTERM_LEFT = 'D'
XTERM_END = 'F'
XTERM_KEYPAD_5 = 'G'
XTERM_HOME = 'H'
XTERM_F1 = '1P'
XTERM_F2 = '1Q'
XTERM_F3 = '1R'
XTERM_F4 = 'S'