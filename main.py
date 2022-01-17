# Random word from list
# display equal dashes
# input of guess -
# difficulty level
import random

list_of_alphabets = ["butter", "naan", "tandoori", "chicken", "daal","fry", "chai", "garam"]
random_word = random.choice(list_of_alphabets)
#print(random_word)
print(len(random_word))
word_list = []
random_len = len(random_word)
for i in range(0,random_len):
    word_list += random_word[i]
lives = random_len -2
y =""
dash = "_"
dash_list = []
empty_var = ""
for temp in range(0,random_len):
    dash_list += "_"
#dash_list has now generated w the same no. of dashes as the allotted word



def indices(insert_list, element):
    result = []
    offset = -1 #-1 as an index denotes last position
    while True:
        try:
            offset = insert_list.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)


# newlist = ['t','a','n','d','o','o','r','i']
#
# templist = indices(newlist,'o')
# print(templist)


def compare(userchoice,randomword,temp_list,temp_index):
    counter = 0
    #temp_list is dash wala list
    #temp_index is where the list which is the output of the indices function will go
    for x in userchoice:
        for y in randomword:
            if x == y:
                temp_list[temp_index[counter]] = user_choice
                counter+=1

for x in range(0, len(random_word)):
    y += dash
print(y)

while lives>0:
    lives -=1
    proceed = int(input("DO YOU WANT TO GUESS THE WORD OR A LETTER? '1' for Word and '2' for Letter.\n"))
    if proceed == 1:
        user_entered_word = str(input("Enter your guess of the word"))
        if user_entered_word.lower() == random_word:
            print(random_word + "\nYOUR ANSWER IS CORRECT!! WOOHOOOO!!")
            break
        else:
            print("WRONG WORD")
            break
    elif proceed == 2:
        user_choice = input("Enter a letter: \n")
        word = ""
        templist = indices(word_list,user_choice)
        #temlist_index = len(templist)

        # templist now has the indices of the userchoice letter in our string

        compare(user_choice,random_word,dash_list,templist)
        #dash_list will now have replaced dashes with the userchoice letter

        for i in range(0,len(dash_list)):
            word += dash_list[i]
        print(word+"\n")
        print("Lives Remaining: "+lives)
