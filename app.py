from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


API_KEY = "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"
MODEL_NAME = "google/gemini-2.0-flash-001"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-objective', methods=['POST'])
def generate_objective():
    """Handles the AJAX request from the frontend to generate the AI Objective."""
    data = request.json
    
    prompt = f"""
    Create a professional 2-sentence Career Objective for a CV.
    Name: {data.get('fullName', 'Candidate')}
    Skills: {data.get('skills', '')}
    Projects: {data.get('projects', '')}
    Qualifications: {data.get('quals', '')}
    Tone: Professional, ambitious, and concise. 
    Return ONLY the objective text. Do not include quotes or intro text.
    """

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload
        )
        result = response.json()
        
        if 'choices' in result:
            ai_text = result['choices'][0]['message']['content'].strip()
            return jsonify({"success": True, "objective": ai_text})
        else:
            return jsonify({"success": False, "error": result.get('error', {}).get('message', 'Unknown API error')})
            
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/export-cv', methods=['POST'])
def export_cv():
    """Processes the submitted form and passes the data to the chosen CV template."""
    
    cv_data = {
        "fullName": request.form.get("fullName"),
        "dob": request.form.get("dob"),
        "email": request.form.get("email"),
        "phone": request.form.get("phone"),
        "city": request.form.get("city"),
        "github": request.form.get("github"),
        "linkedin": request.form.get("linkedin"),
        "objective": request.form.get("objective"),
        "other_qualifications": request.form.get("other_qualifications"),
        "skills": request.form.get("skills"),
        "languages": request.form.get("languages"),
        "extra": request.form.get("extra")
    }

    degrees = request.form.getlist("edu_degree[]")
    boards = request.form.getlist("edu_board[]")
    schools = request.form.getlist("edu_school[]")
    years = request.form.getlist("edu_year[]")
    grades = request.form.getlist("edu_grade[]")
    
    education_list = []
    for i in range(len(degrees)):
        if degrees[i]:
            education_list.append({
                "degree": degrees[i],
                "board": boards[i] if i < len(boards) else "",
                "school": schools[i] if i < len(schools) else "",
                "year": years[i] if i < len(years) else "",
                "grade": grades[i] if i < len(grades) else ""
            })
    cv_data["education"] = education_list

    p_titles = request.form.getlist("p_title[]")
    p_descs = request.form.getlist("p_desc[]")
    
    project_list = []
    for i in range(len(p_titles)):
        if p_titles[i]:
            project_list.append({
                "title": p_titles[i],
                "desc": p_descs[i] if i < len(p_descs) else ""
            })
    cv_data["projects"] = project_list

    template_choice = request.form.get("template_choice", "1")
    
    if template_choice == "2":
        return render_template('cv_template_2.html', cv=cv_data)
    else:
        return render_template('cv_template_1.html', cv=cv_data)

if __name__ == '__main__':
    app.run(debug=True)
