def is_palindrome(text):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

# Example usage
user_input = input("Enter a word or phrase: ")
if is_palindrome(user_input):
    print("✅ It's a palindrome!")
else:
    print("❌ Not a palindrome.")
