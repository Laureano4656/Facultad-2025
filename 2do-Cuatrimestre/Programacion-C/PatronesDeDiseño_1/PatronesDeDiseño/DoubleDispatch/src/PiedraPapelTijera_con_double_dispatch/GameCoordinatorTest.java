package PiedraPapelTijera_con_double_dispatch;

import org.junit.Test;

public class GameCoordinatorTest
{
    private static final PiedraPapelTijera ROCK = new Piedra();
    private static final PiedraPapelTijera PAPER = new Papel();
    private static final PiedraPapelTijera SCISSORS = new Tijera();

    @Test
    public void test()
    {
        assert( ! ROCK.versus( ROCK ) );
        assert( ! ROCK.versus( PAPER ) );
        assert(   ROCK.versus( SCISSORS ) );

        assert(   PAPER.versus( ROCK ) );
        assert( ! PAPER.versus( PAPER ) );
        assert( ! PAPER.versus( SCISSORS ) );

        assert( ! SCISSORS.versus( ROCK ) );
        assert(   SCISSORS.versus( PAPER ) );
        assert( ! SCISSORS.versus( SCISSORS ) );
    }
}
