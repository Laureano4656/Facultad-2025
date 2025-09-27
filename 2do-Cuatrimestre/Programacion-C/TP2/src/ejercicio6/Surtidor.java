package ejercicio6;

public class Surtidor {
    private int cantGasoil;
    private int cantPremium;
    private int cantSuper;
    private int gasoilVendido;
    private int premiumVendido;
    private int superVendido;
    private static int maximaCarga = 20000;

    public Surtidor(){
        this.cantGasoil = maximaCarga;
        this.cantPremium = maximaCarga;
        this.cantSuper = maximaCarga;
        this.gasoilVendido = 0;
        this.premiumVendido = 0;
        this.superVendido = 0;
    }
    boolean extraerGasoil(int litros){
        if (litros <= this.cantGasoil){
            this.cantGasoil -= litros;
            this.gasoilVendido += litros;
            return true;
        }else{
            this.gasoilVendido += this.cantGasoil;
            this.cantGasoil = 0;
            return false;
        }
    }
    boolean extraerPremium(int litros){
        if (litros <= this.cantPremium){
            this.cantPremium -= litros;
            this.premiumVendido += litros;
            return true;
        }else{
            this.premiumVendido += this.cantPremium;
            this.cantPremium =0;
            return false;
        }
    }
    boolean extraerSuper(int litros){
        if (litros <= this.cantSuper){
            this.cantSuper -= litros;
            this.superVendido += litros;
            return true;
        }else{
            this.superVendido += this.cantSuper;
            this.cantSuper =0;
            return false;
        }
    }
    public int getGasoilVendido() {
        return gasoilVendido;
    }
    public int getPremiumVendido() {
        return premiumVendido;
    }
    public int getSuperVendido() {
        return superVendido;
    }
    void llenarDepositoGasoil(){
        this.cantGasoil = maximaCarga;
    }
    void llenarDepositoPremium(){
        this.cantPremium = maximaCarga;
    }
    void llenarDepositoSuper(){
        this.cantSuper = maximaCarga;
    }
    public int getCantGasoil() {
        return cantGasoil;
    }
    public int getCantPremium() {
        return cantPremium;
    }
    public int getCantSuper() {
        return cantSuper;
    }
    public static int getMaximaCarga() {
        return maximaCarga;
    }

    @Override
    public String toString() {
        return "Surtidor{" +
                "cantGasoil=" + cantGasoil +
                ", cantPremium=" + cantPremium +
                ", cantSuper=" + cantSuper +
                ", gasoilVendido=" + gasoilVendido +
                ", premiumVendido=" + premiumVendido +
                ", superVendido=" + superVendido +
                '}';
    }
}
