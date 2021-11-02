import re

def read_template(Filepath):
   """
   This function used to open and read a file
   """
   with open(Filepath)as file:
     return file.read()

def parse_template(textContent):
  """
    This function used parse the text into usable one
  """
  testing=re.findall(r'{(.*?)}',textContent)
  x= tuple(testing)
  testing1=re.sub(r'{(.*?)}',"{}",textContent)

  return testing1,x


def merge(file,inputs):
    """
    This function used to merge the values from user input to the correct place
    """


    testing1=file.format(*inputs)
    return testing1

def write_new_file(content):
    """
    This function write content wanted to a new file or override that file content
    """
    with open('assets/video_game_result.txt', 'w') as video_game:
        video_game.write(content)


if __name__=="__main__":

    print("""
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                   Welcome to madlib Game in here you will enter
     some Adjectives and nouns to finally display the text contained the names u chose
     +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    """
    )
    words=read_template("assets/video_game.txt")
    testing=re.findall(r'{(.*?)}',words)

    arrayWanted=[]
    for i in testing:
        userInput=input(f'Please enter a {i} ')
        arrayWanted.append(userInput)


    arrayWanted2=tuple(arrayWanted)
    print(arrayWanted2)

    textModify=re.sub(r'{(.*?)}',"{}",words)

    print (textModify)

    print(merge(textModify,arrayWanted2))


    write_new_file(merge(textModify,arrayWanted2))
  


# text1=text.split(" ")

# y=['x1','x2']
# x=""

# counter=0
# for index,i in enumerate(text1):


#     if index<len(y):
#         x=(i.format(Adjective = y[counter]))
    
#         print(x)
      
        


# def userInput():
#     word="hi"
#     /{(.*?)}/
#     x1=input(f"please enter {word}")
   

# userInput()


# txt = "For only {noun} dollars!"
# print(txt.format(noun = "hi"))
