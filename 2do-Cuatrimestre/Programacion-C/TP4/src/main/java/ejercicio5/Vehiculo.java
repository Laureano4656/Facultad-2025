package ejercicio5;

public abstract class Vehiculo {
    private String modelo;
    private static int numeroIntero = 0;
    private int numeroInternoVehiculo;

    public Vehiculo(String modelo) {
        this.modelo = modelo;
        numeroIntero++;
        this.numeroInternoVehiculo = numeroIntero;
    }

    public abstract boolean aceptoChofer(Chofer chofer);
    public abstract Acoplado getAcoplado();
    @Override
    public String toString() {
        return "Vehiculo{" +
                "modelo='" + modelo + '\'' +
                ", numeroInternoVehiculo=" + numeroInternoVehiculo +
                '}';
    }
}
