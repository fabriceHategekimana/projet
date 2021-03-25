import ch.unige.cui.rpg.*;
import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;
//@TestInstance(TestInstance.Lifecycle.PER_METHOD);

class RPGTest {


    @Test
    void bagCapacity(){
        System.out.println("Test the bag's capacity");
        
        Bag b= new Bag(1);
		Potion p= new Potion("soin", "+10 HP", 3);
        
        assertEquals(1,p.putEquipment(p));
    }

    @Test
    void bagGoldPocket(){
        System.out.println("Test if the bag's gold pocket is always positive");
        
        Bag b= new Bag(1);
        
        assertEquals(1,b.putMoney(-5));
    }



}
