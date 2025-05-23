# Read the file and store all lines in a list
with open('textfile.txt', 'r') as reader:
    content = reader.readlines()  # Read all lines into a list (removed erroneous .)

    # Reverse the list of lines
    reversed_content = reversed(content)  # Assign reversed iterator to a variable

    # Write the reversed list back to the file
    with open('textfile.txt', 'w') as writer:
        for line in reversed_content:
            writer.write(line)