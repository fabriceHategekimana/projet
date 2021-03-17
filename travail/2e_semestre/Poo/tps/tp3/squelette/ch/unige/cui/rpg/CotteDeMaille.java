package ch.unige.cui.rpg;

public class CotteDeMaille implements Protection{
	private int cWeight;
	private Damage protection;

	public CotteDeMaille(weight, Damage dmg){
		this.cWeight= wheight;
		this.protection = dmg;
	}	

	public static weight(){ 
		return cWeight;
	}

	public Damage absorb(Damage dmg){ 
		dmg.reduceDamage(protection);
		return dmg;
	}
}
