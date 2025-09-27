package ejercicio1;

public class Gato extends Animal implements Emsior_de_Sonido {
    public Gato(String nombre, int esperanzaDeVida) {
        super(nombre, esperanzaDeVida);
    }

    @Override
    public void emitirSonido() {
        System.out.println("Miau Miau");
    }
}
