import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENV = os.environ.get('PROJECT_ENV', 'development')

BRANCH = 'master' if ENV == 'production' else 'develop'

ASSETS_URL = 'https://raw.githubusercontent.com/depromeet/slackbot'
