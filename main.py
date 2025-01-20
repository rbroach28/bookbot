def num_of_words(text):
  return len(text.split())

def character_count(text):
  characters_dict = {}
  words = text.lower().split()
  for char in text.lower():
    if char in characters_dict:
      characters_dict[char] += 1
    else:
      characters_dict[char] = 1
  return characters_dict

def print_report(text):
  words = num_of_words(text)
  characters_dict = character_count(text)
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{words} words found in the document \n")
  for char in characters_dict:
    print(f"The '{char}' character was found {characters_dict[char]} times")

def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    word_count = num_of_words(file_contents)
    character_count_dict = character_count(file_contents)
    print_report(file_contents)
main()
