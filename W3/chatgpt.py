import math

# Constantes
WATER_DENSITY = 998.2  # kg/m³
EARTH_ACCELERATION_OF_GRAVITY = 9.80665  # m/s²
WATER_DYNAMIC_VISCOSITY = 0.0010016  # Pa.s

def water_column_height(tower_height, tank_height):
    """Calcula la altura de la columna de agua."""
    return tower_height + (3 / 4) * tank_height

def pressure_gain_from_water_height(height):
    """Calcula la presión debido a la gravedad en kPa."""
    return (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calcula la pérdida de presión por fricción en una tubería."""
    return (-friction_factor * pipe_length * WATER_DENSITY * fluid_velocity ** 2) / (2000 * pipe_diameter)

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Calcula la pérdida de presión debido a accesorios (codos, uniones)."""
    return (-0.04 * WATER_DENSITY * fluid_velocity ** 2 * quantity_fittings) / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calcula el número de Reynolds para predecir el flujo del agua en una tubería."""
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Calcula la pérdida de presión debido a una reducción en el diámetro de la tubería."""
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter) - 1) ** 4
    return (-k * WATER_DENSITY * fluid_velocity ** 2) / 2000

# Función principal para probar la entrada del usuario
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    # Parámetros de la tubería de suministro
    PVC_SCHED80_INNER_DIAMETER = 0.28687
    PVC_SCHED80_FRICTION_FACTOR = 0.013
    SUPPLY_VELOCITY = 1.65

    reynolds = reynolds_number(PVC_SCHED80_INNER_DIAMETER, SUPPLY_VELOCITY)
    loss = pressure_loss_from_pipe(PVC_SCHED80_INNER_DIAMETER, length1, PVC_SCHED80_FRICTION_FACTOR, SUPPLY_VELOCITY)
    pressure += loss

    loss = pressure_loss_from_fittings(SUPPLY_VELOCITY, quantity_angles)
    pressure += loss

    HDPE_SDR11_INNER_DIAMETER = 0.048692
    loss = pressure_loss_from_pipe_reduction(PVC_SCHED80_INNER_DIAMETER, SUPPLY_VELOCITY, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    # Parámetros de la tubería de casa
    HDPE_SDR11_FRICTION_FACTOR = 0.018
    HOUSEHOLD_VELOCITY = 1.75

    loss = pressure_loss_from_pipe(HDPE_SDR11_INNER_DIAMETER, length2, HDPE_SDR11_FRICTION_FACTOR, HOUSEHOLD_VELOCITY)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")

if __name__ == "__main__":
    main()
