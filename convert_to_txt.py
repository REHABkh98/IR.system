import docx
def clear():
    open('data/data.txt', 'w').close()
def read(file = 'data/data.txt'):
    with open(file, 'r') as file:
        data = file.read().replace('\n', '')
    with open ('data/data.txt', 'w', encoding="utf-8") as file:
        file.write(data)     
    return data    

def write(data):
    with open ('data/data.txt', 'w', encoding="utf-8") as file:
        file.write(data)  
def read_word_file(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
        write('\n'.join(fullText))
    
