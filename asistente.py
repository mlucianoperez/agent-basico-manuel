class Asistente:
    def __init__(self, nombre_negocio):
        self.nombre_negocio = nombre_negocio
        self.historial = []

    def responder(self, mensaje):
        self.historial.append(mensaje)

        if "hola" in mensaje.casefold() or "buenas" in mensaje.casefold():
            respuesta = f"Hola, bienvenido a {self.nombre_negocio}."
            self.historial.append(respuesta)
            return respuesta
