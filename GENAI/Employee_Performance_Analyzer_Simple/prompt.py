"""
Sample Gemini prompt used for Employee Performance Analysis.
"""

def build_employee_prompt(employee):
    return f"""
You are an AI employee performance analyst.

Analyze the employee below.

Name: {employee.get("name")}
Department: {employee.get("department")}
Designation: {employee.get("designation")}
Experience: {employee.get("experience")}
Skills: {employee.get("skills")}
Certifications: {employee.get("certifications")}
Performance Score: {employee.get("performance_score")}
Attendance: {employee.get("attendance")}
Projects Completed: {employee.get("projects_completed")}
Manager Feedback: {employee.get("manager_feedback")}

Generate:
1. Employee summary
2. Technical skills
3. Learning path
4. 5 personalized interview questions
5. Career growth plan
6. Training recommendations
"""
