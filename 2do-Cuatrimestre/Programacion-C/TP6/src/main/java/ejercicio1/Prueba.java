package ejercicio1;

public class Prueba {
    public static void main(String[] args) {
        Usuario usuario = new Usuario("Juan", "abc123");

        try {
            usuario.setNombre("");
        } catch (ejercicio1.exceptions.NombreInvalidoException e) {
            String nombre = e.getNombre();
            if (nombre == null) {
                System.out.println("El nombre no puede ser null");
            } else if (nombre.trim().isEmpty()) {
                System.out.println("El nombre no puede estar vacio");
            } else {
                System.out.println(e.getMessage());
            }
        }

        try {
            usuario.setContrasenia("123");
        } catch (ejercicio1.exceptions.ContrasenaInvalidaException e) {
            String contrasenia = e.getContrasenia();
            if (contrasenia == null) {
                System.out.println("La contrase��a no puede ser null");
            } else if (contrasenia.length() < 6) {
                System.out.println("La contrase��a debe tener al menos 6 caracteres");
            } else if (contrasenia.trim().isEmpty()) {
                System.out.println("La contrase��a no puede estar vacia");
            } else if (!Character.isLetter(contrasenia.charAt(0))) {
                System.out.println("La contrase��a debe comenzar con una letra");
            } else {
                System.out.println(e.getMessage());
            }
        }

        try {
            usuario.setContrasenia("1abcde");
        } catch (ejercicio1.exceptions.ContrasenaInvalidaException e) {
            if (!Character.isLetter(e.getContrasenia().charAt(0))) {
                System.out.println("La contrase��a debe comenzar con una letra");
            } else {
                System.out.println(e.getMessage());
            }
        }

        try {
            usuario.setContrasenia("abcdef");
            System.out.println("Contrase��a cambiada exitosamente a: " + usuario.getContrasenia());
        } catch (ejercicio1.exceptions.ContrasenaInvalidaException e) {
            if (!Character.isLetter(e.getContrasenia().charAt(0))) {
                System.out.println("La contrase��a debe comenzar con una letra");
            } else {
                System.out.println(e.getMessage());
            }
        }
    }
}
