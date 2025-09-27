package ejercicio5;

public class Domicilio {
    private String calle;
    int numero;

    public Domicilio(String calle, int numero) {
       this.calle = calle;
       this.numero = numero;
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
    @Override
    public String toString() {
        return "Domicilio{" +
                "calle='" + calle + '\'' +
                ", numero=" + numero +
                '}';
    }
}
