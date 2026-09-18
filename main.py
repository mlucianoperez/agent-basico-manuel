from asistente import Asistente
from conversacion import iniciar_conversacion


def main():
    asistente = Asistente("Salon premium")
    iniciar_conversacion(asistente)


if __name__ == "__main__":
    main()