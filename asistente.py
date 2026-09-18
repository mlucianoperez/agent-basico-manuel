class Asistente:
    def __init__(self, nombre_negocio):
        self.nombre_negocio = nombre_negocio
        self.nombre_usuario = None
        self.historial = []
        self.preguntas_frecuentes = {
            "horario": "Nuestro horario es de lunes a viernes, de 9:00 a 18:00.",
            "ubicacion": "Estamos ubicados en el centro de la ciudad.",
            "precios": "Puedes consultar nuestros precios en el negocio.",
        }
        self.precios_servicios = {
            "corte": 15.0,
            "manicure": 20.0,
            "pedicure": 25.0,
        }

    def calcular_presupuesto(self):
        servicio = input("Que servicio te interesa? ").strip().casefold()
        if servicio not in self.precios_servicios:
            return f"El servicio '{servicio}' no existe."

        try:
            cantidad = int(input("Cuantas veces quieres agendarlo? "))
        except ValueError:
            return "Por favor, introduce un numero valido."

        return self.precios_servicios[servicio] * cantidad

    def buscar_faq(self, mensaje_normalizado):
        for clave, respuesta in self.preguntas_frecuentes.items():
            if clave in mensaje_normalizado:
                return respuesta

        return "No entendi tu mensaje."

    def mostrar_historial(self):
        for quien, texto in self.historial:
            print(f"{quien}: {texto}")

    def mostar_historial(self):
        self.mostrar_historial()

    def responder(self, mensaje):
        self.historial.append(("Usuario", mensaje))
        mensaje_normalizado = mensaje.casefold()

        if any(palabra in mensaje_normalizado for palabra in ("adios", "salir", "chao")):
            if self.nombre_usuario:
                respuesta = f"Adios {self.nombre_usuario}, gracias por visitar {self.nombre_negocio}."
            else:
                respuesta = f"Adios, gracias por visitar {self.nombre_negocio}."
        elif mensaje_normalizado.startswith("me llamo"):
            nombre_usuario = mensaje[len("me llamo"):].strip()
            self.nombre_usuario = nombre_usuario.capitalize()
            respuesta = f"Hola {self.nombre_usuario}, bienvenido a {self.nombre_negocio}."
        elif any(palabra in mensaje_normalizado for palabra in ("calcular", "presupuesto", "costo")):
            respuesta = self.calcular_presupuesto()
        elif "hola" in mensaje_normalizado or "buenas" in mensaje_normalizado:
            if self.nombre_usuario:
                respuesta = f"Hola {self.nombre_usuario}, bienvenido a {self.nombre_negocio}."
            else:
                respuesta = f"Hola, bienvenido a {self.nombre_negocio}."
        else:
            respuesta = self.buscar_faq(mensaje_normalizado)

        self.historial.append(("Asistente", respuesta))
        return respuesta
