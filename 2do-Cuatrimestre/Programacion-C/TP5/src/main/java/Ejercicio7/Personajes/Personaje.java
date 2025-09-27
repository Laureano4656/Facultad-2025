package Ejercicio7.Personajes;

public abstract class Personaje implements IPersonaje {
    private double armadura;
    private double danioAtaqueCorto;
    private double danioAtaqueLargo;
    private String nombre;

    public Personaje(String nombre, double armadura, double danioAtaqueCorto, double danioAtaqueLargo) {
        this.nombre = nombre;
        this.armadura = armadura;
        this.danioAtaqueCorto = danioAtaqueCorto;
        this.danioAtaqueLargo = danioAtaqueLargo;
    }
    @Override
    public String getNombre() {
        return nombre;
    }
    @Override
    public double getAtaqueCorto() {
        return danioAtaqueCorto;
    }
    @Override
    public double getAtaqueLargo() {
        return danioAtaqueLargo;
    }
    @Override
    public double getArmadura() {
        return armadura;
    }
}
