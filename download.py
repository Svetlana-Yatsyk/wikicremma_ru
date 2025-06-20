import wikipedia, requests, os, sys
from urllib.parse import unquote

os.makedirs("output", exist_ok=True)
wikipedia.set_lang("is")

n = int(sys.argv[-1])
while n > 0:
    try:
        title = wikipedia.random()
        page = wikipedia.page(title)
        art_url = page.url
        art_id = title
        summary = ".".join(page.summary.split(".")[:8])
        with open(f"output/{art_id}.txt", "w") as f:
            f.write(art_url + "@@===#####===@@" + summary)
        print(f"Saved [{art_id}]")
        n -= 1
    except Exception as e:
        print("Error:", e)
