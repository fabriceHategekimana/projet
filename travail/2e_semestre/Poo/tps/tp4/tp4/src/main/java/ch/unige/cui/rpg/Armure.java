package ch.unige.cui.rpg;

public class Armure implements Protection{
	private String name;
	private int cWeight;
	private Damage protection;

	public Armure(String name, int weight, Damage dmg){
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
