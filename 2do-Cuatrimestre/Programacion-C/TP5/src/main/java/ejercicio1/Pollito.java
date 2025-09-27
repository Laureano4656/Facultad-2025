package ejercicio1;

public class Pollito extends Animal implements Emsior_de_Sonido {
    public Pollito(String nombre, int esperanzaDeVida) {
        super(nombre, esperanzaDeVida);
    }

    @Override
    public void emitirSonido() {
        System.out.println("Pio Pio");
    }
}
