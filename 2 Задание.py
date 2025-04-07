def count_unique_chars(text: str):
    char = set(text)
    return len(char)


print(count_unique_chars('hello'))