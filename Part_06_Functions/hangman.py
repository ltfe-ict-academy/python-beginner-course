"""Hangmen Game."""

import random

MAXIMAL_NUMBER_OF_LIVES = 8
ALL_WORDS_STRING = "about, above, abuse, accept, accident, accuse, across, activist, actor, administration, admit, adult, advertise, advise, affect, afraid, after, again, against, agency, aggression, agree, agriculture, force, airplane, airport, album, alcohol, alive, almost, alone, along, already, although, always, ambassador, amend, ammunition, among, amount, anarchy, ancestor, ancient, anger, animal, anniversary, announce, another, answer, apologize, appeal, appear, appoint, approve, archeology, argue, around, arrest, arrive, artillery, assist, astronaut, astronomy, asylum, atmosphere, attach, attack, attempt, attend, attention, automobile, autumn, available, average, avoid, awake, award, balance, balloon, ballot, barrier, battle, beauty, because, become, before, begin, behavior, behind, believe, belong, below, betray, better, between, biology, black, blame, bleed, blind, block, blood, border, borrow, bottle, bottom, boycott, brain, brave, bread, break, breathe, bridge, brief, bright, bring, broadcast, brother, brown, budget, build, building, bullet, burst, business, cabinet, camera, campaign, cancel, cancer, candidate, capital, capture, career, careful, carry, catch, cause, ceasefire, celebrate, center, century, ceremony, chairman, champion, chance, change, charge, chase, cheat, cheer, chemicals, chemistry, chief, child, children, choose, circle, citizen, civilian, civil, rights, claim, clash, class, clean, clear, clergy, climate, climb, clock, close, cloth, clothes, cloud, coalition, coast, coffee, collapse, collect, college, colony, color, combine, command, comment, committee, common, communicate, community, company, compare, compete, complete, complex, compromise, computer, concern, condemn, condition, conference, confirm, conflict, congratulate, Congress, connect, conservative, consider, constitution, contact, contain, container, continent, continue, control, convention, cooperate, correct, corruption, cotton, count, country, court, cover, crash, create, creature, credit, crime, criminal, crisis, criticize, crops, cross, crowd, crush, culture, curfew, current, custom, customs, damage, dance, danger, daughter, debate, decide, declare, decrease, defeat, defend, deficit, define, degree, delay, delegate, demand, democracy, demonstrate, denounce, depend, deplore, deploy, depression, describe, desert, design, desire, destroy, detail, detain, develop, device, dictator, different, difficult, dinner"  # noqa: E501

all_words = ALL_WORDS_STRING.split(", ")
winning_word = random.choice(all_words)  # noqa: S311
current_incorrect_letters = set()
current_guessed_letters = set()


def validate_string_is_single_character(input_string: str) -> bool:
    """Validate if input is an valid single alpha character."""
    if len(input_string) != 1 or not input_string.isalpha():
        print("Input is not valid!")
        return False
    return True


def main() -> None:
    """Run main function for the program."""
    print("***** Welcome to Hangman Game! *****")
    while True:
        # 1. Step: Show currently guessed letters
        output_string = ""
        for letter in winning_word:
            if letter in current_guessed_letters:
                output_string += letter
            else:
                output_string += "_"
            output_string += " "
        print(f"\nCURRENT STATUS: {output_string.upper()}")
        print(
            f"Used letters: {', '.join(list(current_incorrect_letters))}  \
LIVES: {(MAXIMAL_NUMBER_OF_LIVES - len(current_incorrect_letters)) * '* '}",
        )

        # 2. Step: Get user input and validate it
        user_input_char = input("Enter a letter to guess: ")
        if not validate_string_is_single_character(user_input_char):
            continue

        # 3. Step: Check if the letter is in the winning word
        if user_input_char in winning_word:
            print("Yey, good guess!")
            current_guessed_letters.add(user_input_char)
        else:
            print("Try again!")
            current_incorrect_letters.add(user_input_char)

        # 4. Check game status
        ## a) User guessed all the letters
        if set(winning_word) == current_guessed_letters:
            print(f"You won the game! The winning word is: {winning_word.upper()}")
            break
        ## b) User don't have lives
        if len(current_incorrect_letters) >= MAXIMAL_NUMBER_OF_LIVES:
            print(f"Game over... The word is {winning_word.upper()}")
            break


main()
