
# CGPA Calculator (Streamlit)

A dynamic CGPA calculator for the BS in Data Science & Applications grading scheme.
- You select **grades** only; **credits are fixed** per subject.
- The app looks up grade points automatically and computes **CGPA**.
- According to the institute rule, courses with **I/P/F/DR** are **excluded** from GPA/CGPA. **U/W** are included with 0 points.

## 📦 Local setup (macOS)

1. Install Python 3 (macOS already has `python3`). Verify:
   ```bash
   python3 --version
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```
5. The browser opens automatically. To stop, press `Ctrl + C` in the terminal.

## ☁️ Deploy to Streamlit Community Cloud

1. Push these files (`app.py`, `requirements.txt`, `README.md`) to a **GitHub** repository.
2. Go to **https://share.streamlit.io** and sign in with GitHub.
3. Click **New app** → choose your repo, branch, and **main file path**: `app.py`.
4. Click **Deploy**. Your app will build and receive a public URL.
5. (Optional) In app settings → **Advanced**, pin a Python version (e.g., 3.11) if needed.

## 🚀 Deploy to Hugging Face Spaces (alternative)

1. Create a new **Space** → **Streamlit** template.
2. Upload `app.py` and `requirements.txt` (or connect your GitHub repo).
3. The Space will build automatically and provide a public URL.

## 📝 Notes
- Grade options: `S, A, B, C, D, E, U, W, P, F, I, DR`.
- Denominator includes **U/W** credits, excludes **I/P/F/DR** credits.
- If a course is repeated, use the best grade for that course.

