package ch.unige.cui.rpg;

public class Mage{
  private int mana;
  private int currentMana;
  
  public Mage(String name, int maxHP, int gold, ProtectionStack protectionSt, Bag bag){
	  super(name, maxHP, gold, protectionSt, bag);
	  this.mana= mana;
	  this.currentMana= mana;
  }
  
  public void wound(Damage dmg){
	  super.wound(dmg);
  }
  
  public void heal(int hp){
	 super.heal(hp);
  }
  
  public void startQuest(Quest q){
	 super.startQuest(q);
  }
  
  public String toString(){
	  return super.toString();
  }
  
}
