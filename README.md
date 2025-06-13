# Адаптация wikicremma под русскоязычную википедию

# Установка
```
git clone https://github.com/Svetlana-Yatsyk/wikicremma_ru.git
cd /content/wikicremma_ru

pip install -r requirements.txt
apt-get install -y wkhtmltopdf

python download.py 10
python convert_pdf.py
```
