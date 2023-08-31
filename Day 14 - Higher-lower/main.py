from art import logo, vs
from game_data import data
from random import choice
from os import system


def higher_lower():
    score = 0
    playing = True
    print(logo)
    choice_a = choice(data)

    while playing:
        print(
            f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
        print(vs)
        choice_b = choice(data)
        print(
            f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")
        player_choice = input(
            "Who has more followers? Type 'A' or 'B': ").lower()
        most_followers = max(
            choice_a['follower_count'], choice_b['follower_count'])
        if player_choice == 'a':
            player_choice = choice_a
        else:
            player_choice = choice_b
        system("cls")
        print(logo)
        if player_choice["follower_count"] == most_followers:
            score += 1
            print(f"You're right! Current score: {score}")
            choice_a = choice_b
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            playing = False


higher_lower()
