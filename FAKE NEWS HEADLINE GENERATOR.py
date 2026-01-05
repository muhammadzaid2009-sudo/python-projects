# IMPORT A RANDOM MODULE
import random

# CREATE LIST
subject = ["shaheen","Rizwan","tabish hasmi","Suneel munj","shafat ali"]
actions = ["riding cd70 bike","riding a wheel cart","sweaping at floor","bagging"]
places = ["at minare pakistan", "at faisal masjid","at gadafi stadium","at mazare quaid","at green line bus stop"]

# STARRT THE LOOP (WHILE LOOP)
while True:
    chosen_subject = random.choice(subject)
    chosen_action = random.choice(actions)
    chosen_place = random.choice(places)

    headlines = f"BREAKING NEWS:{chosen_subject} {chosen_action} {chosen_place}"
    print("\n" + headlines)
# TAKING INPUT FROM USER
    user_input = input("do you want to see more headlines (yes/no)").strip().lower()
    if user_input == "no":
          break
print("good by it was glad to see you....")




