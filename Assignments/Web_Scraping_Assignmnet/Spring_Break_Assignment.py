import requests
import pathlib

with open('/Users/YingyuChen/is310/Assignments/Web_Scraping_Assignmnet/raw_script_urls.txt',encoding = "ISO-8859-1") as file:
    text = file.readlines()

url_list = []

for line in text:
    line = line.split(' +++$+++ ')
    info = {
        'name':line[1],
        'url':line[2]
    }
    url_list.append(info)

def read_remote(url):
  # assumes the url is already encoded (see urllib.parse.urlencode)
  with requests.get(url) as response:
    response.encoding = 'utf-8'
    if response.status_code == requests.codes.ok: # (that is 200)
      return response.text
  return None

datafolder = pathlib.Path('scripts_dump')
if not datafolder.exists():
    datafolder.mkdir()


for item in url_list:
    response = requests.get(item['url'].strip())
    if response.status_code == 200:
        if 'hundland' not in item['url']:
            fname = item['name'] + '.txt'
            out_path = pathlib.Path(fname)
            outfile = datafolder / out_path
            document = read_remote(item['url'].strip())
            if '<pre>' not in document.lower():
                if len(document) > 50:
                    outfile.write_text(document.strip())
            else:
                idx = document.lower().find('<pre>')+len('<pre>')
                idx2 = document.lower().find('</pre>')
                outfile.write_text(document[idx:idx2].strip())

        
