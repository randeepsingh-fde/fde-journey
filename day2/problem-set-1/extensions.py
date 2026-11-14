file_name = input("Enter the file name: ")

file = file_name.lower()

print(file)

if "." in file:
    index = file.rindex(".")
    after = file[index + 1:]
else:
    after = ""

if after == "gif":
    print("image/gif")
elif after == "jpg":
    print("image/jpeg")
elif after == "jpeg":
    print("image/jpeg")
elif after == "png":
    print("image/png")
elif after == "pdf":
    print("application/pdf")
elif after == "txt":
    print("text/plain")
elif after == "zip":
    print("application/zip")
else:
    print("application/octet-stream")