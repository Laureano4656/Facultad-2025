package ejercicio5;

public class Acoplado {
    private int tara;
    private int cargaMaxima;
    private boolean numeroAcoplado;
    private boolean enUso;

    public Acoplado(int tara, int cargaMaxima, boolean numeroAcoplado) {
        this.tara = tara;
        this.cargaMaxima = cargaMaxima;
        this.numeroAcoplado = numeroAcoplado;
        this.enUso = false;
    }
    public boolean getEnUso() {
        return enUso;
    }
    public void setEnUso(boolean enUso) {
        this.enUso = enUso;
    }
    @Override
    public String toString() {
        return "Acoplado{" +
                "tara=" + tara +
                ", cargaMaxima=" + cargaMaxima +
                ", numeroAcoplado=" + numeroAcoplado +
                ", enUso=" + enUso +
                '}';}
}
