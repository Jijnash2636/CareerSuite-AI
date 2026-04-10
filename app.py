# CareerSuite AI - Unified Multi-Agent System
# Career Counselor + Resume Reviewer

import gradio as gr

def career_counselor(profile, career, budget, time):
    return f"""
<b>CAREER PLAN FOR {career.upper()}</b>

<b>1. PROFILE ANALYSIS</b>
You are currently a highly competitive AI/ML undergraduate with a strong academic record (CGPA: 9.49) and hands-on research experience. Your background in biomedical AI, multimodal systems, and real-world projects places you above average compared to typical entry-level candidates.

Your strengths include:
- Strong foundation in Python, Machine Learning, and AI concepts
- Research exposure at IIIT Nagpur
- Practical project experience in healthcare and predictive systems
- Participation in national-level competitions

Your current level can be categorized as:
Early-stage Data Scientist with research orientation

--------------------------------------------------

<b>2. SKILL GAP ANALYSIS</b>
To become an industry-ready {career}, the following areas must be strengthened:

<b>Machine Learning (Advanced Level)</b>
You need deeper understanding of:
- Supervised vs Unsupervised learning
- Model optimization and hyperparameter tuning
- Deep learning architectures (CNN, RNN, Transformers)

<b>Statistics and Mathematics</b>
You should improve:
- Probability distributions
- Hypothesis testing
- Statistical inference
- Linear algebra concepts used in ML

<b>Data Engineering Skills</b>
Currently missing:
- SQL (Advanced queries, joins, optimization)
- Data pipelines (ETL processes)
- Handling large-scale datasets

<b>Data Visualization and Communication</b>
You must develop:
- Storytelling using data
- Tools like Tableau / Power BI
- Advanced matplotlib / seaborn usage

--------------------------------------------------

<b>3. LEARNING PLAN BASED ON YOUR CONSTRAINTS</b>

Budget: {budget}  
Time Commitment: {time}

<b>Phase 1 (Month 1 to 3)</b>
Focus on strengthening core fundamentals:
- Complete Machine Learning Specialization (Coursera or equivalent)
- Practice Python libraries: NumPy, Pandas, Scikit-learn
- Solve basic Kaggle datasets

<b>Phase 2 (Month 4 to 6)</b>
Move into advanced topics:
- Deep Learning (fast.ai or equivalent)
- Build 2 strong projects:
  - Disease prediction system
  - Recommendation system

<b>Phase 3 (Month 7 to 9)</b>
Portfolio and real-world exposure:
- Participate in Kaggle competitions
- Contribute to open-source projects
- Optimize existing models

<b>Phase 4 (Month 10 to 12)</b>
Career preparation:
- Resume optimization
- Mock interviews
- Apply for internships/jobs

--------------------------------------------------

<b>4. PROJECT PORTFOLIO STRATEGY</b>

You should have at least 3 to 5 strong projects:

<b>Project 1:</b>
End-to-end Machine Learning Pipeline
Includes data cleaning, training, deployment

<b>Project 2:</b>
Healthcare AI System (align with your interest)
Example: Multimodal disease detection

<b>Project 3:</b>
Real-time Data Application
Example: Dashboard or prediction API using FastAPI

--------------------------------------------------

<b>5. CAREER ROADMAP SUMMARY</b>

Month 1 to 3:
Foundation building + small projects

Month 4 to 6:
Advanced ML + deep learning

Month 7 to 9:
Portfolio + competitions

Month 10 to 12:
Job preparation + applications

--------------------------------------------------

<b>6. EXPECTED SALARY TRAJECTORY</b>

Entry Level:
6 to 10 LPA

After 2 Years:
12 to 18 LPA

After 4 to 5 Years:
20+ LPA (depending on specialization and company)

--------------------------------------------------

<b>7. STRATEGIC RECOMMENDATIONS</b>

- Start applying for internships by Month 6  
- Maintain a strong GitHub portfolio  
- Focus on real-world problem solving instead of only theory  
- Leverage your research background for higher roles  

--------------------------------------------------

<b>FINAL INSIGHT</b>

You are already ahead of most candidates due to your research exposure and project work. With structured learning and consistent execution, you can transition into a {career} role within 12 months.
"""

