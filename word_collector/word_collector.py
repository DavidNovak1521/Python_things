def main():
    # fill list with words from file
    with open("words.txt", "r") as file:
        lines = file.readlines()
        listOfWords = [line.rstrip() for line in lines]

    # print current words
    print("\nCurrent words:")
    print(listOfWords)

    # start the adding loop
    while(True):
        newWord = input("\nNew word: ").rstrip()

        if newWord == "done": break

        if newWord in listOfWords:
            print("\nWord already added, try a new one!")
            continue

        listOfWords.append(newWord)
        print("\nWord added to the list.")
    
    # sort the list and print it
    listOfWords.sort()
    print(f"\nNumber of words: {len(listOfWords)}")
    print("Words: ", end="")
    print(listOfWords)

    # write the words back into the file and close it
    with open("words.txt", "w") as file:
        for word in listOfWords:
            file.write(f"{word}\n")
    
    print("Words saved to file.\n")

if __name__ == "__main__":
    main()
