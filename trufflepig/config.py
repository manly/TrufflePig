import os

# The steemit nodes to load data from
NODE_URL = os.environ.get('STEEM_NODE_URL', 'https://api.steemit.com')
NODE_URL2 = os.environ.get('STEEM_NODE_URL2', 'https://steemd.privex.io')
NODE_URL3 = os.environ.get('STEEM_NODE_URL3', None)
NODES = [x for x in (NODE_URL, NODE_URL2) if x]

# The steemit bot account and password
ACCOUNT = os.environ.get('STEEM_ACCOUNT', 'trufflepig')
PASSWORD = os.environ.get('STEEM_PASSWORD', None)
if PASSWORD:
    # The wallet creation needs it in this very explicit way :-(
    os.environ['UNLOCK'] = PASSWORD
POSTING_KEY = os.environ.get('STEEM_POSTING_KEY', None)

# Useful helper constant
PROJECT_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))