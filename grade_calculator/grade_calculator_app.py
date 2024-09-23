from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    prelim_grade = None

    if request.method == 'POST':
        try:
            prelim_grade = float(request.form['prelim_grade'])

            if 0 <= prelim_grade <= 100:
                required_midterm = (75 - (prelim_grade * 0.2)) / 0.3
                required_final = (75 - (prelim_grade * 0.2) - (required_midterm * 0.3)) / 0.5

                dean_lister_midterm = (90 - (prelim_grade * 0.2)) / 0.3
                dean_lister_final = (90 - (prelim_grade * 0.2) - (dean_lister_midterm * 0.3)) / 0.5

                chance_to_pass = required_midterm <= 100 and required_final <= 100
                result = {
                    'prelim_grade': prelim_grade,
                    'required_midterm': required_midterm,
                    'required_final': required_final,
                    'chance_to_pass': "You have a chance to pass!" if chance_to_pass else "It is difficult to pass.",
                    'dean_lister_midterm': dean_lister_midterm,
                    'dean_lister_final': dean_lister_final
                }
            else:
                result = "Please enter a grade between 0 and 100."
        except ValueError:
            result = "Invalid input. Please enter a numerical grade."

    return render_template('index.html', result=result, prelim_grade=prelim_grade)

if __name__ == '__main__':
    app.run(debug=True)
