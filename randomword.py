import requests
from bs4 import BeautifulSoup


#url = "https://randomword.com/"
#try:
#response = requests.get(url)

#print(response.text)
   # soup = BeautifulSoup(response.content, 'html.parser')
   # english_words

#Creating function, which will receive information
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        #print(response.text)
#Creating Soup object

        soup = BeautifulSoup(response.content, "html.parser")
#Inputing command. text.strip(), removes all space from result
        english_words = soup.find("div", id ="random_word").text.strip()
#Get description of the word
        word_definition = soup.find("div", id = "random_word_definition").text.strip()
#For purpose return program to dictionary
        return {
            "english_words": english_words,
            "word_definition": word_definition
            }
#Function, that will report error but not stop program
    except:
        print("Error occured")
#Creat function that will made game itself
def word_game():
    print("Wellcome to play")
    while True:
#Create a function to use the result of the dictionary function
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")
#Start play
        print(f"Meaning of the word - {word_definition}")
        user = input("What word is this?")
        if user == word:
            print("Correct")
        else:
            print(f"Incorrect, it was this word - {word}")
#Creat an opportunity to finish the game

        play_again = input('Do you want another more? y/n')
        if play_again != "y":
            print("Thanks for play!")
            break
word_game()






