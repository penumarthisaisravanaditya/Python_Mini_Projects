#pip install instaloader

import instaloader

insta = instaloader.Instaloader()

username = input("Enter the Instagram username: ")

insta.download_profile(username, profile_pic_only=True)