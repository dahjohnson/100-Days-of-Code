def calculate_love_score(name1, name2):
    TRUE_VAR = "TRUE"
    LOVE_VAR = "LOVE"
    first_word = 0
    second_word = 0

    for x in name1.upper():
        if x in TRUE_VAR:
            first_word += 1
        if x in LOVE_VAR:
            second_word += 1

    for y in name2.upper():
        if y in TRUE_VAR:
            first_word += 1
        if y in LOVE_VAR:
            second_word += 1

    score = str(first_word) + str(second_word)
    print(f"Love Score = {score}")


name1 = input("Enter the first person's full name here: ")
name2 = input("Enter the second person's full name here: ")
calculate_love_score(name1, name2)
# calculate_love_score("Kanye West", "Kim Kardashian")
