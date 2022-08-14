 
from instaloader import Instaloader
loader = Instaloader()
username = input('enter username:     ')
loader.download_profile(username, profile_pic_only=True)
