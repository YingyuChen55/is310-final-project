# import the stuff
import requests
import string

# 1. read the text and save it
def read_remote(url):
  # assumes the url is already encoded (see urllib.parse.urlencode)
  with requests.get(url) as response:
    response.encoding = 'utf-8'
    if response.status_code == requests.codes.ok: 
      return response.text
  return None

def get_text():
    import os
    
    Jane_URL  = "https://www.gutenberg.org/files/1342/1342-0.txt"
    Jane_FILE = "jane.txt"
    
    text = None
    if os.path.exists(Jane_FILE):
       # write the code to read from Jane
       text = ''
    else:
       text = read_remote(Jane_URL)
       # write the code to write text to jane_file
       
    return text

jane = get_text()

# 2. text cleaning
key_word = 'Produced by: Anonymous Volunteers and David Widger'
idx = jane.find(key_word) + len(key_word)
jane_cleaned = jane[idx:]

# 3. replacing task

jane_cleaned = jane_cleaned.replace("man", "person")
jane_cleaned = jane_cleaned.replace("wife", "parther")

# Bonus Try
def replace_word(text, original, changed):
    text = text.replace(original,changed)
    return text

#replace_word(replace_word(jane_cleaned,"man", "person"),"wife", "parther")

