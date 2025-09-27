package ejercicio4;

public class Prueba {
    public  static void main(String[] args) throws Exception
    {
        Camioneta camioneta1 = new Camioneta("ABC123", 2500);
        camioneta1.setDiasAlquiler(3);
        System.out.println("El precio del alquiler de la camioneta es: " + camioneta1.calcularPrecio());

        Camion camion1 = new Camion("DEF456");
        camion1.setDiasAlquiler(5);
        System.out.println("El precio del alquiler del camión es: " + camion1.calcularPrecio());
    }
}
