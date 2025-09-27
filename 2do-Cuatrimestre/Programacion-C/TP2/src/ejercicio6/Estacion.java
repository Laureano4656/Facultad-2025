package ejercicio6;

import java.util.ArrayList;

public class Estacion {
    private static Estacion _instance = null;
    private ArrayList<Surtidor> surtidores;

    private Estacion() {
        this.surtidores = new ArrayList<Surtidor>();
    }

    public int getCantidadSurtidores() {
        return this.surtidores.size();
    }
    public int getCantPremium(){
        int total = 0;
        for (Surtidor s : this.surtidores) {
            total += s.getCantPremium();
        }
        return total;
    }
    public int getCantSuper(){
        int total = 0;
        for (Surtidor s : this.surtidores) {
            total += s.getCantSuper();
        }
        return total;
    }
    public int getCantGasoil(){
        int total = 0;
        for (Surtidor s : this.surtidores) {
            total += s.getCantGasoil();
        }
        return total;
    }
    public Surtidor mayorVentaGasoil(){
        Surtidor mayor = null;
        int max = -1;
        for (Surtidor s : this.surtidores) {
            if (s.getGasoilVendido() > max){
                max = s.getGasoilVendido();
                mayor = s;
            }
        }
        return mayor;
    }
    public Surtidor mayorVentaPremium(){
        Surtidor mayor = null;
        int max = -1;
        for (Surtidor s : this.surtidores) {
            if (s.getPremiumVendido() > max){
                max = s.getPremiumVendido();
                mayor = s;
            }
        }
        return mayor;
    }
    public Surtidor mayorVentaSuper(){
        Surtidor mayor = null;
        int max = -1;
        for (Surtidor s : this.surtidores) {
            if (s.getSuperVendido() > max){
                max = s.getSuperVendido();
                mayor = s;
            }
        }
        return mayor;
    }
    int hisotricoGasoilVendido(){
        int total = 0;
        for (Surtidor s : this.surtidores) {
            total += s.getGasoilVendido();
        }
        return total;
    }
    int hisotricoPremiumVendido(){
        int total = 0;
        for (Surtidor s : this.surtidores) {
            total += s.getPremiumVendido();
        }
        return total;
    }
    int hisotricoSuperVendido(){
        int total = 0;
        for (Surtidor s : this.surtidores) {
            total += s.getSuperVendido();
        }
        return total;
    }
    int historicoTotalVendido(){
        return this.hisotricoGasoilVendido() + this.hisotricoPremiumVendido() + this.hisotricoSuperVendido();
    }
    public void agregarSurtidor(Surtidor s) {
        this.surtidores.add(s);
    }

    public static Estacion getInstance() {
        if (_instance == null) {
            _instance = new Estacion();
        }
        return _instance;
    }
}
