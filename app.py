from flask import Flask, request, send_file, render_template_string
import os
import yara

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Define YARA rules
RULES = '''
rule access_key_rule {
    strings:
        // This is the ONLY string that will grant access.
        // Make this unique and difficult to guess!
        $secret_access_text = "Trust" ascii wide nocase
    condition:
        $secret_access_text
}
'''
compiled_rules = yara.compile(source=RULES)

# Write the flag file
FLAG_FILE = "flag.txt"
with open(FLAG_FILE, "w") as f:
    f.write("flag{no_lock_unpickable}")

# HTML theme (Six of Crows style)
HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kaz Brekker's Vault</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500&family=Share+Tech+Mono&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            font-family: 'Share Tech Mono', monospace;
            background: linear-gradient(to right, #232526, #414345);
            color: #f8f8f8;
            display: flex;
        }
        .sidebar {
            width: 220px;
            background-color: #111;
            padding: 20px;
            height: 100vh;
            box-shadow: 2px 0 10px rgba(0,0,0,0.3);
        }
        .sidebar h2 {
            color: #00ffe7;
            font-size: 1.3em;
            margin-bottom: 20px;
        }
        .sidebar ul {
            list-style: none;
            padding: 0;
        }
        .sidebar ul li {
            padding: 10px;
            color: #ccc;
            cursor: pointer;
            border-bottom: 1px solid #333;
        }
        .sidebar ul li:hover {
            background-color: #222;
            color: #00ffe7;
        }
        .main {
            flex-grow: 1;
            text-align: center;
            padding: 40px;
        }
        h1 {
            font-family: 'Orbitron', sans-serif;
            font-size: 3.5em;
            color: #00ffe7;
            margin-bottom: 0.2em;
            text-shadow: 0 0 10px #00ffe7;
        }
        p {
            font-size: 1.3em;
            color: #ddd;
        }
        form {
            margin: 30px auto;
            background: #292b2c;
            padding: 20px;
            border-radius: 10px;
            display: inline-block;
        }
        input[type="file"] {
            background-color: #444;
            border: 1px solid #888;
            color: #fff;
            padding: 10px;
            font-size: 1em;
            border-radius: 5px;
            width: 70%;
            margin: 4px;
        }
        input[type="submit"] {
            background-color: #00ffe7;
            border: none;
            color: black;
            padding: 12px 24px;
            font-size: 1em;
            border-radius: 5px;
            cursor: pointer;
            margin-left: 10px;
            transition: background-color 0.3s ease, box-shadow 0.3s ease;
        }
        input[type="submit"]:hover {
            background-color: #00ccb8;
            box-shadow: 0 0 8px #00ffe7, 0 0 12px #00ffe7;
        }
        .result {
            margin-top: 20px;
            font-size: 1.5em;
            color: #b2ffb2;
        }
        .error {
            color: #ff8080;
        }
        a {
            color: #00ffe7;
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            text-decoration: underline;
        }
        .decoy-buttons {
            margin-top: 40px;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 20px;
        }
        .decoy-buttons button {
            background-color: #222;
            color: #ccc;
            border: 1px solid #444;
            padding: 15px 25px;
            border-radius: 8px;
            font-size: 1em;
            cursor: pointer;
            transition: all 0.3s ease, box-shadow 0.3s ease;
        }
        .decoy-buttons button:hover {
            background-color: #333;
            color: #00ffe7;
            box-shadow: 0 0 10px #00ffe7, 0 0 20px #00ffe7;
        }
        .glitch {
            animation: glitch 1s infinite;
        }
        @keyframes glitch {
            0% { text-shadow: 2px 2px red; }
            25% { text-shadow: -2px -2px blue; }
            50% { text-shadow: 2px -2px lime; }
            75% { text-shadow: -2px 2px magenta; }
            100% { text-shadow: 0 0 2px white; }
        }
    </style>
</head>
<body>
    <div class="sidebar">
        <h2>🧠 Hacker Tools</h2>
        <ul>
            <li>🚀 Launch Exploit</li>
            <li>🧪 Scan for Weaknesses</li>
            <li>🧊 Freeze Firewall</li>
            <li>💣 Detonate Backdoor</li>
            <li>🔒 Lock Override</li>
        </ul>
    </div>
    <div class="main">
        <h1 class="glitch">Kaz Brekker's Vault 💼</h1>
        <p>Think you're clever enough to beat Kaz? Upload a file that passes the elite YARA inspection 🧐</p>
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file" required />
            <input type="submit" value="Upload 🔐" />
        </form>
        {% if result %}
            <div class="result {{ 'error' if 'Denied' in result else '' }}">{{ result }} {% if 'Denied' in result %}<br><em>🎩 Nice try, but Kaz saw that coming before you even booted your OS.</em>{% endif %}</div>
        {% endif %}
        {% if download_link %}
            <div class="result">🎉 Success! <a href="{{ download_link }}">Download your flag 🚩</a></div>
        {% endif %}

        <div class="decoy-buttons">
            <button onclick="alert('🤔 What is essential for a true alliance?')">🧈 Engage Butter Injector</button>
            <button onclick="alert('⛔ Access denied. Ask more politely.')">🙏 Ask Kaz Nicely</button>
            <button onclick="alert('💤 Nothing happened. Kaz is snoring now.')">😴 Put Guard to Sleep</button>
            <button onclick="alert('📡 Hacking Mars... failed.')">👽 Alien Packet Injector</button>
            <button onclick="alert('🐸 Frog protocol initiated. Please croak to continue.')">🐸 Launch Frog Protocol</button>
            <button onclick="alert('📞 Calling grandma for backup... she’s not answering.')">📞 Call Grandma Hacker</button>
            <button onclick="alert('🪦 You disturbed Kaz’s ancestors. Bad move.')">🪦 Disturb Ancient Hackers</button>
        </div>
    </div>
</body>
</html>

'''

# @app.route("/", methods=["GET", "POST"])
# def index():
#     result = ""
#     download_link = None
#     if request.method == "POST":
#         if "file" not in request.files:
#             result = "No file uploaded"
#         else:
#             file = request.files["file"]
#             filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#             file.save(filepath)

#             matches = compiled_rules.match(filepath)
#             if matches:
#                 result = "Access Denied: Suspicious patterns detected."
#             else:
#                 result = "Access Granted!"
#                 download_link = "/flag"
#     return render_template_string(HTML, result=result, download_link=download_link)

ALLOWED_EXTENSIONS = {'txt'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    download_link = None # This variable doesn't seem used in your provided snippet, but keeping it.

    if request.method == "POST":
        if "file" not in request.files:
            result = "No file part in the request." # More specific error
        else:
            file = request.files["file"]
            if file.filename == '':
                result = "No selected file."

            elif not allowed_file(file.filename):
                result = "Invalid file type. Only .txt files are allowed."
            else:
                file = request.files["file"]
                filepath = os.path.join(UPLOAD_FOLDER, file.filename)
                try:
                    file.save(filepath)

                    matches = compiled_rules.match(filepath)
                    if matches:
                        result = "Access Denied: Suspicious patterns detected."
                    else:
                        result = "Access Granted!"
                        download_link = "/flag"
                except Exception as e:
                    result = f"Error processing file: {e}"
                finally:
                    # Clean up the uploaded file after scanning (important for security and space)
                    if os.path.exists(filepath):
                        os.remove(filepath)
    return render_template_string(HTML, result=result, download_link=download_link)


@app.route("/flag")
def flag():
    return send_file(FLAG_FILE, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