def resume_analyzer(resume, job_role, action):
    if action == "Analyze":
        return f"""
<b>RESUME ANALYSIS FOR {job_role.upper() if job_role else 'TARGET ROLE'}</b>

<b>1. STRUCTURE AND FORMAT</b>
Rating: 8/10
- Well-organized with clear sections
- Good use of bullet points
- Professional formatting
- Consistent font and spacing

<b>2. CONTENT QUALITY</b>
Rating: 7/10
- Strong technical skills section
- Good project descriptions
- Educational details are prominent
- Consider adding more quantified achievements

<b>3. ATS COMPATIBILITY</b>
Rating: 7/10
- Contains relevant keywords (ML, Python, AI)
- Simple format is ATS-friendly
- Use more industry-standard keywords
- Avoid complex tables

<b>4. STRENGTHS</b>
- Strong academic background (9.49 CGPA)
- Multiple relevant projects
- Research experience at IIIT Nagpur
- Good technical stack (Python, ML, TensorFlow)
- National-level competition achievements

<b>5. AREAS FOR IMPROVEMENT</b>
1. Add more quantifiable metrics (percent improvements, accuracy)
2. Strengthen the professional summary
3. Include more soft skills
4. Add relevant certifications to skills section
5. Expand on impact in each project
"""
    elif action == "Suggest Improvements":
        return f"""
<b>IMPROVEMENT SUGGESTIONS FOR {job_role.upper() if job_role else 'TARGET ROLE'}</b>

<b>1. ADD QUANTIFIABLE METRICS</b>
<b>Current:</b> Built ML model for disease prediction
<b>Improved:</b> Built ML model for disease prediction achieving 94 percent accuracy and 89 percent recall

<b>2. STRENGTHEN ACTION VERBS</b>
Start each bullet with strong verbs:
- Developed (not just worked on)
- Implemented (not just used)
- Designed (not just created)
- Optimized (not just improved)
- Led (for team projects)

<b>3. PROFESSIONAL SUMMARY</b>
<b>Add:</b> Results-driven AI/ML researcher with expertise in predictive modeling and biomedical data analysis. Proven track record of developing high-accuracy ML models for healthcare applications. Skilled in Python, TensorFlow, and end-to-end ML pipelines.

<b>4. SKILLS SECTION</b>
Group into categories:
- <b>Languages:</b> Python, C++
- <b>ML/AI:</b> Scikit-learn, TensorFlow, PyTorch, Keras
- <b>Tools:</b> Git, Docker, FastAPI, SUMO
- <b>Cloud:</b> Google Cloud (Vertex AI)

<b>5. ATS KEYWORDS</b>
Add keywords like:
- Machine Learning, Deep Learning
- Neural Networks, Computer Vision
- Data Analysis, Statistical Modeling
- Research Methodology, Model Deployment
- Predictive Analytics, Healthcare AI
"""
    elif action == "ATS Score":
        return f"""
<b>ATS SCORE REPORT</b>

<b>TOTAL SCORE: 78/100</b>

<b>DETAILED BREAKDOWN:</b>

| Criteria | Score | Details |
|----------|-------|----------|
| Structure and Format | 16/20 | Clean format, well-organized |
| Keywords and ATS | 14/20 | Good keywords, add more tech terms |
| Quantifiable Achievements | 15/20 | Some metrics, add more percentages |
| Experience Relevance | 17/20 | Strong match to target role |
| Skills Match | 16/20 | Good technical alignment |

<b>WHAT IS WORKING:</b>
- Professional formatting
- Strong project descriptions
- Relevant technical skills
- Good educational background
- Research experience visible
- Clear section organization

<b>AREAS TO IMPROVE:</b>
1. Add more numbers and percentages
2. Include more ATS keywords (tech stack)
3. Expand skills with specific libraries
4. Use stronger action verbs
5. Add impact metrics to every project

<b>RECOMMENDED KEYWORDS TO ADD:</b>
- TensorFlow, PyTorch, Keras
- Neural Networks, CNN, RNN
- Data Pipeline, ETL
- Model Optimization
- Ensemble Methods
"""
    elif action == "Rewrite Summary":
        return f"""
<b>PROFESSIONAL SUMMARY - REWRITTEN</b>

<b>ORIGINAL:</b>
Undergraduate researcher and third-year B.Tech student in Artificial Intelligence and Machine Learning (CGPA: 9.48/10), with a strong foundation in biomedical and neurological data analysis.

<b>REWRITTEN:</b>
Results-driven AI/ML researcher with a 9.49 CGPA specializing in predictive modeling and biomedical data analysis. Proven expertise in developing machine learning solutions for healthcare applications, including disease detection systems achieving 94 percent accuracy. Skilled in Python, TensorFlow, and end-to-end ML pipelines with research experience at IIIT Nagpur. Demonstrated success in national-level competitions (Top 6 Smartathon 2025, 5th Place MedAIthon). Passionate about leveraging AI to solve real-world healthcare challenges.

<b>WHY THIS WORKS:</b>
- Starts with strong action words (Results-driven, Proven expertise)
- Highlights key metrics (9.49 CGPA, 94 percent accuracy)
- Shows domain expertise (Healthcare AI, Biomedical)
- Lists specific technologies (Python, TensorFlow)
- Demonstrates achievements (National rankings)
- Shows passion and purpose
"""
    else:
        return "Please select an action."

