# Inversor de Texto Efímero

Aplicación web minimalista que invierte el texto ingresado en tiempo real sin guardar datos.

## Características
- **Inversión al vuelo:** Utiliza `[::-1]` de Python para voltear cualquier cadena de texto al instante.
- **Sin Persistencia:** No almacena cookies, variables en memoria ni registros en disco. Al recargar la página la sesión queda limpia.

## Uso local (desarrollo)

1. Crear y activar entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecutar (servidor de desarrollo de Flask, puerto 5000):
   ```bash
   python app.py
   ```

4. En el navegador abrir http://127.0.0.1:5000 .

## Despliegue en EC2 (para el auto-scaling controller)

En este proyecto, la app corre en instancias EC2 detrás de un Application Load
Balancer. Se sirve con **gunicorn en el puerto 80** (servidor de producción) y
como **servicio systemd**, para que arranque sola al bootear y se reinicie ante
fallas. Así cada instancia lanzada por el controlador queda lista para recibir
tráfico sin intervención humana.

Pasos en una instancia Ubuntu 24.04 (usuario `ubuntu`):

```bash
sudo apt update
sudo apt install -y python3-pip python3-venv git

# Clonar la app en /home/ubuntu/app
cd /home/ubuntu
git clone https://github.com/jjgomezr1/AppReverseText.git app
cd app

# Entorno virtual e instalar dependencias (incluye gunicorn)
python3 -m venv venv
./venv/bin/pip install -r requirements.txt

# Instalar el servicio systemd (el archivo inversor.service viene en el repo)
sudo cp inversor.service /etc/systemd/system/inversor.service
sudo systemctl daemon-reload
sudo systemctl enable inversor
sudo systemctl start inversor

# Verificar que responde 200 en la raiz (health check del ALB)
curl -i http://localhost/
```

Una vez validado, se crea una **AMI dorada** a partir de esta instancia; el
controlador lanza copias de esa AMI. Ver la guía `fase-vpc-alb-aws.md` del
proyecto para el detalle completo.

### Notas de despliegue
- La app escucha en el puerto **80**; el health check del Target Group es
  `GET /` (responde 200).
- El servicio usa `Restart=always`, así que si el proceso muere, systemd lo
  revive.
- `gunicorn` sirve el objeto `app` del módulo `app.py` (`app:app`). El bloque
  `if __name__ == "__main__"` de `app.py` solo se usa en desarrollo local; en
  producción lo ignora gunicorn.
