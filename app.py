import streamlit as st
import pandas as pd

st.set_page_config(page_title="IITM BS CGPA Calculator", layout="wide")
st.title("🎓 Year-wise CGPA Calculator")

# Custom CSS for background + styling
st.markdown(
    """
    <style>
    /* Background */
    .stApp {
        background-color: #ffffff;
        background-image: url("https://www.transparenttextures.com/patterns/marble.png");
        background-attachment: fixed;
    }
    /* Title styling */
    h1 {
        color: #2E4053;
        text-align: center;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Grade mapping
GRADE_POINTS = {
    "S": 10, "A": 9, "B": 8, "C": 7,
    "D": 6, "E": 4, "U": 0,
    "P": 0, "F": 0, "W": 0,
    "I": 0, "DR": 0
}

# Exclusion rules
EXCLUDE_FROM_CGPA = {"I", "P", "F", "DR"}
INCLUDE_ZERO_IN_DEN = {"U", "W"}

# Course lists with fixed credits
FOUNDATION = [
    ("Maths 1", 4), ("Maths 2", 4),
    ("Stats1", 4), ("Stats2", 4),
    ("Eng1", 4), ("Eng2", 4),
    ("CT", 4), ("Python", 4)
]

DIPLOMA = [
    ("MLF", 4), ("MLT", 4), ("MLP", 4),
    ("BDM", 4), ("BA", 4), ("TDS", 3),
    ("MLP Project", 2), ("MAD 1.00", 4),
    ("MAD 2.00", 4), ("DBMS", 4),
    ("PDSA", 4), ("JAVA", 4), ("SC", 3),
    ("MAD 1 Project", 2), ("BDM Project", 2),
    ("MAD 2 Project", 2)
]

BSC = [
    ("SE", 4), ("DL", 4), ("AI", 4),
    ("SPG", 4), ("ST", 4), ("BSc Elective", 4)
]

BS = [
    ("Elective 1", 4),
    ("Elective 2", 4),
    ("Elective 3", 4),
    ("Elective 4", 4), 
    ("Elective 5", 4), ("Elective 6", 4)
]

YEARS = {
    "Foundation (Year 1)": FOUNDATION,
    "Diploma (Year 2)": DIPLOMA,
    "BSc (Year 3)": BSC,
    "BS (Year 4)": BS
}

st.markdown("Select grades for each subject. Credits are fixed as per IITM Website.")

# Grade options (default blank)
grade_options = [""] + list(GRADE_POINTS.keys())

all_results = []
total_points = 0
total_credits = 0
year_cgpas = {}

# Loop over years with collapsible expanders
for year_name, courses in YEARS.items():
    with st.expander(year_name, expanded=False):
        year_points = 0
        year_credits = 0
        year_rows = []

        for subject, credits in courses:
            grade = st.selectbox(
                f"{subject} (Credits: {credits})",
                options=grade_options,
                index=0,
                key=year_name + subject
            )

            if grade == "":
                gp = None
                points = 0
                den_credits = 0
            else:
                gp = GRADE_POINTS[grade]
                include_in_den = (grade not in EXCLUDE_FROM_CGPA) or (grade in INCLUDE_ZERO_IN_DEN)
                points = gp * credits if include_in_den else 0
                den_credits = credits if include_in_den else 0

                year_points += points
                year_credits += den_credits

            year_rows.append((subject, grade, credits, gp, points))

        # Add this year's results to overall
        total_points += year_points
        total_credits += year_credits

        year_cgpa = round(total_points / total_credits, 2) if total_credits > 0 else 0.0
        year_cgpas[year_name] = year_cgpa

        df = pd.DataFrame(year_rows, columns=["Subject", "Grade", "Credits", "Grade Point", "C × GP"])
        st.dataframe(df, use_container_width=True)
        st.markdown(f"**Cumulative CGPA up to {year_name}: {year_cgpa}**")

# Final summary
st.subheader("📊 Year-wise CGPA Summary! Remember: Skills matter more than credits.")
st.table({
    "Year": list(year_cgpas.keys()),
    "Cumulative CGPA": list(year_cgpas.values())
})
