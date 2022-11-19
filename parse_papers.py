DLBP_URL = "https://dblp.org/search/publ/api?q=author%3AAaron_Gokaslan%3A&format=json"

from urllib.request import urlopen

# import json
import json
LOAD_URL = False
if LOAD_URL:
 
    # store the URL in url as 
    # parameter for urlopen
    
    # store the response of URL
    response = urlopen(DLBP_URL)
    
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())
else:
    with open("author_list.json", "r") as f:
        data_json = json.load(f)

hits = data_json["result"]["hits"]["hit"]
title_names = set()
for hit in hits:

    info = hit["info"]
    title = info["title"]

    venue = info["venue"]
    year = info["year"]
    url = info["ee"]
    authors = [au["text"].replace(" 0001", "").replace(" 0002", "") for au in info["authors"]["author"]]
    authors_text = ", ".join(authors)

    if title in title_names:
        assert venue == "CoRR"
        continue
    title_names.add(title)
    if venue == "CoRR":
        venue = "arXiv"

    template = f"""
        <tr>
            <td style="padding:20px;width:25%;vertical-align:middle">
            </td>
            <td width="75%" valign="middle">
              <a href="{url}">
                <papertitle>{title}</papertitle>
              </a>
              <br>
              {authors_text}
              <br>
              <em>{venue}</em>, {year}
              <br>
            </td>
          </tr>
          """
    print(template)