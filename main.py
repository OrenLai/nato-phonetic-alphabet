
import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     # print(key)
#     # print(f"aaa{value[2]}")
#     if key == "student" and value[1] == "James":
#         print(value)
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     print(index)


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
# for (index, row) in df.iterrows():
#     print(f"letter = {row.letter} , code = {row.code}")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# print(nato_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
nato_list = [nato_dict[letter] for letter in word]
print(nato_list)
