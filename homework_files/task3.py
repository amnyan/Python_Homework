filename = 'specific_position.txt'
text = "This is the text"

def create_file(filename, text):
        fd = open(filename, 'w')
        fd.write(text)
def write_text(filename, position, text):
    fd =  open(filename, 'r+')
    content = fd.read()
    fd.seek(0)
    updated_content = content[:position] + text + content[position:]
    fd.write(updated_content)
    fd.truncate()

create_file(filename, text)

position = 10
text = "some text"
write_text(filename, position, text)
