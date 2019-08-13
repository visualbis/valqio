from eve import Eve
from dotenv import load_dotenv
from flask_cors import CORS
import os

if os.environ.get("ENV", None) == None:
    load_dotenv()

app = Eve()
CORS(app)

if __name__ == '__main__':
    app.run()
