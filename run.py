from eve import Eve
from dotenv import load_dotenv
from flask_cors import CORS
load_dotenv()

app = Eve()
CORS(app)

if __name__ == '__main__':
    app.run()
