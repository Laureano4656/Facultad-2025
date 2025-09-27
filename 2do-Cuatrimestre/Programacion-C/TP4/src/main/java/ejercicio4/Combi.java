package ejercicio4;

public class Combi extends Vehiculo {
    private double plazas;
    public Combi(String patente) {
        super(patente);
        this.plazas = 12;
    }
    public Combi(String patente, double plazas) {
        super(patente);
        this.plazas = plazas;
    }
    public double getPlazas() {
        return plazas;
    }
    public void setPlazas(double plazas) {
        this.plazas = plazas;
    }
    /**
     * Calcular precio del alquiler de una combi
     * Precio base + 2% del precio base por cada plaza
     * + 1.5% del precio base por cada plaza
     * Multiplicado por la cantidad de días de alquiler
     * this.plazas > 1
     * @throws Exception si la cantidad de plazas es menor a 1
     * @return el precio del alquiler
     */
    @Override
    public double calcularPrecio() throws  Exception{
        assert this.plazas > 0 : "La cantidad de plazas debe ser mayor a 0";
        return (Vehiculo.getPrecioBase() + (Vehiculo.getPrecioBase()*this.plazas*0.02) + (Vehiculo.getPrecioBase()*this.plazas*0.015)) * this.getDiasAlquiler();
    }
}
