from flask import Flask, request, render_template_string, redirect
from generator import generate_tweet
from twitter_client import post_tweet

app = Flask(__name__)

current_tweet = ""

HTML = """
<html>
  <body style="font-family:Arial;margin:40px;max-width:700px">
    <h2>Tweet Generator Panel</h2>
    <form method="POST">
      <textarea name="tweet" style="width:100%;height:140px;">{{tweet}}</textarea><br><br>

      <button name="action" value="approve" style="padding:10px;background:green;color:white;border:none;">
        ✔ Approve & Post
      </button>

      <button name="action" value="regenerate" style="padding:10px;background:orange;color:white;border:none;">
        🔄 Regenerate
      </button>
    </form>
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    global current_tweet

    if request.method == "POST":
        action = request.form.get("action")
        edited_text = request.form.get("tweet")

        if action == "approve":
            post_tweet(edited_text)
            current_tweet = generate_tweet()
            return redirect("/")

        if action == "regenerate":
            current_tweet = generate_tweet()
            return redirect("/")

    if not current_tweet:
        current_tweet = generate_tweet()

    return render_template_string(HTML, tweet=current_tweet)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
