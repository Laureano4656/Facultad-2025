package Ejercicio5;

public abstract class Artesano {
    private String nombre;

    public Artesano(String nombre) {
        this.nombre = nombre;
    }
    public String getNombre() {
        return nombre;
    }
    public String trabajar(Material material){
        return material.trabajarMaterial(this);
    }
    public abstract String trabajarMadera(Madera madera);
    public abstract String trabajarMetal(Metal metal);
}
