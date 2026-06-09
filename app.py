from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>SUNEETHA ConfigMap + Secret Demo </title>
        <style>
            body {{
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #1f4037, #99f2c8);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}

            .card {{
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 15px 35px rgba(0,0,0,0.2);
                width: 400px;
                text-align: center;
                transition: transform 0.3s ease;
            }}

            .card:hover {{
                transform: scale(1.05);
            }}

            h2 {{
                color: #1f4037;
                margin-bottom: 20px;
            }}

            .info {{
                text-align: left;
                margin-top: 20px;
            }}

            .info p {{
                font-size: 16px;
                margin: 8px 0;
                padding: 8px;
                background: #f4f4f4;
                border-radius: 8px;
            }}

            .label {{
                font-weight: bold;
                color: #333;
            }}

            footer {{
                margin-top: 20px;
                font-size: 12px;
                color: gray;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>🚀 ConfigMap + Secret Demo</h2>
            <div class="info">
                <p><span class="label">ENV:</span> {os.getenv('ENV')}</p>
                <p><span class="label">END_POINT:</span> {os.getenv('END_POINT')}</p>
                <p><span class="label">DB_USER:</span> {os.getenv('DB_USER')}</p>
                <p><span class="label">DB_PASSWORD:</span> {os.getenv('DB_PASSWORD')}</p>
            </div>
            <footer>Cloud Computing in Telugu - Kubernetes Demo</footer>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
