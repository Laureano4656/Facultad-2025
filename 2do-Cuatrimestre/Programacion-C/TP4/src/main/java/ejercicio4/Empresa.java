package ejercicio4;

import java.util.ArrayList;

public class Empresa {
    private ArrayList<Vehiculo> vehiculos ;
    public Empresa() {
        this.vehiculos = new ArrayList<Vehiculo>();
    }
    public void agregarVehiculo(Vehiculo v) {
        this.vehiculos.add(v);
    }
    /**
     * Calcula el precio de alquiler de un vehículo según su patente y los días de alquiler.
     * @param patente La patente del vehículo.
     * @param dias La cantidad de días que se desea alquilar el vehículo.
     * @return El precio total del alquiler o -1 si no se encuentra el vehículo.
     * @throws Exception Si ocurre un error al calcular el precio.
     */
    public double calcularPrecioAlquiler(String patente, int dias) throws  Exception{
        for (Vehiculo v : vehiculos) {
            if (v.getPatente().equals(patente)) {
                v.setDiasAlquiler(dias);
                return v.calcularPrecio();
            }
        }
        return -1; // Si no se encuentra el vehículo, se retorna -1
    }
    public ArrayList<Vehiculo> getVehiculos() {
        return vehiculos;
    }
}
