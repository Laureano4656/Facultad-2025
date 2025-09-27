package PiedraPapelTijera_con_double_dispatch;

import java.util.Arrays;
import java.util.List;

public class GameCoordinator
{
    private static final List<PiedraPapelTijera> OBJECTS = Arrays.asList( new Piedra(), new Papel(), new Tijera() );

    public static void main(String[] args)
    {
        for ( PiedraPapelTijera player1 : OBJECTS)
            for (PiedraPapelTijera player2 : OBJECTS)
                System.out.println( player1 + " versus " + player2 + " = " + player1.versus(player2) + " <-- prestar atención al resultado");
    }
}
