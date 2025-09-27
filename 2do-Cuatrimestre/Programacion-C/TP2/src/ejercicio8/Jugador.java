package ejercicio8;

public class Jugador {
    private String nombre;
    private String anioNacimiento;
    private int numeroDeCamiseta;
    private int posicion;
    private int golesAnotados;
    private int partidosJugados;

    public Jugador(String nombre, String anioNacimiento, int numeroDeCamiseta, int posicion) {
        this.nombre = nombre;
        this.anioNacimiento = anioNacimiento;
        this.numeroDeCamiseta = numeroDeCamiseta;
        this.posicion = posicion;
        this.golesAnotados = 0;
        this.partidosJugados = 0;
    }

    public int promedioGolesPorPartido() {
        if (this.partidosJugados == 0) {
            return 0;
        }
        return this.golesAnotados / this.partidosJugados;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getAnioNacimiento() {
        return anioNacimiento;
    }

    public void setAnioNacimiento(String anioNacimiento) {
        this.anioNacimiento = anioNacimiento;
    }

    public int getNumeroDeCamiseta() {
        return numeroDeCamiseta;
    }

    public void setNumeroDeCamiseta(int numeroDeCamiseta) {
        this.numeroDeCamiseta = numeroDeCamiseta;
    }

    public int getPosicion() {
        return posicion;
    }

    public void setPosicion(int posicion) {
        this.posicion = posicion;
    }

    public int getGolesAnotados() {
        return golesAnotados;
    }

    public void setGolesAnotados(int golesAnotados) {
        this.golesAnotados = golesAnotados;
    }

    public int getPartidosJugados() {
        return partidosJugados;
    }

    public void setPartidosJugados(int partidosJugados) {
        this.partidosJugados = partidosJugados;
    }

    @Override
    public String toString() {
        return "Jugador{" +
                "nombre='" + nombre + '\'' +
                ", anioNacimiento='" + anioNacimiento + '\'' +
                ", numeroDeCamiseta=" + numeroDeCamiseta +
                ", posicion=" + posicion +
                ", golesAnotados=" + golesAnotados +
                ", partidosJugados=" + partidosJugados +
                '}';
    }
}
