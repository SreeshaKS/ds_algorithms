from collections import defaultdict, deque


def wordLadder(beginWord, endWord, wordList):
  
  if endWord not in wordList or not endWord or not beginWord or not wordList:
    return -1
  
  if len(beginWord) is not len(endWord):
    return -1
  
  
  L = len(beginWord)
  
  allCombo = {}
  for w in wordList:
    allCombo[w] = []
  # Dog ----> D*g <---- Dig
  for word in wordList:
    for i in range(L):
        try:
            allCombo[word[i]+"*"+word[i+1:]].append(word)
        except:
            allCombo[word[i]+"*"+word[i+1:]] = []
            allCombo[word[i]+"*"+word[i+1:]].append(word)
      
  queue = deque([(beginWord,1)])
  visited= {beginWord: True}
  while queue:
    currentWord, level = queue.popleft()
    
    for i in range(L):
      
      intermediateOption  = currentWord[:i]+"*"+currentWord[i+1:]

      for word in allCombo[intermediateOption]:
        if word == endWord:
          return level
        
        if word not in visited:
          visited[word] = True
          queue.append((word, level+1))
      
      allCombo[intermediateOption] = []
  
  return -1
print(wordLadder("hit","cog",["hot","dot","dog","lot","log","cog"] ))