"""
Deployment script for Depromeet slackbot.

Usage: python deploy.py [STAGE]
[STAGE] must be either 'dev' or 'prod'
"""

import os
import sys

try:
    STAGE = sys.argv[1]
except IndexError:
    raise ValueError('stage must be provided')
    sys.exit(1)

VALID_STAGE = ('dev', 'prod')
if STAGE not in VALID_STAGE:
    raise ValueError('stage must be either "dev" or "prod"')
    sys.exit(1)

# 1. Install requirements into current directory
os.system('pip install -r requirements.txt -t . --upgrade')

# 2. Execute deployment
os.system('npx sls deploy --stage {} --verbose'.format(STAGE))
if STAGE == 'prod':
    os.system('npx sls remove dev')

# 3. Clean up directory
requirements_file = open('requirements.txt', 'r')

for line in requirements_file:
    requirement = line.split('==')[0]

    os.system('rm -rf {}*'.format(requirement))
    if requirement != requirement.lower():
        os.system('rm -rf {}*'.format(requirement.lower()))
    os.system('rm -rf bin')

requirements_file.close()
