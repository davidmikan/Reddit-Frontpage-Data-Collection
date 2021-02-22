SAVE_PATH = f'sub_scraper/datasets/final5:10:100_'
DEFAULT_PROFILE = 'stalkerpublic'
ALT_PROFILE = 'stalker007'

SUBREDDITS = ['memes']

INTERVAL_M = 5
SAVES = 30

MAX_TIMEDIF = 5
MAX_GROUPSIZE = 100
MAX_FILTER = 100

ATTR_STATIC = ['created_utc', 'name', 'permalink', 'is_self']
"""
Die Attribute, die nur bei der Collection des Posts abgerufen werden, und unveränderlich sind.
float created_utc: die Zeit in Sekunden seit 1.1.1979 (UTC+0) bis zur Erstellung des Posts
str name: der Titel des Posts
str permalink: ein Link zum Abrufen des Posts (anzuhängen an www.reddit.com/)
bool is_self: ob der Post ein reiner Textpost, oder sonstiges it
"""
ATTR_VARIABLE = ['score', 'upvote_ratio', 'num_comments', 'stickied']
"""
Attribute, die variabel sind und bei jedem Update eines Posts abgerufen werden (das erste Mal
unmittelbar nach der Collection)
int score: Der Score des Posts (Anz. der Upvotes - Anz. der Downvotes)
float upvote_ratio: 1 - (Anz. der Downvotes / Anz. der Upvotes), das Verhältnis von Upvotes zu 
Downvotes (1 bedeutet keine Downvotes)
int num_comments: Anzahl der Kommentare
bool stickied: ob der Post von Moderatoren an die Spitze der Subreddit-Frontpage gepinnt wurde,
nur erhoben um Posts mit diesem Bias auszuschließen
"""

GGPLOT_PATH = 'sub_scraper/plots/ggplots/'

blue = '#4fc7ff'
yellow = '#ffcd03'
red = '#db2100'
green = '#56b800'
black = '#1c1c1c'
white = '#ffffff'

light = '#F4F6F5'
light2 = '#DFE8E5'
dark = '#16171C'
dead = '#577590'
rising = '#FEA538'
hot = '#FF0F2B'

scalex, scaley = [1, 150], [0, 5000]