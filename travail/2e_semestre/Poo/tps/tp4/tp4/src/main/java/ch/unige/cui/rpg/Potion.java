package ch.unige.cui.rpg;

public class Potion implements Equipement{
	private String name;
	private String effect;
	private int usage;
	private int weight;

	public Potion(String name, String effect, int usage) {
		this.name = name;
		this.effect = effect;
		this.usage = usage;
	}

	public String use(){ 
		usage--;
		return effect;
	}

	public String getName() {
		return name;
	}

	public String getEffect() {
		return effect;
	}

	public int getUsage() {
		return usage;
	}

	public void setUsage(int usage) {
		this.usage = usage;
	}

	public int weight(){ 
		return this.weight;	
	}
}
