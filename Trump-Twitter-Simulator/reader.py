#remove white space from tweets :(


def reader():
  openFiles()

def openFiles():
  #opens up all tweets, gets rid of the white space that was added from the scraping
  r = 55924 #this will change if we use a different data set, too lazy to set this for computer to determine it. i'd probably use numpy arrays
  tweets = [0 for x in range(r)]
  File1 = open("tweets/tweets.txt", "r")
  counter = 0
  for columns in (raw.strip() for raw in File1):  
    if not (len(columns) == 0):
      tweets[counter] = columns
      counter += 1
  
  
  saveTweets(remove(tweets))
  

def remove(tweets):
  #removes the tweets that are retweets or links
  return removeHTTP(removeRT(tweets))



def removeRT(tweets):
  #removes the retweets
  r = 46667 #same thing as before, just determine length before
  updatedTweets = [0 for x in range(r)]
  counter = 0
  for i in range(len(tweets)):
    words = tweets[i].split()
    if "RT" not in words[0]:
      updatedTweets[counter] = tweets[i]
      counter += 1

  return (updatedTweets)





def removeHTTP(tweets):
   #removes the link holding tweets, hard to reproduce
  r = 34213 #same thing as before, just determine length before
  updatedTweets = [0 for x in range(r)]
  counter = 0
  for i in range(len(tweets)):
    if "ttp" not in str(tweets[i]):
      updatedTweets[counter] = tweets[i]
      counter += 1


  return (updatedTweets)
 
  
  
def saveTweets(tweets):
  #saves the tweets into text file SortedTweets.txt
  fileWrite=open("tweets/SortedTweets.txt",'w')
  for i in range (len(tweets)):
    fileWrite.write(tweets[i] + "\n")
  fileWrite.close()
