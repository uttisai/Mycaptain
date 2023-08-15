def most_frequent(string):
   
    letter_freq = {}

    for letter in string:
        if letter.isalpha():  
            letter = letter.lower()  
            if letter in letter_freq:
                letter_freq[letter] += 1
            else:
                letter_freq[letter] = 1

    sorted_freq = sorted(letter_freq.items(), key=lambda item: item[1], reverse=True)

    for letter, freq in sorted_freq:
        print(f"{letter} = {freq:02d}")

input_string = input("Please enter a string: ")
most_frequent(input_string)
