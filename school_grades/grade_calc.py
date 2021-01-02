def print_table(g):
    print("\n----------Grades-----------------------")
    print("| Name:           | Credit: | Grade:  |")
    print("---------------------------------------")
    for subj in g:
        print("| {:15} |    {}    |    {}    |".format(
            subj[0], subj[1], subj[2]))
    print("---------------------------------------")


def print_mean(g):
    x = 0
    y = 0
    credit = 0
    for subj in g:
        if (int(subj[2]) > 1):
            credit += int(subj[1])
        y += int(subj[1])
        x += int(subj[1]) * int(subj[2])
    if(x > 0):
        print(f"Credit: {credit}, Mean: {x/y:.2f}\n")


# open file, create list of subjects

my_file = open("grades.txt", "r")

grades = []
for line in my_file:
    subject = line.strip().split(" ")
    grades.append(subject)

my_file.close()

# manage

keyword = "nothing"

while(True):
    print_table(grades)
    print_mean(grades)
    print("---> 'add' for adding new subject")
    print("---> 'delete' for deleting the last subject")
    print("---> 'done' for ending and calculating")
    keyword = input("\nNext step: ")
    subject = [None, None, None]
    if(keyword == "add"):
        subject[0] = input("Name: ")
        subject[1] = input("Credit: ")
        subject[2] = input("Grade: ")
        grades.append(subject)
    elif(keyword == "delete"):
        grades.pop()
    elif(keyword == "done"):
        break
    else:
        print("\nWrong keyword!")

print_table(grades)
print_mean(grades)

# save to file

save = input("Do you want to save the changes? [yes/no] -> ")

if(save == "yes"):
    my_file = open("grades.txt", "w")
    for subj in grades:
        my_file.write("{} {} {}\n".format(subj[0], subj[1], subj[2]))
