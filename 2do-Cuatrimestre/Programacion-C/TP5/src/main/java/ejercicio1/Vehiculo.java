package ejercicio1;

public abstract class Vehiculo {
    private String patente;
    private String numeroDeChasis;
    private String numeroMotor;

    public Vehiculo(String patente, String numeroDeChasis, String numeroMotor) {
        this.patente = patente;
        this.numeroDeChasis = numeroDeChasis;
        this.numeroMotor = numeroMotor;
    }

    public String getPatente() {
        return patente;
    }

    public void setPatente(String patente) {
        this.patente = patente;
    }

    public String getNumeroDeChasis() {
        return numeroDeChasis;
    }

    public void setNumeroDeChasis(String numeroDeChasis) {
        this.numeroDeChasis = numeroDeChasis;
    }

    public String getNumeroMotor() {
        return numeroMotor;
    }

    public void setNumeroMotor(String numeroMotor) {
        this.numeroMotor = numeroMotor;
    }
}
