rm -rf out.json 
scrapy crawl house -o out.json
python data_process.py
python gen_html.py