package ejercicio4;

public class ConjuntoNumeros implements Cloneable{
    private Numero[] celda;
    private int largo;
    private String nombre;
    public ConjuntoNumeros(String nombre, int largo) {
        this.nombre = nombre;
        this.largo = largo;
        this.celda = new Numero[largo];
    }

    public Numero[] getCelda() {
        return celda;
    }

    public void setCelda(Numero[] celda) {
        this.celda = celda;
    }
    public void addNumero(Numero n, int posicion) {
        if (posicion >= 0 && posicion < largo) {
            this.celda[posicion] = n;
        } else {
            System.out.println("Posicion fuera de rango");
        }
    }
    public int getLargo() {
        return largo;
    }

    public void setLargo(int largo) {
        this.largo = largo;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    @Override
    protected Object clone() throws CloneNotSupportedException {
        ConjuntoNumeros clonado = (ConjuntoNumeros) super.clone();
        clonado.celda = this.celda.clone();
        return clonado;
    }
}
