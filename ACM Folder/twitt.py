'''Joe Muscolino: Twitter Bot'''
import tweepy



def main():
    consumer_key = 'S20xefDgAi4bX8ZcuLvP4n6MZ'
    consumer_secret = 'fWefs8B8nqFqn2yQkh8SIcLlOPzvoT3VYLNQz8WTvOZeY0gPXE'
    access_token = '1105578179840770048-CBxH9YxuEhr3aHxQF1byTYKzABoqtW'
    access_token_secret = 'eNdFiNrqhg39XnoVmrgK8lNjwsoQbvNLuD9y7woXhISWe'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    ### DONT EDIT ABOVE ###
    '''SENDS TWEET'''
    #api.update_status('new status')
    
    '''PRINTS TIMELINE'''
    public_tweets = api.home_timeline()
    count = 0 
    for tweet in public_tweets:
        print('TWEET BELOW')
        print(tweet.text)
        print()
            

    user = api.get_user('AcmArizona') ## USE @AcmArizona
    print(user.screen_name)
    print(user.followers_count)
    '''FINDS AND PRINTS WHO WE FOLLOW'''
    for friend in user.friends():
       print(friend.screen_name)

    friend_lis = []
    for friend in tweepy.Cursor(api.friends).items():
    # Process the friend here
        friend_lis.append(friend)
    
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()

    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print('Error! Failed to get request token.')

main()

