import random
import art
import game_data

print(art.logo)

user_score = 0
keep_playing = True
option_A = game_data.data[(random.randint(0, 49))]


while keep_playing:
    option_B = game_data.data[(random.randint(0, 49))]
    print(f'Compare A: {option_A["name"]}, a {option_A["description"]}, from {option_A["country"]}.')
    print(art.vs)
    print(f'Compare B: {option_B["name"]}, a {option_B["description"]}, from {option_B["country"]}.')
    users_choice = input('Who has more followers? Type "A" or "B": ').upper()

    if users_choice == "A":
        users_choice = option_A
        if users_choice["follower_count"] > option_B["follower_count"]:
            user_score += 1
            print(f"You're right! Current score: {user_score}")
            option_A = option_B
        elif users_choice["follower_count"] < option_B["follower_count"]:
            print(f"Sorry, that's wrong. Final score: {user_score}")
            keep_playing = False
    elif users_choice == "B":
        users_choice = option_B
        if users_choice["follower_count"] > option_A["follower_count"]:
            user_score += 1
            print(f"You're right! Current score: {user_score}")
            option_A = option_B
        elif users_choice["follower_count"] < option_A["follower_count"]:
            print(f"Sorry, that's wrong. Final score: {user_score}")
            keep_playing = False

