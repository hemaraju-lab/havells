import logging
from flask import Flask

# Set up logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    handlers=[
                        logging.StreamHandler()
                    ])

app = Flask(__name__)

@app.route('/')
def hello():
    app.logger.info('Received request for /')
    return "Hello, world!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
