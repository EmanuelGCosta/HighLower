from random import randint
import art
from game_data import data


def random_person(random):
    return data[random]


def the_game():
    print(art.logo)
    points = 0
    list_len = len(data)
    random1 = randint(0, list_len - 1)
    error = False
    person1 = random_person(random1)

    while not error:
        if points != 0:
            print(f"You're right! Current score: {points}")

        print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}.")
        followers1 = int(person1['follower_count'])
        print(art.vs)

        random2 = randint(0, list_len - 1)
        person2 = random_person(random2)
        print(f"Compare B: {person2['name']}, a {person2['description']}, from {person2['country']}.")
        followers2 = int(person2['follower_count'])

        while person1 == person2:
            random2 = randint(0, list_len - 1)
            person2 = random_person(random2)

        if followers1 >= followers2:
            answer = 'a'
        else:
            answer = 'b'

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess == answer:
            points += 1
            person1 = person2
            print("\n\n\n\n\n\n\n\n")
        else:
            print(f"Sorry, that's wrong. Final score: {points}")
            error = True


the_game()



