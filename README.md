                                   **  AI-Powered CV Builder **

A dynamic, web-based CV generation tool that uses AI to automatically write professional Career Objectives based on a user's skills and project experience. Built with Python (Flask) and integrated with the OpenRouter API.

Features

* **Smart AI Integration:** Automatically generates a tailored, professional 2-sentence Career Objective using OpenRouter (defaulting to Gemini 2.0 Flash) based on the user's inputted skills, projects, and qualifications.
* **Multiple Professional Layouts:** Choose between a "Standard" (Single Column) or "Modern" (Two Column) layout before exporting.
* **Seamless PDF Export:** Custom CSS print media queries ensure the CV prints perfectly to PDF without browser headers, footers, or URLs.
* **Dynamic Form Fields:** Users can add or remove as many Education and Project entries as they need on the fly.
* **Secure Backend:** API keys are hidden securely in the Python Flask backend, keeping them safe from client-side exposure.

Tech Stack

* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Backend:** Python 3, Flask
* **API:** OpenRouter (LLM integration)

Project Structure

\`\`\`text
CV_Maker/
│
├── app.py                      # Main Flask application and API routing
├── README.md                   # Project documentation
│
└── templates/                  # HTML Templates
    ├── index.html              # The main data entry form & layout selector
    ├── cv_template_1.html      # Standard single-column CV template
    └── cv_template_2.html      # Modern two-column CV template
\`\`\`

Installation & Setup

**1. Clone the repository:**
\`\`\`bash
git clone https://github.com/Ankanlearn2003/CV_Maker.git
cd CV_Maker
\`\`\`

**2. Install the required dependencies:**
Ensure you have Python installed, then run:
\`\`\`bash
pip install flask requests
\`\`\`

**3. Set up your API Key:**
* Get a free API key from [OpenRouter](https://openrouter.ai/).
* Open `app.py` and replace `"PASTE_YOUR_OPENROUTER_KEY_HERE"` with your actual API key.

**4. Run the application:**
\`\`\`bash
python app.py
\`\`\`

**5. Open in your browser:**
Navigate to `http://127.0.0.1:5000` to start building your CV!

## 🖨️ How to Export as PDF
1. Fill out your details on the main page.
2. Click **"Preview & Export CV"** and select your desired layout.
3. On the generated CV page, click the **"Print / Save as PDF"** button.
4. *Important:* In your browser's print dialog window, ensure **"Headers and footers"** is **unchecked** for a clean, professional look. Save as PDF!

Author
**Ankan Sarkar** ```
