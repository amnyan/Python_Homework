def count_words_in_file(file_path, words_to_count):
    word_counts = {word: 0 for word in words_to_count}

    fd = open(file_path, 'r')
    for line in fd:
        words = line.split()
        for word in words:
            cleaned_word = word.strip('.,!?;:"()').lower()
            if cleaned_word in word_counts:
                word_counts[cleaned_word] += 1

    fd.close()
    return word_counts

file_path = 'sample_text.txt'
words_to_count = ["example", "all", "word", "up", "did", "him"]
word_counts = count_words_in_file(file_path, words_to_count)

for word, count in word_counts.items():
    print(f"The word '{word}' appears {count} times in the file.")

