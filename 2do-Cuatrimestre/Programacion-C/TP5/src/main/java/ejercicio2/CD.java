package ejercicio2;

import java.util.ArrayList;

public class CD extends Producto implements Prestable,Comparable<CD>{
    private String interprete;
    private ArrayList<String> canciones;
    private boolean isPrestado;

    public CD(int codigo, String titulo, int anioPublicacion, String interprete) {
        super(codigo, titulo, anioPublicacion);
        this.interprete = interprete;
        this.canciones = new ArrayList<>();
        this.isPrestado = false;
    }

    public String getInterprete() {
        return interprete;
    }

    public void setInterprete(String interprete) {
        this.interprete = interprete;
    }

    public ArrayList<String> getCanciones() {
        return canciones;
    }

    public void setCanciones(ArrayList<String> canciones) {
        this.canciones = canciones;
    }

    public void addCancion(String cancion) {
        this.canciones.add(cancion);
    }

    @Override
    public boolean isPrestado() {
        return isPrestado;
    }

    @Override
    public void prestar() {
        if (this.isPrestado()) {
            System.out.println("El CD ya está prestado.");
        } else {
            this.isPrestado = true;
        }
        System.out.println("El CD ha sido prestado.");
    }
    @Override
    public void devolver() {
        if (this.isPrestado()) {
            this.isPrestado = false;
            System.out.println("El CD ha sido devuelto.");
        } else {
            System.out.println("El CD no estaba prestado.");
        }
    }
    @Override
    public int compareTo(CD o){
        assert o != null: "No se puede comparar con un objeto nulo";
        if (this.interprete.compareTo(o.interprete) == 0) {
            return this.getTitulo().compareTo(o.getTitulo());
        } else {
            return this.interprete.compareTo(o.interprete);
        }
    }
}
