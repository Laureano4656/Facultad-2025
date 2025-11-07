package Ejercicio1.persistencia;

import Ejercicio1.modelo.Cliente;
import Ejercicio1.modelo.Mascota;

import java.util.ArrayList;

public interface IPersistencia
{
    ArrayList<ClienteDTO> getClientes();
    void insertarMascota();
    void insertarCliente();
    void insertarPracticaVeterinaria();
    ArrayList<MascotaDTO> getMascotasCliente(ClienteDTO c);
    void getPracticasVeterinarias(MascotaDTO m);
    void getMascotasPorTipo(String tipo);
    void getMascota(String historiaClinica);
}
