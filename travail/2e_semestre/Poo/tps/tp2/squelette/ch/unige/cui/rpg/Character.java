package ch.unige.cui.rpg;

public class Character{
    private String name;
    private int gold;
    private int maxHP;
    private int currentHP;
    private int armor;
    private Quest currentQuest;

    public Character(){ 
    }

    public Character(String name, int maxHP, int armor){ 
	this.name= name;
    	this.maxHP= maxHP;
	this.armor= armor;
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
}
