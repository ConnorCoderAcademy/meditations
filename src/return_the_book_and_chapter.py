import json

from meditations_text import meditations

import os 
# Set a variable to correlate with each dictionary value in the meditations dictionary (each dictionary key is one chapter and each subchapter is a list item in the dicitonary value)
meditations_book_1 = meditations["1"]
meditations_book_2 = meditations["2"]
meditations_book_3 = meditations["3"]
meditations_book_4 = meditations["4"]
meditations_book_5 = meditations["5"]
meditations_book_6 = meditations["6"]
meditations_book_7 = meditations["7"]
meditations_book_8 = meditations["8"]
meditations_book_9 = meditations["9"]
meditations_book_10 = meditations["10"]
meditations_book_11 = meditations["11"]
meditations_book_12 = meditations["12"]




book_list = [meditations_book_1, meditations_book_2, meditations_book_3, meditations_book_4, meditations_book_5, meditations_book_6, meditations_book_7, meditations_book_8, meditations_book_9, meditations_book_10, meditations_book_11, meditations_book_12]

def next_step():
    next_step = input("\nWould you like to search for another chapter? (Y/N): ")
    if next_step == "Y":
            return_book_and_chapter()
    elif next_step == "y":
            return_book_and_chapter()
    elif next_step == "N":
            os.system('cls||clear')
    elif next_step == "n":
            os.system('cls||clear')
    else: 
        return_book_and_chapter() 


def return_book_and_chapter():
    meditations_book_chosen = int(input("Which Book Would You Like to Search (1 to 12)?: "))
    meditations_chapter_chosen = int(input("Which chapter would you like? : "))
   # Correct for zero-indexing so when a user inputs a book chapter, the numerical value will be one less than what they chose (e.g. chapter 2 is index 1)
    meditations_chapter_chosen_index_correction = int(meditations_chapter_chosen) - 1
    if meditations_book_chosen == 1:
        print("\n", meditations_book_1[meditations_chapter_chosen_index_correction], "\n")
        next_step()
    elif meditations_book_chosen == 2:
        print(meditations_book_2[meditations_chapter_chosen_index_correction])
        next_step()
    elif meditations_book_chosen == 3:
        print(meditations_book_3[meditations_chapter_chosen_index_correction])
        next_step()
    elif meditations_book_chosen == 4:
        print(meditations_book_4[meditations_chapter_chosen_index_correction])
        next_step()
    elif meditations_book_chosen == 5:
        print(meditations_book_5[meditations_chapter_chosen_index_correction])
        next_step()
    elif meditations_book_chosen == 6:
        print(meditations_book_6[meditations_chapter_chosen_index_correction])
        next_step()
    elif meditations_book_chosen == 7:
        print(meditations_book_7[meditations_chapter_chosen_index_correction])
        next_step()
    elif meditations_book_chosen == 8:
        print(meditations_book_8[meditations_chapter_chosen_index_correction])
        next_step()
    elif meditations_book_chosen == 9:
        print(meditations_book_9[meditations_chapter_chosen_index_correction])
        next_step()
    elif meditations_book_chosen == 10:
        print(meditations_book_10[meditations_chapter_chosen_index_correction])
        next_step()
    elif meditations_book_chosen == 11:
        print(meditations_book_11[meditations_chapter_chosen_index_correction])
        next_step()
    elif meditations_book_chosen == 12:
        print(meditations_book_12[meditations_chapter_chosen_index_correction])
        next_step()
    else: 
        input("\nBook ", meditations_book_chosen, " does not have that many chapters! Please any key to choose again.\n")
        return_book_and_chapter()