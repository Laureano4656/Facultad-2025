package ejercicio5;

public class Perro extends Animal implements Cloneable {


    public Perro(int esperanzaDeVida, String nombre) {
        super(esperanzaDeVida, nombre);

    }




    public Object clone() throws CloneNotSupportedException {
        throw new CloneNotSupportedException("Not supported yet.");
    }
}