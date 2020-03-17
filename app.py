# author: teknofage (Nokiddingknapping/SIMPLEMINDFULL)

import praw
import time
# import response
# import pirates.txt

from praw.errors import RateLimitExceeded, APIException
from requests import HTTPError
from requests.exceptions import ReadTimeout

"""
1. Search Reddit pages
2. find phrase "MCO Card"
3. Post response letting user/thread know about the name change, and how to refer to it in the future as "Monaco Card"
4. Sleep for some time
5. go to 1.
"""
# Initialize PRAW with a custom User-Agent

r = praw.Reddit("simple comment responder from SIMPLEMINDFULL")

# and login
reddit.login("bacon_sandwich_2014", "baconandpeanutbutter1!")

# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit("nostalgia")
corrected_users = set()   # to avoid duplicates
response = ""

for i in xrange(0, 10): #Run the loop ten times
    comments = r.get_comments('askreddit')
    for comment in comments:
        body = comment.body.lower()
        if body.find("He-man in the bathroom"):
            corrected_users.add(comment.author)
            #post response in subreddit thread, 
            # notify user
    time.sleep(120) #sleep for 2 minutes
    
for comment in subreddit.stream.comments():
    print(comment.body)
    if re.search("Pirates of Dark Water never got finished!", comment.body, re.IGNORECASE):
            mco_reply = "bacon_sandwich_2014 says: " + respo
            comment.reply(mco_reply)
            print(mco_reply)
    time.sleep(120) #sleep for 2 minutes
    



if __name__ == "__main__":
    main()
