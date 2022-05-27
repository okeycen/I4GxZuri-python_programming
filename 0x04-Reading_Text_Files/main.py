# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
#another way of removing the leading and trailing whitespaces  
#words=" ".join(result.split())

def read_file_content(filename):
    # [assignment] Add your code here 
    file = open(filename)
    return file.read()

def count_words():
    # [assignment] Add your code here
    text=read_file_content("story.txt")

    #removing special character from the text file
    data= text.split()
    new_data=""
    for elem in data:
        result=''.join(char for char in elem if char.isalnum())
        new_data=new_data+result+" "
    
    words=new_data.lower().split()

    #count elements in the list[duplicates removed]
    dict_of_words= {elem:words.count(elem) for elem in words}
    
    return dict_of_words

print(count_words())