import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

import ch.unige.cui.rpg.Character;
import ch.unige.cui.rpg.Damage;
import ch.unige.cui.rpg.Protection;
import ch.unige.cui.rpg.ProtectionStack;
import ch.unige.cui.rpg.Quest;
import ch.unige.cui.rpg.Armure;
import ch.unige.cui.rpg.Bag;
import ch.unige.cui.rpg.Potion;
import ch.unige.cui.rpg.Sword;

public class Game{
	public static void main(String[] args){
		//Exercice 1
		try{ 
				Path p= Paths.get("fichier.txt");
				List<String> data= Files.readAllLines(p);
				String name= data.get(0).split(" ")[1];
				int maxHP= Integer.parseInt(data.get(1).split(" ")[1]);
				String type= data.get(2).split(" ")[1]; 
				int bpp= Integer.parseInt(data.get(3).split(" ")[1]);
				int bmp= Integer.parseInt(data.get(4).split(" ")[1]);

				Damage p1= new Damage();
				Damage p2= new Damage();
				p1.setDamage("physique", bpp);
				p2.setDamage("magique", bmp);
				Armure a1= new Armure(type, 5, p1);
				Armure a2= new Armure(type, 5, p2);
				Protection[] pro= {a1,a2};
				ProtectionStack ps= new ProtectionStack(pro);

				Character Lancelot = new Character(name, maxHP, ps);
		}
		catch(Exception e){ 
			e.printStackTrace();
		}

		//Exercice 2
		Potion p= new Potion("Soin", "+20 HP", 4);
		Damage swordDamage= new Damage();
		swordDamage.setDamage("physique", 4);
		Sword s= new Sword(swordDamage, 2);
		Bag sacDAventurier= new Bag(25);

		sacDAventurier.putEquipment(p);
		sacDAventurier.putEquipment(s);
		sacDAventurier.putMoney(70);
			
	}
}

