file_read = open("README")

while True:
    text = file_read.readline()
    if not text:
        break
    print(text)

file_read.close()
