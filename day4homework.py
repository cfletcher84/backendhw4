# # # The Range Riddle
import random
mood = ("Happy", "Sad", "Energetic", "Calm")
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

for i in range(len(days_of_week)):
    print(f"On {days_of_week[i]} you were feeling {random.choice(mood)}")

# Double Scoop with Nested loops

time_of_day = ("Morning", "Afternoon", "Evening")

for x in range(len(days_of_week)):
    for y in range(len(time_of_day)):
            print(f"On {days_of_week[x]} you were feeling {random.choice(mood)} in the {time_of_day[y]}")

# Loop Comdition Logic

hour_int = 0

while True:
    hour_int += 1
    print("This loop will never end")
    if hour_int >= 5:
        break

# Task 2

while hour_int < 10:
    hour_int += 1
    print("This loop will never end")
    hour_int >= 10

# Random Game night
    
items = ("Apple", "Banana", "Orange", "Grape")
user_choice = input("What is your choice? : ")
pc_choice = random.choice(items)

if user_choice == pc_choice:
    print("Congratulations you picked the same thing!")
else:
    print(f"You chose {user_choice} and the computer chose {pc_choice}")

# Looping Lists

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
message = ("Dope", "Fun", "Gangster", "Exciting")

for i in range(len(genres)):
    track = i + 1
    print(f"Your track number is {track}:  Genre is {genres[i]} thats so {message[i]}.")

# Task 2

track = 0

while True:
    random_genre = (random.choice(genres))
    random_message = (random.choice(message))
    if random_genre != "Hip-hop":
        track += 1
        print(f"Your track number is {track}:  Genre is {random_genre} thats so {random_message}.")
    else:
        print("Uh oh, looks like the end of our playlist!")
        break

# Task 3

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
message = ("Dope", "Fun", "Gangster", "Exciting")
track = 0

while True:
    random_genre = (random.choice(genres))
    if random_genre != "Classical":
        track += 1    
        print(f"Your track number {track} in genre {random_genre} is ready for the light show.")
    else:
        track += 1    
        print(f"Your track number {track} in genre {random_genre}. No light show needed!")
        break



# Advanced Looping Techniques Task 1


genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
message = ("Dope", "Fun", "Gangster", "Exciting")
track = 0

for i in genres:
    genre_slice = genres[1:4]
    print(genre_slice)
    break

# Task 2

music_list = [music + " Music" for music in genres]
print(music_list)

# # Task 3

countdown = ("10", "9", "8", "7", "6", "5", "4", "3", "2", "1")
count = 11

for i in range(len(countdown)):
    count -= 1
    if count <= 1:
        print(f"{count} \nThe beat drops now!")
    elif count <= 11:
        print(f"{count}")

# while True:
#     count -= 1
#     if count <= 10 and count >= 1:
#         print(f"{count}")
#     else:
#         print(f"{count} The beat drops now!")
#         break