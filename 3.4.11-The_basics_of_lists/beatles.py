#!/usr/bin/python3


# step 1
beatles = []
print("step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("step 2:", beatles)

# step 3
for member in ["Stu Sutcliffe", "Pete Best"]:
    user_input = input(f"Add {member} to the band? (yes/no:")
    if user_input.lower() == "yes":
        beatles.append(member)
print("step 3:", beatles)

# step 4
if "Stu Sutcliffe" in beatles:
    del beatles[beatles.index("Stu Sutcliffe")]
if "Pete Best" in beatles:
    del beatles[beatles.index("Pete Best")]
print("step 4", beatles)

# step 5
beatles.insert(0, "Ringo Starr")
print("step 5", beatles)

print("The fab", len(beatles))
