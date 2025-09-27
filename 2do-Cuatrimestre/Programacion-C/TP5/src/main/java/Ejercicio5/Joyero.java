package Ejercicio5;

public class Joyero extends Artesano {
    public Joyero(String nombre) {
        super(nombre);
    }
    public String trabajarMadera(Madera madera){
       return "El joyero " + this.getNombre() + " fabrico un aro de " + madera.getTipoMadera();
    }
    public String trabajarMetal(Metal metal){
       return "El joyero " + this.getNombre() + " fabrico un anillo " + metal.getColor();
    }
//    @Override
//    public void trabajar(Material material) {
//
//    }
}
