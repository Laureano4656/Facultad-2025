package ejercicio4;

public class PermanenteExperto extends EmpleadoPermanente{
    public PermanenteExperto(String nombre, Domicilio domicilio, int antiguedad, double sueldoBase) {
        super(nombre, domicilio, antiguedad, calcularSueldoBase(sueldoBase, antiguedad));
    }

    private static double calcularSueldoBase(double sueldoBase, int antiguedad) {
        return sueldoBase * 1.50 + sueldoBase * ((double) antiguedad * 1.5 / 100);
    }
}
