package ejercicio5;

public class Gato extends Animal implements Cloneable{


    public Gato(int esperanzaDeVida, String nombre) {
        super(esperanzaDeVida, nombre);
    }


    @Override
    public Object clone() throws CloneNotSupportedException {
        Gato clonado = null;
        clonado = (Gato) super.clone();
        return clonado;
    }
}
