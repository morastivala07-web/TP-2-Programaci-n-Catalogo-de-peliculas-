def main():
    while True:
        print("\nCatálogo de películas")
        print("1. Buscar por título")
        print("2. Filtrar por género")
        print("3. Ver películas mejor valoradas")
        print("4. Salir")

        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            print("La búsqueda por título estará disponible próximamente.")
        elif opcion == "2":
            print("El filtro por género estará disponible próximamente.")
        elif opcion == "3":
            print("La lista de valoraciones estará disponible próximamente.")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Ingresá un número del 1 al 4.")


if __name__ == "__main__":
    main()
