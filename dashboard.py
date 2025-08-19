from flask import Flask, render_template_string
import os

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Rede - Monitoramento de Rede</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, ##f7f1e1, #2a5298);
            color: #00000;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .card {
            background: rgba(255, 255, 255, 0.1);
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0px 8px 20px rgba(0,0,0,0.3);
        }
        h1 {
            margin-bottom: 20px;
            font-size: 2em;
        }
        .status {
            font-size: 2em;
            font-weight: bold;
            padding: 20px;
            border-radius: 12px;
            display: inline-block;
            margin-top: 20px;
        }
        .online {
            background: #4caf50;
            color: white;
            animation: pulse 1.5s infinite;
        }
        .offline {
            background: #f44336;
            color: white;
            animation: blink 1s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        @keyframes blink {
            0%, 50%, 100% { opacity: 1; }
            25%, 75% { opacity: 0.5; }
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>🌐 Rede</h1>
        <div class="status {{status_class}}">
            {{status}}
        </div>
    </div>
</body>
</html>
"""

def ping_host(ip="8.8.8.8"):
    resposta = os.system(f"ping -n 1 {ip} > nul")  # para Windows
    return resposta == 0

@app.route("/")
def home():
    if ping_host():
        return render_template_string(TEMPLATE, status="✅ Online", status_class="online")
    else:
        return render_template_string(TEMPLATE, status="❌ Offline", status_class="offline")

if __name__ == "__main__":
    app.run(debug=True)
