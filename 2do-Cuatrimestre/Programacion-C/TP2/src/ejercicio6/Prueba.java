package ejercicio6;

public class Prueba {
    public static void main(String[] args) {
        Surtidor surtidor1 = new Surtidor();
        Surtidor surtidor2 = new Surtidor();
        Surtidor surtidor3 = new Surtidor();

        Estacion estacion = Estacion.getInstance();
        estacion.agregarSurtidor(surtidor1);
        estacion.agregarSurtidor(surtidor2);
        estacion.agregarSurtidor(surtidor3);
        surtidor1.extraerGasoil(5000);
        surtidor1.extraerPremium(3000);
        surtidor1.extraerSuper(2000);
        surtidor2.extraerGasoil(7000);
        surtidor2.extraerPremium(4000);
        surtidor2.extraerSuper(1000);
        surtidor3.extraerGasoil(6000);
        surtidor3.extraerPremium(2000);
        surtidor3.extraerSuper(3000);
        System.out.println("Cantidad total de litros vendidos: " + estacion.historicoTotalVendido());
        System.out.println("Cantidad de surtidores: " + estacion.getCantidadSurtidores());
        System.out.println("Cantidad total de litros vendidos de Gasoil: " + estacion.getCantGasoil());
        System.out.println("Cantidad total de litros vendidos de Premium: " + estacion.getCantPremium());
        System.out.println("Cantidad total de litros vendidos de Super: " + estacion.getCantSuper());
        Surtidor mayorGasoil = estacion.mayorVentaGasoil();
        if (mayorGasoil != null) {
            System.out.println("Surtidor con mayor venta de Gasoil: " + mayorGasoil );
        } else {
            System.out.println("No hay surtidores.");
        }
        Surtidor mayorPremium = estacion.mayorVentaPremium();
        if (mayorPremium != null) {
            System.out.println("Surtidor con mayor venta de Premium: " + mayorPremium);
        } else {
            System.out.println("No hay surtidores.");
        }
        Surtidor mayorSuper = estacion.mayorVentaSuper();
        if (mayorSuper != null) {
            System.out.println("Surtidor con mayor venta de Super: " + mayorSuper);
        } else {
            System.out.println("No hay surtidores.");
        }
    }
}
