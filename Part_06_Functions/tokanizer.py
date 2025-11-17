"""Program for tokenizing text."""


def get_user_text() -> str | None:
    """Get input from user and validate if the input is correct."""


def parse_text_to_tokens(text: str) -> list[str]:
    """Tokenize the input text."""
    return []


def main() -> None:
    """Run the tokenizer."""
    text = get_user_text()
    if not text:
        print("Validation of the input text failed! Try again!")
        return

    tokenized_text = parse_text_to_tokens(text)
    print(f"TOKENIZED TEXT: {tokenized_text}")


main()
