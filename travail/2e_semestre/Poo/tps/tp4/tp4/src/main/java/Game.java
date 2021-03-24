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

public class Game{
	public static void main(String[] args){
		//Character Lancelot = new Character("Lancelot", 20, 7);
		//Damage p1= new Damage();
		//p1.setDamage("feu", 1);
		//p1.setDamage("physique", 4);
		//CotteDeMaille cdm= new CotteDeMaille(5, p1);
		//VesteEnCuir vec= new VesteEnCuir(2, p2);
		//Protection[] pro= {cdm,vec};
		//ProtectionStack ps= new ProtectionStack(pro);
		//ps.absorb(d);
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
	}
}

