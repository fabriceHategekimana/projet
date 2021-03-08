import ch.unige.cui.rpg.Character;
import ch.unige.cui.rpg.Quest;

public class Game{
	public static void main(String[] args){
		Character Lancelot = new Character("Lancelot", 20, 7);
		Lancelot.test1();
		Character chevalier0= new Character("A", 20, 7);
		Character chevalier1= new Character("B", 20, 7);
		Character chevalier2= new Character("C", 20, 7);
	
		System.out.println("État du chevalier A");
		System.out.println(chevalier0.toString());

		System.out.println("le chevalier A prend 5 de dégat!");
		chevalier0.wound(5);

		System.out.println("État du chevalier A");
		System.out.println(chevalier0.toString());

		Quest q0= new Quest("Pourfendre un dragon", 2000);
		System.out.println("Le chevalier B commence une nouvelle quête");
		chevalier1.startQuest(q0);

	}
}
