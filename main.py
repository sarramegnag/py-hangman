import random

def display_hangman(num_tries):
  print(" ____")
  print("|    |")
  print("|    %s" % ("O" if num_tries >= 1 else " "))
  print("|   %s%s%s" % ("/" if num_tries >= 3 else " ", "|" if num_tries >= 2 else " ", "\\" if num_tries >= 4 else " "))
  print("|   %s %s" % ("/" if num_tries >= 5 else " ", "\\" if num_tries >= 6 else " "))

def get_word_to_display(letters, word):
  word_to_display = ""

  for letter in word:
    if letter.lower() in letters:
      word_to_display += letter
    else:
      word_to_display += "_"

  return word_to_display

words = [
  "Serviette",
  "Poivre",
  "Chaise",
  "Vert",
  "Ventre",
  "Parapluie",
  "Goupille",
  "Pantalon",
  "Botte",
  "Girafe"
]

stop_game = False
max_tries = 6

while not stop_game:
  num_tries = 0
  letters = ""

  random_number = random.randint(0, len(words) - 1)

  word_to_find = words[random_number]

  while num_tries != max_tries and "_" in get_word_to_display(letters, word_to_find):
    answer = ""
    while len(answer) != 1:
      answer = input("Quelle lettre voulez-vous ? ")
      if len(answer) != 1:
        print("Vous devez proposer une lettre")
        
    letter = answer[0].lower()
    letters += letter

    if not letter in word_to_find.lower():
      num_tries += 1
      display_hangman(num_tries)

    print("Mot à trouver : " + get_word_to_display(letters, word_to_find))

  if num_tries == max_tries:
    print("Vous avez perdu ! Le mot était \"%s\"" % (word_to_find))
  else:
    print("Vous avez gagné malgré %d erreurs ! Le mot était \"%s\"" % (num_tries, word_to_find))

  stop_game = input("Voulez-vous recommencer ? O/n ")[0].lower() == "n"
