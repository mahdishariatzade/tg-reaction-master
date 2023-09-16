from dotenv import load_dotenv
import os

load_dotenv()

API_ID = int(os.getenv('API_ID')) if os.getenv('API_ID') else int(input('API_ID: '))
API_HASH = os.getenv('API_HASH') if os.getenv('API_HASH') else input('API_HASH: ')
REACT_EMOJI = input('EMOJI: ')

# victim_ids = os.getenv('VICTIM_USER_IDS') if os.getenv('VICTIM_USER_IDS') else input('VICTIM_USER_IDS: ').split('-')
# victim_ids = list(map(int, victim_ids))
# 520008598 foroogh
# 6279874186 fariba
# group_ids = os.getenv('VICTIM_GROUP_IDS') if os.getenv('VICTIM_GROUP_IDS') else input('VICTIM_GROUP_IDS: ')
# -1001678716086
max_reaction = os.getenv('MAX_REACTION') if os.getenv('MAX_REACTION') else (input('MAX_REACTION: '))
max_reaction = int(max_reaction)
