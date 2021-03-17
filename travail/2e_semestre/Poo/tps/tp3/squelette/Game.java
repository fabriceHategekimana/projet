import ch.unige.cui.rpg.Character;
import ch.unige.cui.rpg.Quest;
import ch.unige.cui.rpg.Damage;

public class Game{
	public static void main(String[] args){
		Character Lancelot = new Character("Lancelot", 20, 7);
		Character chevalier0= new Character("A", 20, 7);
		Character chevalier1= new Character("B", 20, 7);
		Character chevalier2= new Character("C", 20, 7);

		Damage d= new Damage();
		d.setDamage("feu", 2);
		d.setDamage("physique", 6);

		System.out.println(d.toString());
	}
}

