import streamlit as st
import wikipedia
import os
import uuid

wikipedia.set_lang("ru")
OUTPUT_DIR = "output"
UPLOAD_DIR = "uploads"
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.title("Wikicremma: случайная статья + изображения")

if st.button("Скачать случайную статью"):
    try:
        while True:
            title = wikipedia.random()
            page = wikipedia.page(title)
            art_url = page.url
            art_id = title.replace("/", "_").replace("\\", "_")
            summary = page.summary
            full_text = art_url + "\n@@===#####===@@\n" + summary
            if len(full_text) >= 700:
                filepath = os.path.join(OUTPUT_DIR, f"{art_id}.txt")
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(full_text)
                st.success(f"Статья: {title}")
                st.text_area("Текст статьи", full_text, height=300)
                st.session_state["current_article"] = {
                    "id": str(uuid.uuid4()),
                    "title": art_id,
                    "text": full_text,
                    "file": filepath
                }
                break
    except Exception as e:
        st.error(f"Ошибка: {e}")

if "current_article" in st.session_state:
    uploaded_files = st.file_uploader("Загрузите изображения", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    
    if uploaded_files:
        article_info = st.session_state["current_article"]
        article_id = article_info["id"]
        article_title = article_info["title"]
        save_dir = os.path.join(UPLOAD_DIR, article_id)
        os.makedirs(save_dir, exist_ok=True)

        for file in uploaded_files:
            file_path = os.path.join(save_dir, file.name)
            with open(file_path, "wb") as f:
                f.write(file.read())
        st.success("Файлы сохранены.")
        st.write(f"Связь ID статьи: `{article_id}` (заголовок: {article_title})")

if st.checkbox("🔒 Показать все загруженные пары"):
    for article_dir in os.listdir(UPLOAD_DIR):
        article_path = os.path.join(UPLOAD_DIR, article_dir)
        if os.path.isdir(article_path):
            st.markdown(f"### 📄 ID статьи: {article_dir}")
            for image_file in os.listdir(article_path):
                st.image(os.path.join(article_path, image_file), width=200, caption=image_file)
