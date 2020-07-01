from flask import Flask, jsonify

app = Flask(__name__)

courses = [{'Name ': "Python with flask API",
            'Course_ID': "0",
            'Description': "Learning API",
            'Fees' : "Depend on the units you have taken"},
           {'Name ': "API with flask Application programing interface",
            'Course_ID': "1",
            'Description': "server with API",
            'Fees': "Will be calculated yearly"},
           {'Name ': "Python",
            'Course_ID': "2",
            'Description': "Interesting programing language",
            'Fees': "Online learning is free"},
           {'Name ': "C++",
            'Course_ID': "3",
            'Description': "C++ is fun to learn",
            'Fees': "PDF books are available online"}]

@app.route('/')
def index():
    return "wellcome to the API Appalication"


@app.route('/courses', methods=['GET'])
def get():
    return jsonify({'Courses ': courses})

@app.route("/courses/<int:Course_ID>", methods=['GET'])
def getCourses(Course_ID):
    return jsonify({'Courses ': courses[Course_ID]})

@app.route("/courses", methods=['POST'])
def create():
    course = {'Name ': "web development ",
            'Course_ID': "4",
            'Description': "Online learning is fun",
            'Fees': "PDF books are available online"}

    courses.append(course)
    return jsonify({'created ': course})


if __name__ == "__main__":
    app.run(degub=True)