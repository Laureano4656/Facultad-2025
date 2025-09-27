package ejercicio5;

import java.util.ArrayList;

public class Empresa {
    public ArrayList<Chofer> chofers;
    public ArrayList<Vehiculo> vehiculos;

    public Empresa() {
        this.chofers = new ArrayList<>();
        this.vehiculos = new ArrayList<>();
    }

    public Empresa(ArrayList<Chofer> chofers, ArrayList<Vehiculo> vehiculos) {
        this.chofers = chofers;
        this.vehiculos = vehiculos;
    }

    public boolean agregarChofer(Chofer chofer) {
        return this.chofers.add(chofer);
    }

    public boolean agregarVehiculo(Vehiculo vehiculo) {
        return this.vehiculos.add(vehiculo);
    }

    public int cantidadCategoria(Categoria categoria) {
        assert categoria != null : "La categoria no puede ser nula";
        int contador = 0;
        for (Chofer chofer : chofers) {
            if (chofer.getCategoria() == categoria) {
                contador++;
            }
        }
        return contador;
    }

    public int cantidadSinVehiculo() {
        int contador = 0;
        for (Chofer chofer : chofers) {
            if (chofer.getVehiculoAsignado() == null) {
                contador++;
            }
        }
        return contador;
    }

    public int cantVehiculos() {
        return this.vehiculos.size();
    }

    public int cantAcoplados() {
        int contador = 0;
        for (Vehiculo vehiculo : vehiculos) {
            if (vehiculo.getAcoplado() != null) {
                contador++;
            }
        }
        return contador;
    }
}
