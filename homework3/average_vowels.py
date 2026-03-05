# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 



def counting_vowels_and_consonants(text):
    
    vowels = "aeiouAEIOU"
    
    v_count = 0
    
    c_count = 0
    
    for char in text:
    
        if char.isalpha(): # Ensure it is a letter, not a space or punctuation
    
            if char in vowels:
    
                v_count += 1
    
            else:
    
                c_count += 1
                
    return (v_count, c_count)


def average_vowels_and_consonants(paragraph):
    
    # Split by period and remove any empty strings caused by trailing dots
    
    sentences = [s.strip() for s in paragraph.split('.') if s.strip()]
    
    num_sentences = len(sentences)
    
    if num_sentences == 0:
    
        return (0, 0.0, 0.0)
    
    total_vowels = 0
    
    total_consonants = 0
    
    for sentence in sentences:
    
        v, c = counting_vowels_and_consonants(sentence)
    
        total_vowels += v
    
        total_consonants += c
    
    
    avg_v = total_vowels / num_sentences
    
    avg_c = total_consonants / num_sentences
    
    return (num_sentences, avg_v, avg_c)


count, avg_v, avg_c = average_vowels_and_consonants(paragraph)


print(f"• Count of {count} sentences:")
print(f"• Average Vowels:    {avg_v:.2f} per sentence")
print(f"• Average Consonants: {avg_c:.2f} per sentence")