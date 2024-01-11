import random, time

# The word_dict dictionary contains word : hint pairs.
word_dict = {
    "Delicious":"Adj. -Has good taste.",
    "Misery":"Noun - pain, mental or physical.",
    "Convolution":"Noun - Mathematical operation, often used in the field of Deep Learning.",
    "Activity":"Noun - excercise, movement, action",
    "Lasagna":"Noun - Italian food. Garfield",
    "Mario":"Noun - Name of an italian videogame character.",
    "Cookies":"Noun - Often cooked by grandmothers. Chocolate... ",
    "Companion":"Noun - A person or animal which accompanies somebody, is that person's ...",
    "Wolfswagen":"Noun - German car producer. Hitler. Das Auto"
}

word_list = [key for key in word_dict.keys()]

limit = 10
iteration = 0
states = ['   _____ \n'               
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n',  
            '   _____ \n'
                    '  |     | \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n',
            '   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n',
            '   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n',
            '   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     O \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n',
            '   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     O \n'
                    '  |     | \n'
                    '  |      \n'
                    '__|__\n',
            '   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     O \n'
                    '  |    /| \n'
                    '  |      \n'
                    '__|__\n',
            '   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     O \n'
                    '  |    /|\\n'
                    '  |      \n'
                    '__|__\n',
            '   _____ \n'
                    '  |     |  \n'
                    '  |     |  \n'
                    '  |     |  \n'
                    '  |     O  \n'
                    '  |    /|\ \n'
                    '  |    /   \n'
                    '__|__\n',
            '   _____ \n'
                    '  |     |  \n'
                    '  |     |  \n'
                    '  |     |  \n'
                    '  |     O  \n'
                    '  |    /|\ \n'
                    '  |    / \ \n'
                    '__|__\n',]  
guessed_words = []
guessed = False
print("This is a simple hangman game. \nYou have 10 tries to guess what word I'm thinking of.")
word = word_list[random.randint(0, len(word_list)-1)]
word_hint = word_dict[word]

def initialization():
    wants_to_start = input("Want to start? (y/n):")
    if wants_to_start.lower() == "y":
        time.sleep(0.5)
        print("Let's go!")
        
def game(iteration):
    print(states[iteration])
    guessed:str = input(f"The hint is: {word_hint}. \nYour guess is: ")
    guessed_words.append(guessed)
    if guessed != word:
        print("WRONG GUESS!")
        iteration += 1
        game(iteration)
    else:
        print(f"You win! \nIt took you {iteration} tries to guess correctly.")
        print(f"\nYour tries: {guessed_words}.")
        guessed_words.append("Guessed")
    
    
while iteration <= limit & guessed == False:
    if iteration == 0:
        initialization()
    game(iteration)
    if guessed_words[-1] == "Guessed":
        random.seed(iteration if iteration != 4 else random.randint(5, 12))
    iteration+=1
        