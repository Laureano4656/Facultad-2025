package ejercicio5;

public class Categoria {
    String nombreCategoria;
    double sueldo;
    boolean habilitaColectivoLinea;
    boolean habilitaColectivoLarga;
    boolean habilitaCamion;

    public Categoria(String nombreCategoria, double sueldo, boolean habilitaColectivoLinea, boolean habilitaColectivoLarga, boolean habilitaCamion) {
        this.nombreCategoria = nombreCategoria;
        this.sueldo = sueldo;
        this.habilitaColectivoLinea = habilitaColectivoLinea;
        this.habilitaColectivoLarga = habilitaColectivoLarga;
        this.habilitaCamion = habilitaCamion;
    }

    public boolean getHabilitaColectivoLinea() {
        return habilitaColectivoLinea;
    }

    public boolean getHabilitaColectivoLarga() {
        return habilitaColectivoLarga;
    }

    public boolean getHabilitaCamion() {
        return habilitaCamion;
    }

    public double getSueldo() {
        return sueldo;
    }
    public String getNombreCategoria() {
        return nombreCategoria;
    }
}
