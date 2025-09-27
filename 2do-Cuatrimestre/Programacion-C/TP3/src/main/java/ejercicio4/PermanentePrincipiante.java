package ejercicio4;

public class PermanentePrincipiante extends EmpleadoPermanente {

    public PermanentePrincipiante(String nombre, Domicilio domicilio, int antiguedad, double sueldoBase) {
        super(nombre, domicilio, antiguedad, calcularSueldoBase(sueldoBase, antiguedad));
    }

    private static double calcularSueldoBase(double sueldoBase, int antiguedad) {
        if (antiguedad >= 2 && antiguedad <= 4) {
            return sueldoBase * 1.05;
        } else if (antiguedad >= 5 && antiguedad <= 9) {
            return sueldoBase * 1.07;
        } else if (antiguedad >= 10 && antiguedad <= 14) {
            return sueldoBase * 1.15;
        } else {
            return sueldoBase * 1.20;
        }
    }
}