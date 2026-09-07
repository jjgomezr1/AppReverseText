# Inversor de Texto Efímero

Aplicación web minimalista que invierte el texto ingresado en tiempo real sin guardar datos.

## Características
- **Inversión al vuelo:** Utiliza `[::-1]` de Python para voltear cualquier cadena de texto al instante.
- **Sin Persistencia:** No almacena cookies, variables en memoria ni registros en disco. Al recargar la página la sesión queda limpia.

## Instalación y Uso

1. Crear y activar entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecutar:
   ```bash
   python app.py
   ```

4. En el navegador abir http://127.0.0.1:5000 .