if __name__ == "__main__":
    # Leer el resultado desde el archivo energy.res
    energy_result_file = "scores/energy/energy.res"
    with open(energy_result_file, "r") as file:
        energy_result = float(file.read())

    # Leer el resultado desde el archivo entropy.res
    entropy_result_file = "scores/entropy/entropy.res"
    with open(entropy_result_file, "r") as file:
        entropy_result = float(file.read())

    # Leer el resultado desde el archivo temperature.res
    temperature_result_file = "scores/temperature/temperature.res"
    with open(temperature_result_file, "r") as file:
        temperature_result = float(file.read())

    # Realizar las operaciones matemáticas
    discerned = energy_result - (temperature_result * entropy_result)

    # Guardar el resultado en el archivo discerned.res
    discerned_result_file = "scores/similarity/similarity.res"
    with open(discerned_result_file, "w") as file:
        file.write(str(discerned))
