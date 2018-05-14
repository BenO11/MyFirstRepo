name = "Ben"
subjects = ["English","Math","Latin","History"]

print("My name is " + name)

#print(subjects)

for i in subjects:
    print("One of my classes is " + i)

teams = ["Rangers","Jets","Duke","Canadiens","OSU","Saints","Lizards"]

for i in teams:
    if i == "Rangers":
        print(i + " are the best hockey team!")
    elif i == "Jets":
        print(i + " aren't the best but one day the will be.")
    else:
        print("One of my favorite sports teams is the " + i)


teams1 = []

while True:
    print("Who are your favorite teams? Type 'end' to quit.")
    answer = input()
    if answer == "end":
        break
    else:
        teams1.append(answer)

for i in teams1:
    if i == "patriots":
        print(i + " oof, tough loss.")
    else:
        print("One of your favorite teams is " + i)
