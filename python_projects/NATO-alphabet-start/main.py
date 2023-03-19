import pandas


nato = pandas.read_csv(r"python_projects\\NATO-alphabet-start\\nato_phonetic_alphabet.csv")
nato_data_frame = pandas.DataFrame(nato)

nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}


def generate_nato():
    user_word = input("Enter a word to get NATO code: ").upper()
    try:
        user_nato = [nato_dict[letter] for letter in user_word]
    except SyntaxError:
        print("Sorry, only letters in the alphabet please.")
        generate_nato()
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_nato()
    else:
        print(user_nato)

generate_nato()
