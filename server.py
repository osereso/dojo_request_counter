from flask import Flask, request, render_template, redirect

app = Flask(__name__)

def read_file(file_name):
    result = {}
    with open(file_name, 'r') as f:
        for line in f:
            line_list = line.split(': ')
            result[line_list[0]] = int(line_list[1])
    return result


def write_file(file_name, data):
    with open(file_name, 'w') as f:
        for item in data.items():
            f.write(item[0] + ': ' + str(item[1]) + '\n')


@app.route('/')
def index():
    counts = read_file('request_counts.txt')
    return str(counts)


@app.route('/request-counter')
def increment():
    counts = read_file('request_counts.txt')
    counts['GET'] += 1
    write_file('request_counts.txt', counts)
    return redirect('/')


if __name__ == '__main__':
    app.run(port=9999, debug=True)
