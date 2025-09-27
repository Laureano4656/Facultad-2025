package ejercicio5;

public class Domicilio implements Cloneable {
    private String calle;
    private int numero;

    public Domicilio(String calle, int numero) {
        this.calle = calle;
        this.numero = numero;
    }

    @Override
    public Object clone() throws CloneNotSupportedException {
        Domicilio clonado = null;
        clonado = (Domicilio) super.clone();
        return clonado;
    }

    public String getCalle() {
        return calle;
    }

    public void setCalle(String calle) {
        this.calle = calle;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }
}
