import pafy
from youtube_search import YoutubeSearch
from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def return_download_link(name):
    results = YoutubeSearch(name, max_results=10).to_dict()
    url = f"https://youtube.com/watch?v={results[0]['id']}"
    video = pafy.new(url)
    return video.getbestaudio().url

if __name__ == "__main__":
    app.run()