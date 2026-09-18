class Asistente:
    def __init__(self, nombre_negocio):
        self.nombre_negocio = nombre_negocio
        self.historial = []
        self.preguntas_frecuentes = {
            "horario": "Nuestro horario es de lunes a viernes, de 9:00 a 18:00.",
            "ubicacion": "Estamos ubicados en el centro de la ciudad.",
            "precios": "Puedes consultar nuestros precios en el negocio.",
        }

    def buscar_faq(self, mensaje_normalizado):
        for clave, respuesta in self.preguntas_frecuentes.items():
            if clave in mensaje_normalizado:
                return respuesta

        return "No entendi tu mensaje."

    def responder(self, mensaje):
        self.historial.append(mensaje)
        mensaje_normalizado = mensaje.casefold()

        if "hola" in mensaje_normalizado or "buenas" in mensaje_normalizado:
            respuesta = f"Hola, bienvenido a {self.nombre_negocio}."
        else:
            respuesta = self.buscar_faq(mensaje_normalizado)

        self.historial.append(respuesta)
        return respuesta
