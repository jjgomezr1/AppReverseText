from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inversor de Texto Efímero</title>
    <style>
        body { font-family: system-ui, sans-serif; max-width: 600px; margin: 40px auto; padding: 0 20px; color: #333; }
        textarea { width: 100%; height: 100px; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; font-family: inherit; }
        button { padding: 10px 15px; background: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; margin-top: 10px; }
        .result-box { background: #f0f4f8; border-left: 4px solid #007bff; padding: 15px; margin-top: 20px; border-radius: 0 4px 4px 0; word-break: break-word; }
        .result-box p { font-size: 1.2em; font-weight: 500; margin: 5px 0 0 0; color: #111; }
        .info { font-size: 0.85em; color: #666; margin-top: 30px; }
    </style>
</head>
<body>
    <h2>Inversor de Texto (Efímero)</h2>
    <form method="POST">
        <textarea name="contenido" placeholder="Escribe o pega tu texto aquí..." required autofocus>{{ texto_original if texto_original else '' }}</textarea>
        <button type="submit">Invertir Texto</button>
    </form>

    {% if texto_invertido %}
    <div class="result-box">
        <small style="color: #555;">Texto al revés:</small>
        <p>{{ texto_invertido }}</p>
    </div>
    {% endif %}

    <p class="info">🔒 <strong>Cero rastro:</strong> Esta app procesa la inversión al vuelo. Si recargas o cierras la pestaña, todo desaparece.</p>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    texto_original = None
    texto_invertido = None

    if request.method == "POST":
        texto_original = request.form.get("contenido", "")
        # Invierte el texto usando slicing [::-1] de Python
        texto_invertido = texto_original[::-1]

    return render_template_string(
        HTML_TEMPLATE, 
        texto_original=texto_original, 
        texto_invertido=texto_invertido
    )

if __name__ == "__main__":
    app.run(debug=True)