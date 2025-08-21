import ass_4 as mp
function_map = {
    1: mp.happy_number,
    2: mp.string_permutations,
    3: mp.count_vowel_words,
    4: mp. number_to_words,
    5: mp.pascal_triangle,
    6: mp.smith_number,
    7: mp.longest_word,
    8: mp.dice_roll_game,
    9: mp.binary_search,
    10: mp.trimorphic_number,
}
while True:
    print('''
------ FUNCTION MENU ------
1. Check if a Number is a Happy Number
2. Generate All Permutations of a String
3. Count Words Starting with a Vowel
4. Convert Number to Words
5.  Print Pascal's Triangle
6. Check if a Number is a Smith Number
7.Find the Longest Word in a Sentence
8. Dice Roll Game
9. Binary Search
10.Check if a Number is a Trimorphic Number
0. Exit
---------------------------''')
    
    choice = int(input("Enter your choice: "))
    if choice > 0 and choice <= len(function_map):
        function_map[choice]()
    elif choice == 0:
        break
    else:
        ("Invalid choice")
