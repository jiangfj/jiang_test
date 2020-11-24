import os

filename = "../month01/code_all/code/"
p = os.listdir(filename)
p.sort()
for item in p:
    filename += item
    filename1 = filename
    p1 = os.listdir(filename)
    for file in p1:
        if "demo" in file:
            filename +=("/"+file)
            with open(filename,"r") as oldfile:
                with open("month1_demo.txt","a+") as newfile:
                    newfile.write(oldfile.read())
                    newfile.write("\n")
                    newfile.write(f"{item}".center(40,"*"))
                    newfile.write("\n")
        filename=filename1

    filename = "../month01/code_all/code/"
