def picture(wrong):
    wrong_guesses = int(wrong)
    # Create the picture
    picture = "_________\n|       |"
    if wrong_guesses >= 1:
        picture += "\n|       O"
    if wrong_guesses >= 2:
        picture += "\n|      /|\\"
    if wrong_guesses >= 3:
        picture += "\n|      / \\"
    picture += "\n|\n|"

    # Print the picture
    print(picture)

