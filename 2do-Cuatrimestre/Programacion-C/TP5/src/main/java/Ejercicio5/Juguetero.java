package Ejercicio5;

public class Juguetero extends Artesano {
    public Juguetero(String nombre) {
        super(nombre);
    }
    public String trabajarMadera(Madera madera){
        return "El juguetero " + this.getNombre() + " fabrico un muñequito de " + madera.getTipoMadera();
    }
    public String trabajarMetal(Metal metal){
        return "El juguetero " + this.getNombre() + " fabrico un autito " + metal.getColor();
    }
//    @Override
//    public void trabajar(Material material) {
//        material.trabajarMaterial(material);
//    }
}
