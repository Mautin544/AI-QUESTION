from flask import Flask, request, render_template_string
from groq_client import ask_groq

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Question Answering</title>
</head>
<body>
    <h2>Ask AI a Question</h2>
    <form method="post">
        <textarea name="question" rows="5" cols="60">{{ question or "" }}</textarea><br>
        <button type="submit">Ask</button>
    </form>

    {% if answer %}
    <h3>Response:</h3>
    <div style="border:1px solid #ccc; padding:10px; width:60%; white-space: pre-wrap;">
        {{ answer }}
    </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    question = ""
    if request.method == "POST":
        question = request.form.get("question", "").strip()
        if question:
            answer = ask_groq(question)
        else:
            answer = "Please enter a question."
    return render_template_string(HTML, answer=answer, question=question)

if __name__ == "__main__":
    app.run(debug=True)
