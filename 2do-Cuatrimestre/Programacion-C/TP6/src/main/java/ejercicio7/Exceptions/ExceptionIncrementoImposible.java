package ejercicio7.Exceptions;

public class ExceptionIncrementoImposible extends Exception {
    private double maxDistanciaSoportada;
    private double distanciaPretendida;
    public ExceptionIncrementoImposible(String message, double maxDistanciaSoportada, double distanciaPretendida) {
        super(message);
    }
    public double getMaxDistanciaSoportada() {
        return maxDistanciaSoportada;
    }
    public double getDistanciaPretendida() {
        return distanciaPretendida;
    }
    
}
