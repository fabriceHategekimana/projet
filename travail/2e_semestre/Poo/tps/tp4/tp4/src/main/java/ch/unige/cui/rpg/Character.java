package ch.unige.cui.rpg;

public class Character{
    private String name;
    private int gold;
    private int maxHP;
    private int currentHP;
    private int armor;
	private ProtectionStack ps;
    private Quest currentQuest;

    public Character(){ 
    }

    public Character(String name, int maxHP, ProtectionStack ps){ 
	this.name= name;
    	this.maxHP= maxHP;
    	this.currentHP= maxHP;
		this.ps= ps;
		this.gold= 0;
    }

    public void wound(int damage){ 
   	this.currentHP -= damage; 
    }

    public void heal(int hp){ 
   	this.currentHP += hp; 
    }

    public void startQuest(Quest q){ 
   	this.currentQuest= q; 
    }

	public void test1(){
		System.out.println("test1");
	}

	@Override
	public String toString() {
	    return "---------------------------" +
		"\n name = " + name +
		"\n gold = " + gold +
		"\n maxHP = " + maxHP +
		"\n currentHP = " + currentHP +
		"\n armor = " + armor +
		"\n currentQuest = " + currentQuest +
		"\n---------------------------";
	}

}
