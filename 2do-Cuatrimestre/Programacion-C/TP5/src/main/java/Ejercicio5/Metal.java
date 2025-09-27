package Ejercicio5;

public class Metal extends Material {
    private String tipoMetal;

    public Metal(String tipoMetal, String color) {
        super(color);
        this.tipoMetal = tipoMetal;
    }

    public String getTipoMetal() {
        return tipoMetal;
    }

    @Override
    public String trabajarMaterial(Artesano artesano) {
       return artesano.trabajarMetal(this);
    }
    @Override
    public String toString() {
        return "Metal [color=" + getColor() + ", tipoMetal=" + tipoMetal + "]";
    }

}
