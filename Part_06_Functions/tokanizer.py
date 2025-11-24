"""Program for tokenizing text."""


def get_user_text() -> str | None:
    """Get input from user and validate if the input is correct."""
    user_input = input("Enter text to tokenize: ")
    if not user_input:
        print("Text should not be empty!")
    return user_input


def parse_text_to_tokens(text: str) -> list[str]:
    """Tokenize the input text."""
    text = text.strip().lower()
    text_splitted = text.split()
    cleaned_words = []
    for word in text_splitted:
        for char in word:
            if not char.isalpha():
                word = word.replace(char, "")  # noqa: PLW2901
        cleaned_words.append(word)
    return list(set(cleaned_words))


def main() -> None:
    """Run the tokenizer."""
    text = get_user_text()
    if not text:
        print("Validation of the input text failed! Try again!")
        return

    tokenized_text = parse_text_to_tokens(text)
    print(f"TOKENIZED TEXT: {tokenized_text}")


main()
