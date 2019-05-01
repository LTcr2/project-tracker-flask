"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student-info")
def get_student():
    """Show information about a student.
    /student-search routes to /student
    """

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    return render_template('student_info.html',
                            first=first,
                            last=last,
                            github=github)
    

    #return "{} is the GitHub account for {} {}".format(github, first, last)

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student"""

    return render_template("student_search.html")


@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""

    first  = request.form.get('first_name')
    last  = request.form.get('last_name')
    github  = request.form.get('github')
    hackbright.make_new_student(first, last, github)

    return render_template("/student-add.html")
                    # first = first,
                    # last=last,
                    # github=github)


@app.route("/confirmation-page")
def confirm_add():

    html = render_template('confirmation-page.html')
                            # first=first,
                            # last=last,
                            # github=github)


    return html

    #The method that handles the form results should return a template that acknowledges the user was added.
    #Have it provide a link (via an <a> tag) to the information page about the student.

    return html


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)


