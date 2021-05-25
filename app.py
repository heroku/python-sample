import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    app_name = os.environ.get('APP_NAME', '[set APP_NAME env var]')
    return 'Hello World from {}!'.format(app_name)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
