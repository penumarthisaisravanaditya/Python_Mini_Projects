print("Palindrome Checker")
print("-" * 30)
text = input("Enter Your Word Here:")
text = text.lower()
reverse_text = text[::-1]
if reverse_text == text:
    print("===== Palindrome =====")
else:
    print("===== Not a Palindrome =====")


print("Thank You for Using This Palindrome Checker!")