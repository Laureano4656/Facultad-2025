package ejercicio4;

public class PermanenteIntermedio extends EmpleadoPermanente{
    public PermanenteIntermedio(String nombre, Domicilio domicilio, int antiguedad, double sueldoBase) {
        super(nombre, domicilio, antiguedad, calcularSueldoBase(sueldoBase, antiguedad));
    }

    private static double calcularSueldoBase(double sueldoBase, int antiguedad) {
        return sueldoBase * 1.25 + sueldoBase*((double) antiguedad /100);
    }
}
