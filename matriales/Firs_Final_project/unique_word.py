def count_words(words):
    """Counts the occurrences of each unique word in the given list."""
    unique_words = set(words)  # Get unique words
    counts = {word: 0 for word in unique_words}  # Initialize counts for each unique word
    
    for word in words:  # Iterate through the original list of words
        counts[word] += 1  # Increment the count for each word

    return counts

# Example usage
words = ["Welcome", "Ali", "Hi", "Ali", "No", "Hi", "No", "Ali", "No", "Ali"]
word_counts = count_words(words)
print(word_counts)
