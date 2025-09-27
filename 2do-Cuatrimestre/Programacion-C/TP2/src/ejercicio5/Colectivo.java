package ejercicio5;

public class Colectivo {
    private String modelo;
    private static int contador = 0;
    private int numerointerno;


    public Colectivo(String modelo) {
        this.modelo = modelo;
        contador++;
        this.numerointerno = contador;
    }

    public int getNumerointerno() {
        return numerointerno;
    }
    public String getModelo() {
        return modelo;
    }
    public void setModelo(String modelo) {
        this.modelo = modelo;
    }
    @Override
    public String toString() {
        return "Colectivo{" +
                "modelo='" + modelo + '\'' +
                ", numerointerno=" + numerointerno +
                '}';
    }
}
