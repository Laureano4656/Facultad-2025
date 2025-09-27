package ejercicio2;

public class Libro extends Producto implements Prestable{
    private boolean isPrestado;

    public Libro(int codigo, String titulo, int anioPublicacion) {
        super(codigo, titulo, anioPublicacion);
        this.isPrestado = false;
    }
    @Override
    public boolean isPrestado() {
        return isPrestado;
    }
    @Override
    public void prestar(){
        if(this.isPrestado()){
            System.out.println("El libro ya está prestado.");
        } else {
            this.isPrestado = true;
            System.out.println("El libro ha sido prestado.");
        }
    }
    @Override
    public void devolver() {
        if (this.isPrestado()) {
            this.isPrestado = false;
            System.out.println("El libro ha sido devuelto.");
        } else {
            System.out.println("El libro no estaba prestado.");
        }
    }
}
