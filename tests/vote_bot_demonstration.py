import praw

# Achtung: Dieses Skript dient nur edukativen Zwecken. Vote Manipulation durch Bots
# ist auf Reddit verboten und wird, falls nachgewiesen, mit (Shadow-)Bans bestraft.

bot = praw.Reddit( 
    # Die Anmeldedaten sind mit jenen des jeweiligen Accounts auszufüllen.
    # Wie man sich API-Zugang verschafft, wird in
    # https://praw.readthedocs.io/en/latest/getting_started/quick_start.html demonstriert
    # (zugegriffen am 22.2.2021)
    client_id = '###',
    client_secret = '###',
    password = '###',
    username = '###',
    user_agent = '###'
)
target = bot.subreddit('memes')
disliked_keywords = [
    # Eine Liste mit Schlüsselwörtern, die nicht erwünscht sind,
    # diese wird der Bot mit Downvotes versehen
    'dog',
    'puppy',
    'pitbull',
    'good boy'
]
liked_keywords = [
    # Enthält der Post eines diese Schlüsselwörter, gibt der Bot ihm
    # ein Upvote
    'cat',
    'kitten',
    'meow'
]

for post in target.stream.submissions():
    # Der Stream agiert als Endlosschleife: jeder neu erstellte Post 
    # läuft durch durch eine Iteration und sein Titel wird sodann mit
    # den Schlüsselwörtern abgeglichen, und die passende Handlung durchgeführt
    name = post.name.lower()
    if any(k in name for k in disliked_keywords):
        post.downvote()
    elif any(k in name for k in liked_keywords):
        post.upvote()