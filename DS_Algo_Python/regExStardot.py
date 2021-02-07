def is_match(text, pattern):
    i = 0
    j = 0
    lT = len(text)
    lP = len(pattern)
    
    if text == pattern:
      return True
    
    while i < lT and j < lP:
        if pattern[j] == ".":
            i += 1
        elif j+1 < lP and pattern[j+1] == "*":
            x = i
            
            if text[x] != pattern[j]:
              i+=1
              j+=2
              continue;
              
            while x < lT and text[x] == pattern[j]:
                x += 1
            
            i = x
        elif pattern[j] == text[i]:
            i += 1
        j += 1
        
    if i == lT:
      return True
    
    return False