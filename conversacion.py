def iniciar_conversacion(asistente):
    print(f"Bienvenido a {asistente.nombre_negocio}.")

    while True:
        mensaje = input("Tu: ")
        respuesta = asistente.responder(mensaje)
        print(f"Asistente: {respuesta}")

        if any(palabra in mensaje.casefold() for palabra in ("adios", "chao", "salir")):
            break

    asistente.mostrar_historial()
