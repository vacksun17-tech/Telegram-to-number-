import os
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

TARGET_API = "https://api.igfollows.site/TG/index.php"

@app.route('/TG/index.php', methods=['GET'])
def proxy_gateway():
    params = request.args.to_dict()
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(TARGET_API, params=params, headers=headers, timeout=10)
        data = response.json()
        
        # --- Yahan hum faltu tags ko delete kar rahe hain ---
        if "developer" in data: del data["developer"]
        if "tag" in data: del data["tag"]
        if "key_expiry" in data: del data["key_expiry"]
        
        # --- Ab apne tags set karo ---
        data["admin"] = "@YuIin"
        data["owner"] = "@kihoerack"
        
        return jsonify(data)

    except Exception as e:
        return jsonify({"success": False, "message": "Error", "error": str(e)}), 502

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    
