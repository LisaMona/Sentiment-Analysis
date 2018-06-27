
#import TextBlob
from textblob import TextBlob

text = "It is a great book"
obj = TextBlob(text)

#returns the sentiment of text along with value between -1 to +1
# neagtive values = negative sentiment, positive values = positive sentiment
sentiment = obj.sentiment.polarity
print(sentiment)
