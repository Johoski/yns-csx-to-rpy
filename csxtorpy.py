# TODO solve japanese and chinese text problem
# TODO recognize language
# TODO skip empty lines and unneeded languages
# TODO recognize character
# TODO modify character to Ren'Py
# TODO transform csx dialogue to Ren'Py dialogue
# TODO easy to use cli/gui menu

import re

# reads data from txt
filename1 = input("Name of the text file to read: ")
file2 = open("output.txt", "w")
with open(filename1, "r") as file1:
    while (line := file1.readline()):
        print(line)
        patterneng = re.sub("\[EN\d+\]\s*",' "x "', line)
        announcement = re.sub("\[Announcment+\]\s*", 'an "', patterneng)
        haruka = re.sub("\[Haruka+\]\s*",'h "', announcement)
        sora = re.sub("\[Sora+\]\s*",'s "', haruka)

        file2.writelines(sora)
        print(sora)