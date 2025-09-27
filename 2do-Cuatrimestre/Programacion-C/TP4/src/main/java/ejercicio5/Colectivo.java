package ejercicio5;

public class Colectivo extends Vehiculo {
    private int cantidadPasajeros;

    public Colectivo(String modelo, int cantidadPasajeros) {
        super(modelo);
        this.cantidadPasajeros = cantidadPasajeros;
    }
    @Override
    public boolean aceptoChofer(Chofer chofer) {
        if (this.cantidadPasajeros < 30) {
            return chofer.getCategoria().getHabilitaColectivoLinea();
        } else {
            return chofer.getCategoria().getHabilitaColectivoLarga();
        }
    }
    @Override
    public Acoplado getAcoplado() {
        return null;
    }
    @Override
    public String toString() {
        return "Colectivo{" +
                "cantidadPasajeros=" + cantidadPasajeros +
                "} " + super.toString();
    }
}
