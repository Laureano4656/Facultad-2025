package ejercicio1;

public class Perro extends Animal implements Emsior_de_Sonido {
    public Perro(String nombre, int esperanzaDeVida) {
        super(nombre, esperanzaDeVida);
    }

    @Override
    public void emitirSonido() {
        System.out.println("Guau Guau");
    }
}
