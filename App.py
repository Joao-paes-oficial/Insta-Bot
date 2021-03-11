from instapy import InstaPy
from instapy import smart_run

# Put your insta username and password
session = InstaPy(username = '', password = '')

with smart_run(session):
    session.set_do_follow(enabled = True, percentage = 100) #To follow 100% people
    session.set_do_like(enabled = True, percentage = 100) #To like 100% people's photo
    session.like_by_tags(['Tag necessária, ex: udemy'], amount = 5) #Put the amount people to follow and like
    comments = ['Nice shot!', 'I love your posts'] #Comments to do
    session.set_do_comment(enabled = True, percentage = 95) #It's a error
    session.set_comments(comments, media = 'Photo') #Just comments on photos
    session.join_pods() #To join 