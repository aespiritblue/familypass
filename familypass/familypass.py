from flask import Flask, request, render_template_string

app = Flask(__name__)

# Define the HTML template for the form and results
form_template = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Family Pass Request Generator</title>
</head>
<body>
    <h1>J-CO Family Pass Generator</h1>
    <form method="post" action="/">
        <label for="rank">Rank (PV1, PV2, PFC, SPC):</label>
        <input type="text" id="rank" name="rank" required><br>

        <label for="last_name">Last Name:</label>
        <input type="text" id="last_name" name="last_name" required><br>

        <label for="first_name">First Name:</label>
        <input type="text" id="first_name" name="first_name" required><br>

        <label for="age">Age:</label>
        <input type="text" id="age" name="age" required><br>

        <label for="sex">Sex:</label>
        <input type="text" id="sex" name="sex" required><br>

        <label for="race">Race:</label>
        <input type="text" id="race" name="race" required><br>

        <label for="component">Component:</label>
        <input type="text" id="component" name="component" required><br>

        <label for="relative">Relative's Name (First Last):</label>
        <input type="text" id="relative" name="relative" required><br>

        <label for="relationship">Relationship:</label>
        <input type="text" id="relationship" name="relationship" required><br>

        <label for="contact_number">Contact Number (Use dashes!):</label>
        <input type="text" id="contact_number" name="contact_number" required><br>

        <label for="dates_of_fp">Dates of Family Pass:</label>
        <input type="text" id="dates_of_fp" name="dates_of_fp" required><br>

        <input type="submit" value="Generate Document">
    </form>
    {% if subject_line and bluf %}
    <h2>Generated Document:</h2>
    <pre>Subject Line: {{ subject_line }}</pre>
    <pre>{{ bluf }}</pre>
    {% endif %}
</body>
</html>
"""

def generate_document(rank, last_name, first_name, age, sex, race, component, relative, relationship, contact_number, dates_of_fp):
    # Define the subject line
    subject_line = f"(INFORM/ACTION) 7Ws+1_AIT Family Pass Request for {rank} {last_name}, {first_name}_JCO"
    
    # Define the BLUF sections
    bluf = f"""
BLUF:
    
1. Who: {rank} {last_name}, {first_name} / Age: {age} / Sex: {sex} / Race: {race} / Component: {component} / AIT / MOS: 27D
    
2. What: {rank} {last_name}, {first_name} is requesting a family pass on {dates_of_fp}. IOT spend time with {relative} ({relationship}) Contact #: {contact_number}
    
3. Where: Within a 15 mile radius of Fort Gregg-Adams.
    
4. When: {dates_of_fp}
    
5. Why: {rank} {last_name}, {first_name} wants to spend time with their family.
    
6. What (actions did leadership take): {rank} {last_name}, {first_name} has been counseled and understands the rules and regulations regarding the family pass. SM understands it is not guaranteed to be approved.
    
7. What (is needed from higher): Approval from the Battalion Commander.
    
+1 (Requires Notification to CAC / TRADOC CDR)
    """
    
    return subject_line, bluf

@app.route('/', methods=['GET', 'POST'])
def home():
    subject_line = bluf = None
    if request.method == 'POST':
        rank = request.form['rank']
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        age = request.form['age']
        sex = request.form['sex']
        race = request.form['race']
        component = request.form['component']
        relative = request.form['relative']
        relationship = request.form['relationship']
        contact_number = request.form['contact_number']
        dates_of_fp = request.form['dates_of_fp']
        
        subject_line, bluf = generate_document(rank, last_name, first_name, age, sex, race, component, relative, relationship, contact_number, dates_of_fp)
    
    return render_template_string(form_template, subject_line=subject_line, bluf=bluf)

if __name__ == "__main__":
    app.run(debug=True)
