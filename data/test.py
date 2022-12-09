
import twint
import nest_asyncio
import pandas as pd

#https://medium.com/geekculture/introduction-to-twint-say-goodbye-to-twitter-rate-limitations-also-no-need-for-a-twitter-api-b632084db0ba
def collect_tweets_from_user(keywords, from_date, end_date, dst_file, limit = 10000):

  # To avoid "the event loop is already running in python" error message.
  nest_asyncio.apply()

  # Configure
  conf = twint.Config()

  # Tweets from Joe Biden
#   conf.Username = tw_username

  #Get tweets published after March 1st, 2022
  conf.Since = from_date
  conf.Until = end_date
  # Search Criteria
  conf.Search = keywords
  conf.Limit = limit

  # Tweets Storage
  conf.Output = dst_file
  conf.Store_json = True

  # Run the execution
  twint.run.Search(conf)

# def collect_tweets(keywords, from_date, dst_file, limit=50):

#   # To avoid the event loop is already running in python error message.
#   nest_asyncio.apply()

#   # Configure
#   conf = twint.Config()

#   #Get tweets published after March 1st, 2022
#   conf.Since = from_date
#   conf.Until = end_date
#   # Search Criteria
#   conf.Search = keywords
 
#   conf.Limit = limit

#   conf.Output = dst_file

#   conf.Store_json = True

#   # Run
#   twint.run.Search(conf)
# tw_username = "elonmusk"
keywords = "Hurricane Ian"
from_date = "2022-09-23"
end_date = "2022-10-1"
dst_file = "hurricaneIanDuring_range.json"

collect_tweets_from_user(keywords, from_date, end_date, dst_file)
# collect_tweets_from_user(keywords, from_date, dst_file)
# collect_tweets(keywords, from_date, end_date, dst_file)

def convert_to_df(tweets_json_file, cols = ["date", "username", "tweet"]):

  # Read the file as pandas dataframe
  pandas_df = pd.read_json(tweets_json_file, lines = True)

  #Only get specific columns
  pandas_df = pandas_df[cols]

  return pandas_df

biden_tweet_df = convert_to_df("hurricaneIanDuring_range.json")
biden_tweet_df.to_csv('hurricaneIanDuring.csv')