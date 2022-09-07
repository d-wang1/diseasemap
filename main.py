file = open("data/adi_census_2019.txt",'r')
for line in file:
    charList = [char for char in line if char != '"']
    line = "".join(charList)
    charList = [char for char in line if char != '\n']
    line = "".join(charList)
    list = line.split(",")
    print(list)
file.close()