class Data:
    # Gets Url, uname and pwd from text file

    # def getSetUpData(self):
    file = open("E:/PycharmProjects/Practice/resources.txt")
    line = file.readlines()
    url = line[0].split("\t")[1]
    uname = line[1].split("\t")[1]
    pwd = line[2].split("\t")[1]
    file.close()

