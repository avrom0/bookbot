import os

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path_to_file = os.path.join(script_dir, "books", "frankenstein.txt")
    with open(path_to_file) as f:
        file_contents = f.read()

    letter_counts = {}

    lowered_text = file_contents.lower()
    for letter in lowered_text:
        if letter.isalpha() == True:
            if letter not in letter_counts:
                letter_counts[letter] = 1
            else:
                letter_counts[letter] += 1
   
       # Convert dictionary into a list of tuples and sort by count
    sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Print each letter and its count
    for char, count in sorted_letters:
        print(f"The '{char}' character appears {count} times")
   
   # print(letter_counts)
    
    
    
    
    #    words = file_contents.split()
    #    print(len(words))
    #    print(file_contents[:100])

if __name__ == "__main__":
    main()