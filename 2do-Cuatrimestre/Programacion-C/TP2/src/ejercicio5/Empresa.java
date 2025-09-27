package ejercicio5;

import java.util.ArrayList;

public class Empresa {
    private static Empresa _instance = null;
    private String nombre;
    private ArrayList<Chofer> choferes = new ArrayList<Chofer>();
    private ArrayList<Colectivo> colectivos = new ArrayList<Colectivo>();

    public int cantidadChoferes() {
        return choferes.size();
    }
    public int cantidadColectivos() {
        return colectivos.size();
    }
    public int cantidadSinColectivo() {
        int contador = 0;
        for (Chofer chofer : choferes) {
            if (chofer.getColectivo() == null) {
                contador++;
            }
        }
        return contador;
    }
    public int cantCategoria(Categoria categoria) {
        int contador = 0;
        for (Chofer chofer : choferes) {
            if (chofer.getCategoria().equals(categoria)) {
                contador++;
            }
        }
        return contador;
    }
    public void categoriaMayorA(double sueldo) {
        for (Chofer chofer : choferes) {
            if (chofer.getCategoria().getSueldo() > sueldo) {
                System.out.println(chofer.getCategoria().getNombrecategoria());
            }
        }
    }
    public void sueldoMayorA(double sueldo) {
        for (Chofer chofer : choferes) {
            if (chofer.getCategoria().getSueldo() > sueldo) {
                System.out.println(chofer.getNombre() + " - " + chofer.getCategoria().getSueldo());
            }
        }
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public ArrayList<Chofer> getChoferes() {
        return choferes;
    }

    public void setChoferes(ArrayList<Chofer> choferes) {
        this.choferes = choferes;
    }

    public ArrayList<Colectivo> getColectivos() {
        return colectivos;
    }

    public void setColectivos(ArrayList<Colectivo> colectivos) {
        this.colectivos = colectivos;
    }

    public static Empresa getInstance(String nombre) {
        if (_instance == null) {
            _instance = new Empresa();
        }
        return _instance;
    }
    public String getNombre() {
        return nombre;
    }

}
