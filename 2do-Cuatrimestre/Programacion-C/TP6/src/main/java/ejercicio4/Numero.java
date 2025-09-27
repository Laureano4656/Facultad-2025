package ejercicio4;

public class Numero implements Cloneable {
    int dato;

    public Numero(int dato) {
        this.dato = dato;
    }
    public Numero() {
        this.dato = 0;
    }
    int getDato() {
        return dato;
    }

    void setDato(int dato) {
        this.dato = dato;
    }

    @Override
    protected Object clone() {
        Numero clonado = null;
        try {
            clonado = (Numero) super.clone();
        } catch (CloneNotSupportedException e) {
            e.printStackTrace();
        }
        return clonado;
    }
}
