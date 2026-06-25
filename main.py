import os
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Target API URL
TARGET_API = "https://api.igfollows.site/TG/index.php"

@app.route('/TG/index.php', methods=['GET'])
def proxy_gateway():
    # User ke bheje gaye params lo
    params = request.args.to_dict()
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        # Target site se data fetch karo
        response = requests.get(TARGET_API, params=params, headers=headers, timeout=10)
        data = response.json()
        
        # Tags add karo
        data["admin"] = "@YuIin"
        data["owner"] = "@kihoerack"
        
        return jsonify(data)

    except Exception as e:
        return jsonify({"success": False, "message": "API Error", "error": str(e)}), 502

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
  
