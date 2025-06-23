def check_palindrome():
    text = input("no lemon: ")
    # Remove spaces and punctuation, convert to lowercase
    cleaned = ''.join(char.lower() for char in text if char.isalnum())

    if cleaned == cleaned[::-1]:
        print(f'"{text}" is a palindrome.')
    else:
        print(f'"{text}" is not a palindrome.')

check_palindrome()