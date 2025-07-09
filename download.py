import wikipedia, requests, os, sys
from urllib.parse import unquote

os.makedirs("output", exist_ok=True)
wikipedia.set_lang("ru")

n = int(sys.argv[-1])
while n > 0:
    try:
        title = wikipedia.random()
        page = wikipedia.page(title)
        art_url = page.url
        art_id = title
        summary = page.summary
        full_text = art_url + "@@===#####===@@" + summary

        if len(full_text) >= 900:
            with open(f"output/{art_id}.txt", "w") as f:
                f.write(full_text)
            print(f"Saved [{art_id}] ({len(full_text)} characters)")
            n -= 1
        else:
            print(f"Skipped [{art_id}] because it is too short ({len(full_text)} characters)")
    except Exception as e:
        print("Error:", e)
