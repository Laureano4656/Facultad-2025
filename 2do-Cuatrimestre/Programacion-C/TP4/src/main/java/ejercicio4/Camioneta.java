package ejercicio4;

public class Camioneta extends Vehiculo{
    private double PMA;
    public Camioneta(String patente, double PMA) {
        super(patente);
        this.PMA = PMA;
    }
    public Camioneta(String patente) {
        super(patente);
        this.PMA = 3500;
    }
    public double getPMA() {
        return PMA;
    }
    public void setPMA(double PMA) {
        this.PMA = PMA;
    }
    /** El precio de alquiler de una camioneta se calcula como:
     * Precio base + 20% del precio base por cada tonelada de PMA
     * Multiplicado por la cantidad de días de alquiler
     * this.PMA > 0
     * @throws Exception si la PMA es menor o igual a 0
     * @return el precio del alquiler
     */
    @Override
    public double calcularPrecio() throws Exception{
        assert this.PMA > 0 : "La PMA debe ser mayor a 0";
        return (Vehiculo.getPrecioBase() + (Vehiculo.getPrecioBase()*this.PMA*0.2)) * this.getDiasAlquiler();
    }
}
