class Data:
    # Gets Url, uname and pwd from text file

    # def getSetUpData(self):
    file = open("/usr/local/google/home/sateeshg/git-pythonselenium/abhibus/resources/resource.txt")
    line = file.readlines()
    url = line[0].split("\t")[1]
    mobilenumber = line[1].split("\t")[1]
    invalid_mobile_number = line[2].split("\t")[1]
    # uname = line[1].split("\t")[1]
    # pwd = line[2].split("\t")[1]
    file.close()
