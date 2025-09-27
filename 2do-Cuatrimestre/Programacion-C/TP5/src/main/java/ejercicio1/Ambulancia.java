package ejercicio1;

public class Ambulancia extends Vehiculo implements Emsior_de_Sonido {
    public Ambulancia(String patente, String numeroDeChasis, String numeroMotor) {
        super(patente, numeroDeChasis, numeroMotor);
    }

    @Override
    public void emitirSonido() {
        System.out.println("Neee Neee");
    }
}
