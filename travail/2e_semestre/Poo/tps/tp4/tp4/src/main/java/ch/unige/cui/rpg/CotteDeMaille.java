package ch.unige.cui.rpg;

public class CotteDeMaille implements Protection{
	private int cWeight;
	private Damage protection;

	public CotteDeMaille(int weight, Damage dmg){
		this.cWeight= weight;
		this.protection = dmg;
	}	

	public int weight(){ 
		return cWeight;
	}

	public Damage absorb(Damage dmg){ 
		dmg.reduceDamage(protection);
		return dmg;
	}
}
