import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import telebot

# إعداد التطبيق
app = Flask(__name__)
CORS(app) # هذا السطر مهم جداً ليسمح للموقع بالاتصال بالبوت

# البيانات التي قدمتها
TOKEN = "8696528094:AAEC3N-h1eGvOQb9JBUdbk0C_QYZcBBvxxs"
CHAT_ID = "5428442515"
bot = telebot.TeleBot(TOKEN)

@app.route('/')
def home():
    return "Bot is Running Successfully!"

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    user_msg = data.get('message', 'رسالة فارغة')
    
    try:
        bot.send_message(CHAT_ID, f"🔔 تنبيه جديد من موقعك:\n\n{user_msg}")
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
