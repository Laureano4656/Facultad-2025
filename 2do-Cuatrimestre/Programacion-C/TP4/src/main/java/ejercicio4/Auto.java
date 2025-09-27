package ejercicio4;

public class Auto extends Vehiculo{
    private int plazas;

    public Auto(String patente) {
        super(patente);
        this.plazas = 5;
    }
    public Auto(String patente, int plazas) {
        super(patente);
        this.plazas = plazas;
    }
    public int getPlazas() {
        return plazas;
    }
    public void setPlazas(int plazas) {
        this.plazas = plazas;
    }

    /**
     * Calcular precio del alquiler de un auto
     * Precio base + 1.5% del precio base por cada plaza
     * Multiplicado por la cantidad de días de alquiler
     * this.plazas > 1
     * @throws  Exception si la cantidad de plazas es menor a 1
     * @return el precio del alquiler
     */
    @Override
    public double calcularPrecio() throws Exception{
        assert this.plazas > 0 : "La cantidad de plazas debe ser mayor a 0";
        return (Vehiculo.getPrecioBase() + (Vehiculo.getPrecioBase()*this.plazas*0.015)) * this.getDiasAlquiler();
    }
}
