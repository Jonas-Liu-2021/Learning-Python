text_read = open("README")
text_write = open("README[复件]", "w")

while True:
    text = text_read.readline()
    if not text:
        break
    text_write.write(text)


text_read.close()
text_write.close()