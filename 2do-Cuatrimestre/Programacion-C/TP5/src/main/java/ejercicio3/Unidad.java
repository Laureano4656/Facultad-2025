package ejercicio3;

public abstract class Unidad {
    private String equipo;
    private int costo;
    private double energia;

    public Unidad(String equipo, int costo, double energia) {
        this.equipo = equipo;
        this.costo = costo;
        this.energia = energia;
    }

    public String getEquipo() {
        return equipo;
    }

    public void setEquipo(String equipo) {
        this.equipo = equipo;
    }

    public int getCosto() {
        return costo;
    }

    public void setCosto(int costo) {
        this.costo = costo;
    }

    public double getEnergia() {
        return energia;
    }

    public void setEnergia(double energia) {
        this.energia = energia;
    }

    public abstract void recibeDanio(int danio);
}
