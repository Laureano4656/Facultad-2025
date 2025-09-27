package Ejercicio5;

public class Madera extends Material {
    private String tipoMadera;

    public Madera(String tipoMadera, String color) {
        super(color);
        this.tipoMadera = tipoMadera;
    }

    public String getTipoMadera() {
        return tipoMadera;
    }

    @Override
    public String trabajarMaterial(Artesano artesano) {
        return artesano.trabajarMadera(this);
    }
    @Override
    public String toString() {
        return "Madera [color=" + getColor() + ", tipoMadera=" + tipoMadera + "]";
    }
}
