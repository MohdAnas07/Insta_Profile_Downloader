import instaloader

ig = instaloader.Instaloader()
dp = input("Enter Insta UserName: ")
ig.download_profile(dp, profile_pic_only = True)
