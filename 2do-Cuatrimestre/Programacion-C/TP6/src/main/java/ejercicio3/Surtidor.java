package ejercicio3;

import ejercicio3.exception.CargaInvalidaException;
import ejercicio3.exception.DatoCargaInvalido;
import ejercicio3.exception.FaltaCombustibleException;
import ejercicio3.exception.TipoCombustibleInvalidoException;

public class Surtidor {
    private static final double MAX_CAPACIDAD = 20000.0; // Capacidad máxima en litros
    private double cantidadDiesel;
    private double cantidadPremium;
    private double cantidadSuper;

    public Surtidor() {
        this.cantidadDiesel = MAX_CAPACIDAD;
        this.cantidadPremium = MAX_CAPACIDAD;
        this.cantidadSuper = MAX_CAPACIDAD;
    }
    public double getCantidadDiesel() {
        return cantidadDiesel;
    }
    public double getCantidadPremium() {
        return cantidadPremium;
    }
    public double getCantidadSuper() {
        return cantidadSuper;
    }
    public void cargarCombustible(String tipoCombustible, double cantidad) throws CargaInvalidaException, TipoCombustibleInvalidoException, FaltaCombustibleException {

        switch (tipoCombustible.toLowerCase()) {
            case "diesel":
                if (cantidad <= 0) {
                    throw new CargaInvalidaException(new DatoCargaInvalido(cantidadDiesel, cantidad, tipoCombustible));
                }
                if (cantidad > cantidadDiesel) {
                    throw new FaltaCombustibleException(this.cantidadDiesel, cantidad, tipoCombustible);
                }
                cantidadDiesel -= cantidad;
                break;
            case "premium":
                if (cantidad > cantidadPremium) {
                    throw new FaltaCombustibleException(this.cantidadPremium, cantidad, tipoCombustible);
                }
                cantidadPremium -= cantidad;
                break;
            case "super":
                if (cantidad > cantidadSuper) {
                    throw new FaltaCombustibleException(this.cantidadSuper, cantidad, tipoCombustible);
                }
                cantidadSuper -= cantidad;
                break;
            default:
                throw new TipoCombustibleInvalidoException(0, cantidad, tipoCombustible);
        }

    }
    public void llenarDisel(){
        this.cantidadDiesel = MAX_CAPACIDAD;
    }
    public void llenarPremium(){
        this.cantidadPremium = MAX_CAPACIDAD;
    }
    public void llenarSuper(){
        this.cantidadSuper = MAX_CAPACIDAD;
    }

}
