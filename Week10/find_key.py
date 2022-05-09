import os

PATH_PICS = r"pics"

#get file names from a folder 
file_list = os.listdir(PATH_PICS)
#cleprint(file_list)

save_path = os.getcwd()
#print("Current Working Directory is " + save_path)

os.chdir(PATH_PICS)
print("Current Working Directory is " + os.getcwd())

#for each file, rename filename
remove = "0123456789"
table = str.maketrans("","",remove)

for file_name in file_list:
    os.rename(file_name, file_name.translate(table))

os.chdir(save_path)



