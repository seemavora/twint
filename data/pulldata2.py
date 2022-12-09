import twint

c = twint.Config()
c.Limit = 1000
c.Store_csv = True
c.Output = "sample.csv"
c.Lang = "en"
# c.Translate = True
c.Location =True
c.Search='Hurricane Ian'
twint.run.Search(c)

Tweets_df = twint.storage.panda.Tweets_df
Tweets_df.to_csv("sample.csv")