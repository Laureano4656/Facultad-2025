package ejercicio5;

public class Camion extends Vehiculo {
    private double tara;
    private double cargaMaxima;
    private Acoplado acoplado;

    public Camion(String modelo, double tara, double cargaMaxima) {
        super(modelo);
        this.tara = tara;
        this.cargaMaxima = cargaMaxima;
        this.acoplado = null;
    }

    public void agregarAcoplado(Acoplado acoplado) {
        assert acoplado != null: "El acoplado no puede ser null";
        assert !acoplado.getEnUso() : "El acoplado ya está en uso";
        this.acoplado = acoplado;
        acoplado.setEnUso(true);
    }
    @Override
    public boolean aceptoChofer(Chofer chofer) {
        assert chofer != null : "El chofer no puede ser nulo";
        return chofer.getCategoria().getHabilitaCamion();
    }
    @Override
    public Acoplado getAcoplado() {
        return acoplado;
    }
    @Override
    public String toString() {
        return "Camion{" +
                "tara=" + tara +
                ", cargaMaxima=" + cargaMaxima +
                ", acoplado=" + (acoplado != null ? acoplado : "Ninguno") +
                "} " + super.toString();
    }
}
