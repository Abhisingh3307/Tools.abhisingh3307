<!DOCTYPE html>
<html>
<head>
    <title>Universal Debugger</title>
    <style>
        textarea { width: 100%; height: 300px; }
        pre { background: #f0f0f0; padding: 10px; }
    </style>
</head>
<body>
    <h2>🧠 Universal Code Debugger (Multi-Language)</h2>
    <form method="post">
        <textarea name="code" placeholder="Paste your code here...">{{ code }}</textarea><br>
        <button type="submit">🔍 Debug & Run</button>
    </form>
    <hr>
    <h3>✅ Output:</h3>
    <pre>{{ stdout }}</pre>
    <h3>❌ Error:</h3>
    <pre>{{ stderr }}</pre>
    <h3>📊 Status: {{ status }}</h3>
</body>
</html>
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
