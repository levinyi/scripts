import os
import sys
import requests
from bs4 import BeautifulSoup


# url = "https://www.physicsandmathstutor.com/chemistry-revision/a-level-edexcel-ial/unit-5/"
url = sys.argv[1]
html = requests.get(url)

if html.status_code == 200:
    soup = BeautifulSoup(html.text, "html.parser")
    for link in soup.find_all('a'):
        new_link = str(link.get('href'))
        if new_link.endswith('.pdf'):
            pdf_name = new_link.split("/")[-1].replace(" ", "_").replace(",","").replace("&","and")
            if os.path.exists(pdf_name):
                pdf_name = pdf_name.replace(".pdf","_1.pdf")
            
            # print pdf_name
            
            pdf_r = requests.get(new_link,stream=True,verify=False)

            with open(pdf_name, "wb") as pdf_file:
                for chunk in pdf_r.iter_content(chunk_size=1024):
                    if chunk: # filter out keep-alive new chunks
                        pdf_file.write(chunk)
                        pdf_file.flush()
