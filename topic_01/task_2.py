a_str = '     dscad    ' 
a_striped = a_str.strip()
print(a_striped)

b_str = '****rgvedf****' 
b_striped = b_str.strip('*')
print(b_striped)

c_str = str(input("Enter C:"))
c_striped = c_str.strip()
print(c_striped)
##############################

word_str = "Hello PYTHON"
word_capitalized = word_str.capitalize()
print(word_capitalized)

text_str = "python is not so HARD"
text_capitalized = text_str.capitalize()
print(text_capitalized)

phrase_str = str(input("Enter phrase: "))
phrase_capitalized = phrase_str.capitalize()
print(phrase_capitalized)

###############################

txt_str = "hello, and welcome to Python"
txt_titled = txt_str.title()
print(txt_titled)

phrase_str = "hello, and welcome to Python. it's great, isn't it?"
phrase_titled = phrase_str.title()
print(phrase_titled)

word_str = str(input("Enter word: "))
word_titled = word_str.title()
print(word_titled)

###############################

sentence_str = "Hello I'm from Python"
sentence_upper = sentence_str.upper()
print(sentence_upper)

word_str = "programming111"
word_upper = word_str.upper()
print(word_upper)

text_str = str(input("Enter text: "))
text_upper = text_str.upper()
print(text_upper)
###############################

text_str = "Hello I'm from Python"
text_lower = text_str.lower()
print(text_lower)

word_str = "PYTHON000"
word_lower = word_str.lower()
print(word_lower)

text_str = str(input("Enter text: "))
text_lower = text_str.lower()
print(text_lower)
