import ch.unige.cui.rpg.Character;
import ch.unige.cui.rpg.Quest;
import ch.unige.cui.rpg.Damage;
import ch.unige.cui.rpg.CotteDeMaille;
import ch.unige.cui.rpg.VesteEnCuir;
import ch.unige.cui.rpg.ProtectionStack;
import ch.unige.cui.rpg.Protection;

public class Game{
	public static void main(String[] args){
		Character Lancelot = new Character("Lancelot", 20, 7);
		Character chevalier0= new Character("A", 20, 7);
		Character chevalier1= new Character("B", 20, 7);
		Character chevalier2= new Character("C", 20, 7);

		//Définition de l'armure1
		Damage p1= new Damage();
		p1.setDamage("feu", 1);
		p1.setDamage("physique", 4);

		CotteDeMaille cdm= new CotteDeMaille(5, p1);

		//Définition de l'armure2
		Damage p2= new Damage();
		p2.setDamage("électrique", 2);
		p2.setDamage("physique", 1);

		VesteEnCuir vec= new VesteEnCuir(2, p2);
		
		//Définition de dégat
		Damage d= new Damage();
		d.setDamage("feu", 10);
		d.setDamage("électrique", 10);
		d.setDamage("magique", 10);
		d.setDamage("physique", 10);

		Protection[] pro= {cdm,vec};

		ProtectionStack ps= new ProtectionStack(pro);

		//Teste sur les dégats
		ps.absorb(d);

		System.out.println(d.toString());
	}
}

