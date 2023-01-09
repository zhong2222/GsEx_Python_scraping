import json
from urllib.request import urlopen
# from random import shuffle
import random 
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():
    # はてブのホットエントリーから記事を入手して、ランダムに1件返却します.
    # **** ここを実装します（基礎課題） ****

    # 1. はてブのホットエントリーページのHTMLを取得する
    url = "http://feeds.feedburner.com/hatena/b/hotentry"
    with urlopen(url) as res:
        html = res.read()
    # 2. BeautifulSoupでHTMLを読み込む
    soup = BeautifulSoup(html, "html.parser")

    # 3. 記事一覧を取得する
    items = soup.select("item")

    # 4. ランダムに1件取得する
    item = random.choice(items)
    print(item)

    """
        5. 以下の形式で返却する.
            {
                "content" : "記事のタイトル",
                "link" : "記事のURL"
            }
    """
    return json.dumps({
        # "content" : "記事のタイトルだよー",
        # "link" : "記事のURLだよー"
        "content" : item.find("title").string,
        "link": item.get("rdf:about")

    })

# @app.route("/api/xxxx")
# def api_xxxx():
    """
        **** ここを実装します（発展課題） ****
        ・自分の好きなサイトをWebスクレイピングして情報をフロントに返却します
        ・お天気APIなども良いかも
        ・関数名は適宜変更してください
    """
@app.route("/api/finance")
def api_finance():
    url = "https://finance.yahoo.co.jp"
    with urlopen(url) as res:
        html = res.read()

    soup = BeautifulSoup(html, "html.parser")

    headlines = soup.select("._2c_j0P1B iRvzaBLO a")
    headline = random.choice(headlines)
    print(headline)

    return json.dumps({

        "content" :  headline.find("h1").string,
        "link": headline["href"]
    })


if __name__ == "__main__":
    app.run(debug=True, port=5004)
