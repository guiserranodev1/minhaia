from flask import Flask, render_template, request, jsonify
import google.generativeai as genai


genai.configure(api_key="AIzaSyCNP5IcXq97QLuSq3RLdAaquqsGjMlZ0AU")


model = genai.GenerativeModel("gemini-2.5-flash")


app = Flask(__name__, template_folder="templates", static_folder="static")

# teste commit

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json["message"]

        response = model.generate_content(user_input)

        return jsonify({
            "reply": response.text
        })

    except Exception as e:
        return jsonify({
            "reply": f"Erro: {str(e)}"
        })


if __name__ == "__main__":
    app.run(debug=True)