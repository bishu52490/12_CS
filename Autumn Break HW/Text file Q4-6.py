#Ques 4
def Show_words():
    with open("NOTES.TXT","r") as file:
        line = file.readline()          #return first line as string
        while line:                         #false when readline return empty string
            if len(line.split()) == 5:      #string split into individual words and stored in list
                                                    #and each elem is a word of the line so len of that list = no of word in line
                print(line[:-1])            #line[:-1] --> to remove extra newlines
            line = file.readline()      #for taking further lines


#Ques 5
def DISPLAYWORDS():
    with open("STORY.TXT","r") as file:
        line = file.readline()           #return first line as string
        while line:                          #false when readline return empty string
            words = line.split()        #string split into individual words and stored in list
            for word in words:          #takes each word from list (words)
                if len(word) < 4:
                    print(word)
            line = file.readline()          #for taking further lines as string and return empty string after last line
#OR
def DISPLAYWORDS():
    with open("STORY.TXT","r") as file:
        content = file.read()
        words = content.split()
        for word in words:          #takes each word from list (words)
            if len(word) < 4:
                print(word)

#Ques 6
def AMCount():
    a_count = 0
    m_count = 0
    with open("STORY.TXT","r") as file:
        line = file.readline()                       #return first line as string
        while line:                                      #false when readline return empty string
            for char in line:                       #takes each character from string (line)
                if char.lower() == 'a':             #lower the case of the char and check if it is 'a' or not
                    a_count += 1                    #add 1 to a_count if char is 'a'
                #similarly
                elif char.lower() == 'm':
                    m_count+=1                  #add 1 to m_count if char is 'm'
            line = file.readline()
            
    #at last print results
    print(f"The Alphabet 'a' occured {a_count} times and 'm' occured {m_count} times ")

#OR
def AMCount():
    with open("STORY.TXT","r") as file:
        content = file.read()                               #reads everything in file
        a_count = content.lower().count('a')        #lowercase all content then count occurence of 'a'
        m_count = content.lower().count('m')     #lowercase all content then count occurence of 'a'
        #at last print results
    print(f"The Alphabet 'a' occured {a_count} times and 'm' occured {m_count} times ")
