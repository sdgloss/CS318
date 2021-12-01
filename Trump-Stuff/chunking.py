import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import PunktSentenceTokenizer





def chunking():
  #organizeData() #only need these uncommented when updating the training data

  #gets files
  File1 = open("tweets/training.txt", "r")
  File2 = open("tweets/sample.txt", "r")


  #turns files into text strings
  for columns in (raw.strip() for raw in File1):  
    train_text = str(columns)
  for columns in (raw.strip() for raw in File2):  
    sample_text = str(columns)



  custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
  tokenized = custom_sent_tokenizer.tokenize(sample_text)
  print(len(tokenized))
  processData(tokenized)
  






def processData(tokenized):
  #try:
    for c in range (len(tokenized)):
      i = tokenized[c]
      words = nltk.word_tokenize(i)
      tagged = nltk.pos_tag(words)
      chunkGram = r"""
       CHUNK: {<RB.?>*<VB.?>*<NNP>+<NN>?}
       NMS: {<NN>*<NNP>}
       NP: {<VB|NMS|JJ|RB.*>+}
       NP: {<NMS>?<VB>?<CC>?<JJ>*<VB>+}"""
      chunkParser = nltk.RegexpParser(chunkGram)
      chunked = chunkParser.parse(tagged)
      addData(chunked.pformat())
      print (c)

    

  #except Exception as e:
      #  print(str(e))


def addData(chunked):

  sentenceStruct = ""
  chunks = chunked.split("\n")
  for i in range (len(chunks)):
    lined = chunks[i]
    line = lined.replace(")", "")
    if (len(line) >> 2 and line[2] == "("):
        while(line and line[0] == " "):
         line = line[1: len(line)]
        lines = line.split(" ")
        holder = [[0 for x in range(2)]for y in range(len(lines))]
        firstChar = lines[0]
        
        if (len(firstChar) >> 1 and firstChar[1] == "N"):
          path = "corpora/NP.txt"
          if (len(lines) >> 1):
           for i in range (len(lines) - 1):
            holder[i] = processWord(lines[i +1])
            sentenceStruct += "<NP> "
            word = ""
            for i in range (len(holder) - 1):
              word += str(holder[i][0]) + " "
            editFile(path, word)


        elif (len(firstChar) >> 1 and firstChar[1] == "C"):
         path = "corpora/CHUNK.txt"
         if (len(lines) >> 1):
          for i in range (len(lines) - 1):
            holder[i] = processWord(lines[i +1])
  
           
          sentenceStruct += "<CHUNK> "
          word = ""
          for i in range (len(holder) - 1):
            word += str(holder[i][0]) + " "
          editFile(path, word)

    elif(len(line) >>2):
        while(line and line[0] == " "):
          line = line[1: len(line)]
        lines = line.strip(" ")
        holder = processWord(lines) 

        sentenceStruct += "<" + holder[1] + "> "
        holder[1] = "corpora/" + holder[1] + ".txt"
        editFile(holder[1], holder[0])

  editFile("corpora/Sentence.txt", sentenceStruct)

     
  

def editFile(filepath, word):
  if (str(word) != "0"):
    if(filepath == "corpora/Sentence.txt"):
      if(str(word) != "<.>"):
        fileWrite=open(filepath,'a')
        fileWrite.write(str(word) + "|")
        fileWrite.close()
    
    else:
      fileWrite=open(filepath,'a')
      fileWrite.write(str(word) + "\n")
      fileWrite.close()


def processWord(string):
  #turns the word into a word and a type 
  parts = [0 for x in range(2)]
  hold = ""
  for i in range (len(string)):
    if (string[i] != "/"):
      if (string[i] != " "):
        hold += string[i]
    else:
        parts[0] = hold
        hold = ""
  
  parts[1] = hold

  return parts




def organizeData():
  r = 34213
  tweets = [0 for x in range(r)]
  File1 = open("tweets/SortedTweets.txt", "r")
  counter = 0
  for columns in (raw.strip() for raw in File1):  
      tweets[counter] = columns
      counter += 1
  fileWrite=open("tweets/training.txt",'w')
  for i in range (int(len(tweets)/10)):
    fileWrite.write(tweets[i])
  fileWrite.close()

  file2Write=open("tweets/sample.txt",'w')
  for i in range (int(len(tweets)/10), len(tweets)):
    file2Write.write(tweets[i])
  file2Write.close()

  #need a more random method for data selection, otherwise will run into overfitting I imagine

