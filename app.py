from flask import Flask, request, render_template
import src.resume_parser as rp
import src.matching as match

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["resume"]
        job_desc = request.form["job_desc"]

        extracted_text = rp.extract_text(file)
        extracted_skills = rp.extract_skills(extracted_text)
        score = match.calculate_similarity(extracted_text, job_desc)

        return render_template("index.html", text=extracted_text, skills=extracted_skills, score=score)

    return render_template("index.html", text="", skills=[], score="")

if __name__ == "__main__":
    app.run(debug=True)