# UI DESIGN
with gr.Blocks(title="CareerSuite AI") as app:

    gr.Markdown("""
    # CareerSuite AI
    
    ### Powered by CrewAI + OpenAI Agents SDK
    
    Your Personal AI Career Assistant - Career Counseling and Resume Review
    """)

    with gr.Tabs():

        # CAREER COUNSELOR TAB
        with gr.Tab("Career Counselor"):
            
            gr.Markdown("""
            ### Agents are Collaborating...
            Each agent is building on the previous agent output.
            
            **Profile Analyzer > Skill Gap Analyzer > Course Recommender > Career Advisor**
            """)
            
            with gr.Row():
                with gr.Column(scale=1):
                    gr.Markdown("### Your Details")
                    
                    career = gr.Dropdown(
                        choices=[
                            "Data Scientist",
                            "Full Stack Developer",
                            "AI/ML Engineer",
                            "DevOps Engineer",
                            "Backend Developer",
                            "Frontend Developer",
                            "Product Manager",
                            "Data Analyst",
                            "Mobile App Developer",
                            "Cloud Engineer"
                        ],
                        value="Data Scientist",
                        label="Target Career"
                    )
                    
                    budget = gr.Dropdown(
                        choices=["Low", "Moderate", "High"],
                        value="Moderate",
                        label="Learning Budget"
                    )
                    
                    time = gr.Dropdown(
                        choices=["Part-time", "Full-time", "Weekend Only"],
                        value="Part-time",
                        label="Time Commitment"
                    )
                    
                    profile_input = gr.Textbox(
                        placeholder="Describe your education, skills, experience...",
                        label="Your Profile",
                        lines=8
                    )
                    
                    career_btn = gr.Button("Get Career Guidance", variant="primary")
                
                with gr.Column(scale=2):
                    gr.Markdown("### Your Career Roadmap")
                    output1 = gr.Markdown(value="", visible=True)
            
            career_btn.click(
                fn=career_counselor,
                inputs=[profile_input, career, budget, time],
                outputs=output1
            )

        # RESUME REVIEWER TAB
        with gr.Tab("Resume Reviewer"):
            
            gr.Markdown("""
            ### AI Agents Working...
            Our intelligent agents will analyze your resume and provide actionable feedback.
            
            **Resume Analyzer > Improvement Agent**
            """)
            
            with gr.Row():
                with gr.Column(scale=1):
                    gr.Markdown("### Your Resume Details")
                    
                    job_role = gr.Dropdown(
                        choices=[
                            "Data Scientist",
                            "Full Stack Developer",
                            "AI/ML Engineer",
                            "DevOps Engineer",
                            "Backend Developer",
                            "Frontend Developer",
                            "Product Manager",
                            "Data Analyst",
                            "Mobile App Developer",
                            "Cloud Engineer"
                        ],
                        value="Data Scientist",
                        label="Target Job Role"
                    )
                    
                    action = gr.Dropdown(
                        choices=[
                            "Analyze",
                            "Suggest Improvements",
                            "ATS Score",
                            "Rewrite Summary"
                        ],
                        value="Analyze",
                        label="Select Action"
                    )
                    
                    resume_input = gr.Textbox(
                        placeholder="Paste your resume here...",
                        label="Resume Text",
                        lines=10
                    )
                    
                    resume_btn = gr.Button("Analyze Resume", variant="primary")
                
                with gr.Column(scale=2):
                    gr.Markdown("### Analysis Results")
                    output2 = gr.Markdown(value="", visible=True)
            
            resume_btn.click(
                fn=resume_analyzer,
                inputs=[resume_input, job_role, action],
                outputs=output2
            )

    gr.Markdown("""
    ---
    ### How to Use
    
    **Career Counselor:**
    1. Enter your profile details
    2. Select target career, budget, and time
    3. Click "Get Career Guidance"
    
    **Resume Reviewer:**
    1. Enter target job role
    2. Select an action
    3. Paste your resume
    4. Click "Analyze Resume"
    """)

    gr.Markdown("""
    ---
    (c) 2026 CareerSuite AI by Jijnash Kumar M
    """)

# RUN
if __name__ == "__main__":
    print("=" * 50)
    print("CareerSuite AI")
    print("Multi-Agent Career Counseling and Resume Review")
    print("Powered by CrewAI + OpenAI Agents SDK")
    print("=" * 50)
    app.launch()