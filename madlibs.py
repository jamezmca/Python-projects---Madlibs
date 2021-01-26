# # string concatentation (aka how to put strings together)
# # suppose we want to create a string that says "subscribe to ______"
# youtuber = "James McArthur" #some string variable

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("adjective: ")
verb1 = input("verb: ")
verb2 = input("verb: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so exceited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)