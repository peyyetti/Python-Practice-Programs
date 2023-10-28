import os

print("Hello ")

if( not os.path.exists("TEMP")):
    os.mkdir("TEMP")
    
var = os.listdir("TEMP")

print(var, "\n", "next ")

for traversal in var:
    print(traversal)


# for i in range(5):
#     os.mkdir(f"TEMP/folder{i+1}")
    # os.rename(f"TEMP/folder{i}",f"TEMP/Folder {i+1}")
    # os.rmdir(f"TEMP/Folder {i+1}")
    # os.rmdir(f"TEMP")
    