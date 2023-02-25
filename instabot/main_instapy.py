# requirements:
# - venv
# - modzilla firefox
# - selenium
# -> pip3 install selenium
# - driver modzilla for selenium: geckodriver 
# -> pip3 install geckodriver-autoinstaller
# - instapy
# -> python3 -m pip install instapy

# InstaPy doc: https://github.com/timgrossmann/InstaPy/blob/master/DOCUMENTATION.md

# to activate venv
# -> source  bin/activate

# Data
your_username = "anticoreste" 
your_password = "Inore20am"

# Main code
from instapy import InstaPy
from instapy import smart_run

# session = InstaPy(username=your_username, password=your_password, want_check_browser=False).login()  #, headless_browser=True
# session.like_by_tags(["cycling", "bici"], amount=1)

# while True:
# 	i=1

# # session.like_by_tags(["cycling", "bici"], amount=1)

session = InstaPy(username=your_username, password=your_password, want_check_browser=False)
with smart_run(session):
	session.like_by_tags(["cycling"], amount=10)

# session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)
# session.set_use_clarifai(enabled=True, api_key='324d6e2958e040208ce44ffe21c8fd7a')
# session.clarifai_check_img_for(['nsfw'])
# session.clarifai_check_img_for(['bike'], comment=True, comments=['Nice!'])

# 9 by default + amount
# session.set_do_follow(True, percentage=90)
# session.set_do_comment(True, percentage=90)
# session.set_comments(["Nice!", "Sweet!"])
# session.like_by_tags(["cycling", "bici"], amount=1)

# session.set_relationship_bounds(enabled=True, max_followers=8500)
# session.set_dont_like(["naked", "nsfw"])

# session.end()