import re

def extract_data(text, data_type):
    if data_type == 'email':
        return extract_email_addresses(text)
    elif data_type == 'phone':
        return extract_phone_numbers(text)
    elif data_type == 'credit_card':
        return extract_credit_card_numbers(text)
    elif data_type == 'hashtag':
        return extract_hashtags(text)
    else:
        return []

def extract_email_addresses(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return re.findall(email_pattern, text)

def extract_phone_numbers(text):
    phone_pattern = r'(?:\+\d{1,3}\s?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{3,4}'
    return re.findall(phone_pattern, text)

def extract_credit_card_numbers(text):
    pattern = r'\b(?:\d{4}[ -]?){3}\d{4}\b'
    return re.findall(pattern, text)

def extract_hashtags(text):
    hashtag_pattern = r'#\w+'
    return re.findall(hashtag_pattern, text)

def process_text(text):
    print("\n--- Extracted Data ---")
    for dtype in ['email', 'phone', 'credit_card', 'hashtag']:
        matches = extract_data(text, dtype)
        print(f"\n{dtype.capitalize()}s:")
        if matches:
            for item in matches:
                print(f"- {item}")
        else:
            print("- None found")

if __name__ == "__main__":
    paragraph = """
    Hey, it's Garang here—reach me at garang.buke@example.com, or maybe at my backup: garang_at_mail.com (invalid format). You can also try my old one: garang.buke123@old-school-email.net.
Buke left a note with his number written as (254) 712-345-678, but sometimes he uses +254712345678 or just 0712 345 678. In older forms, he once wrote it as 0712.345.678 or even 0712-345678.
Oh, and someone leaked what looked like his card: 4111-1111-1111-1111, though one version was missing a digit: 4111 1111 1111 111. Another fake one showed up as 1234-5678-9012-345x (invalid character).
I keep my emergency backup in this format: 5500 0000 0000 0004.

Emails were bouncing when sent to buke@@mail.com (double @), but others worked like buke.dev@tech.io and buke_99@students.alustudent.com.
Someone once mistyped mine as garang.buke@.com (missing domain). I’ve seen many typos like buke@mail, buke@com, and buke@company.c (short domain).
We were both trending with #GarangRocks and #TeamBuke, but I saw people also used # (invalid) or just #123 (numeric tag). Some got creative with #Garang_Buke_2024 and #GoGarangGo!, though punctuation breaks the hashtag.
Even #hello#world showed up (double hash). Buke launched a fan challenge tagged #Buke4President and someone tried tagging with #!fail (invalid start).

If you ever need to reach our old office, the contact was listed as 123-456-7890 (US format), which confused people, since it was followed by +1 (123) 456-7890 too.
For international friends, we shared a weird listing: +44 (0) 20 7946 0958 and 0207.946.0958.
Garang keeps a list of fake test cards too: 4242 4242 4242 4242 and 4012-8888-8888-1881.
Just don’t try them online! Some were poorly written like 4000-0000-0000 (missing block), or 1234-5678-9012-34567 (too long).
Let us know what you find—email us at support@garangbuke.org or fake@domain (invalid) and tag us on social with #RegexIsFun.
    """

    print("------------------------------------------------------------------------")
    print("From the paragraph below, this is the data extracted:\n")
    print(paragraph.strip())

    print("\n--- Edge Cases Included ---")
    print("• Emails: valid + malformed (missing '@') → 'garang.buke@example.com', 'garang_at_mail.com'")
    print("• Phones: multiple formats → '(254) 712-345-678', '+254712345678', '0712 345 678'")
    print("• Credit cards: correct and incorrect (short by one digit) → '4111-1111-1111-1111', '4111 1111 1111 111'")
    print("• Hashtags: valid and malformed → '#GarangRocks', '#', '#123'")

    process_text(paragraph)

    while True:
        response = input("\nWould you like to test your own text? (yes/no): ").strip().lower()
        if response == 'yes':
            user_text = input("\nEnter your custom text:\n")
            process_text(user_text)
        elif response == 'no':
            print("Program terminated.")
            break
        else:
            print("Please enter 'yes' or 'no'.")

