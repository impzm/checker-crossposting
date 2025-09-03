import praw 
reddit = praw.Reddit(client_id='your_client_id_here',
                     client_secret='your_client_secret_here',
                     username='your_username',
                     password = 'your_password',
                     user_agent = 'Crossposting')


subreddit = reddit.subreddit('subreddit_name').is_crosspostable_subreddit

print(subreddit)