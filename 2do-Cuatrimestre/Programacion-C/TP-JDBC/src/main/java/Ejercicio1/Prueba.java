package Ejercicio1;

import Ejercicio1.modelo.Cliente;
import Ejercicio1.persistencia.ClienteDTO;
import Ejercicio1.persistencia.DB;
import Ejercicio1.persistencia.IPersistencia;
import Ejercicio1.persistencia.MascotaDTO;

import java.sql.ResultSet;
import java.util.ArrayList;

public class Prueba
{
    public static void main(String[] args)
    {
        try
        {
            Class.forName("java.sql.Driver");
        } catch (ClassNotFoundException e)
        {
            e.printStackTrace();
        }
        try
        {
            IPersistencia db = new DB();

            ArrayList<ClienteDTO> clientes = db.getClientes();

            for (ClienteDTO c : clientes)
            {
                System.out.println("ID: " + c.getId());
                System.out.println("Nombre: " + c.getNombre());
                System.out.println("Direccion: " + c.getDireccion());
                System.out.println("Telefono: " + c.getTelefono());
                System.out.println("-----------------------");
            }
            ArrayList<MascotaDTO> mascotas = db.getMascotasCliente(clientes.get(0));

            for (MascotaDTO m : mascotas)
            {
                System.out.println("ID: " + m.getId());
                System.out.println("Nombre: " + m.getNombre());
                System.out.println("Animal: " + m.getAnimal());
                System.out.println("Fecha de Nacimiento: " + m.getFechaNacimiento().getTime());
                System.out.println("Historia Clinica: " + m.getHistoriaClinica());
                System.out.println("-----------------------");
            }

        } catch (Exception e)
        {
            System.out.println(e);
            System.exit(1);
        }
    }
}
