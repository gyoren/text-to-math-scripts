import os

# making initial variables
string = ""
unicodelist = []
output = open("output.txt", "wb")

def main():
    string = input("Write text to convert here: ")

    for a in string:
        unicodelist.append(a.encode("unicode_escape").hex())
        # converts input into unicode escape codes and converts result into hex
        # !!! the output of this is an array of BYTES strings !!!
    
    script1 = []
    for b in unicodelist:
        # checking the location of the letters using two ranges: capital and small;
        # this is required due to unicode having 6 characters separating the normal capital and small letters
        if 64 < int(b, 16) < 91:
            script1.append(chr(int(b, 16) + 119737 + 6)) # offsets the unicode escape code by the right value (+6 for capital letters)
        elif 96 < int(b, 16) < 123:
            script1.append(chr(int(b, 16) + 119737))
    script1final = "".join(script1)

    script2 = []
    for b in unicodelist:
        # repeating the action above for all fonts that have all latin letters as assigned and valid characters;
        # some fonts are ommited due to this: https://i.imgur.com/DhX3kpK.png
        if 64 < int(b, 16) < 91:
            script2.append(chr(int(b, 16) + 119841 + 6))
        elif 96 < int(b, 16) < 123:
            script2.append(chr(int(b, 16) + 119841))
    script2final = "".join(script2)

    script3 = []
    for b in unicodelist:
        if 64 < int(b, 16) < 91:
            script3.append(chr(int(b, 16) + 119945 + 6))
        elif 96 < int(b, 16) < 123:
            script3.append(chr(int(b, 16) + 119945))
    script3final = "".join(script3)

    script4 = []
    for b in unicodelist:
        if 64 < int(b, 16) < 91:
            script4.append(chr(int(b, 16) + 120101 + 6))
        elif 96 < int(b, 16) < 123:
            script4.append(chr(int(b, 16) + 120101))
    script4final = "".join(script4)

    script5 = []
    for b in unicodelist:
        if 64 < int(b, 16) < 91:
            script5.append(chr(int(b, 16) + 120153 + 6))
        elif 96 < int(b, 16) < 123:
            script5.append(chr(int(b, 16) + 120153))
    script5final = "".join(script5)

    script6 = []
    for b in unicodelist:
        if 64 < int(b, 16) < 91:
            script6.append(chr(int(b, 16) + 120205 + 6))
        elif 96 < int(b, 16) < 123:
            script6.append(chr(int(b, 16) + 120205))
    script6final = "".join(script6)

    script7 = []
    for b in unicodelist:
        if 64 < int(b, 16) < 91:
            script7.append(chr(int(b, 16) + 120257 + 6))
        elif 96 < int(b, 16) < 123:
            script7.append(chr(int(b, 16) + 120257))
    script7final = "".join(script7)

    script8 = []
    for b in unicodelist:
        if 64 < int(b, 16) < 91:
            script8.append(chr(int(b, 16) + 120309 + 6))
        elif 96 < int(b, 16) < 123:
            script8.append(chr(int(b, 16) + 120309))
    script8final = "".join(script8)

    output.write(f"{script1final}\n{script2final}\n{script3final}\n{script4final}\n{script5final}\n{script6final}\n{script7final}\n{script8final}".encode("utf8"))

def continuation():
    continueQuestion = input("Continue? 'y' to continue, anything else to finish: ")
    while continueQuestion != "" and continueQuestion == "y":
        main()
        continueQuestion = input("Continue? 'y' to continue, anything else to finish: ")
        output.write("\n\n".encode("utf8"))

while True: # while loop so you can write as much as you want, though the text will be separated every "session" with an empty line
    main()
    continuation()
    break