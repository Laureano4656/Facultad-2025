package ejercicio1;

public class Vaca extends Perro implements Emsior_de_Sonido {
    public Vaca(String nombre, int esperanzaDeVida) {
        super(nombre, esperanzaDeVida);
    }

    @Override
    public void emitirSonido() {
        System.out.println("Muu Muu");
    }
}
