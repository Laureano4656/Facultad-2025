package Ejercicio5;

public abstract class Material {
    private String color;

    public Material(String color) {
        this.color = color;
    }
    public String getColor() {
        return color;
    }
    public abstract String trabajarMaterial(Artesano artesano);
}
