package ejercicio8;

public class Posicion {
    private int x;
    private int y;

    public Posicion(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public void setXY(int x) {
        this.x = x;
        this.y = y;
    }
    public void incrementaPosicion(double dx, double dy) {
        this.x += dx;
        this.y += dy;
    }
    public double distancia(Posicion pos) {
        return Math.sqrt(Math.pow(this.x - pos.x, 2) + Math.pow(this.y - pos.y, 2));
    }

    @Override
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}
