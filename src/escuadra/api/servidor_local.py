"""
Servidor HTTP local para exponer herramientas de Escuadra.

El servidor está desactivado por defecto y debe iniciarse
explícitamente para permitir integraciones externas.
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class ServidorEscuadra(BaseHTTPRequestHandler):
    """Manejador HTTP local de Escuadra."""

    def do_POST(self):
        """Procesa solicitudes POST."""

        if not self.path.startswith("/calcular/"):
            self.send_response(404)
            self.end_headers()
            return

        longitud = int(self.headers.get("Content-Length", 0))
        datos = self.rfile.read(longitud)

        try:
            parametros = json.loads(datos.decode("utf-8"))

            respuesta = {
                "herramienta": self.path.replace("/calcular/", ""),
                "parametros": parametros,
                "resultado": None,
            }

            contenido = json.dumps(respuesta).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(contenido)

        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()


def iniciar_servidor(host="localhost", puerto=8000):
    """
    Inicia el servidor HTTP local.

    Solo escucha en localhost por seguridad.
    """

    servidor = HTTPServer((host, puerto), ServidorEscuadra)

    print(f"Servidor iniciado en http://{host}:{puerto}")
    servidor.serve_forever()


if __name__ == "__main__":
    iniciar_servidor()
