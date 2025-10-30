package Ejercicio1;

public class Via {
    private int trenesEnVia = 0;
    private int direccionActualEnVia = 0;
    private int esperandoTramo1 = 0;
    private int esperandoTramo2 = 0;
    private int turno = 1; // <-- NUEVO: Empieza el turno el tramo 1

    // --- Métodos de consulta (Getters) ---
    public int getTrenesEnVia() { return trenesEnVia; }
    public int getDireccionActualEnVia() { return direccionActualEnVia; }
    public int getTurno() { return turno; }

    // NUEVO: Método para simplificar la lógica en el monitor
    public boolean hayAlguienEsperandoEn(int direccion) {
        if (direccion == 1) return esperandoTramo1 > 0;
        return esperandoTramo2 > 0;
    }

    // --- Métodos de modificación (Setters) ---
    public void registrarTrenEntrando(int direccion) {
        this.trenesEnVia++;
        this.direccionActualEnVia = direccion;
    }

    public void registrarTrenSaliendo(int direccionQueSale) {
        this.trenesEnVia--;
        if (this.trenesEnVia == 0) {
            this.direccionActualEnVia = 0;
            // NUEVO: Cede el turno a la otra dirección
            this.turno = (direccionQueSale == 1) ? 2 : 1;
        }
    }

    public void agregarTrenEnEspera(int direccion) {
        if (direccion == 1) this.esperandoTramo1++; else this.esperandoTramo2++;
    }

    public void quitarTrenDeEspera(int direccion) {
        if (direccion == 1) this.esperandoTramo1--; else this.esperandoTramo2--;
    }
}