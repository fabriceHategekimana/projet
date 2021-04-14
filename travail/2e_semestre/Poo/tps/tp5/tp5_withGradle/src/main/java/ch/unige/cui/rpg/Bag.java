package ch.unige.cui.rpg;

import java.util.Stack;

public class Bag{
	private int capacity;
	private int goldPocket;
	private Stack<Equipment> mainPocket;

	public Bag(int capacity){
		this.capacity= capacity;
		mainPocket= new Stack<Equipment>();
	}	

	public int takeMoney(int value){ 
		if(this.goldPocket > value){
			this.goldPocket -= value;
			return value;
		}		
		else{ 
			return 0;
		}
	}

	public void putMoney(int value){ 
		if(value > -1){
			this.goldPocket += value;	
		}
	}

	public int putEquipment(Equipment e){ 
		if(this.capacity >= e.getWeight()){
			this.mainPocket.push(e);
			this.capacity -= e.getWeight();
			return 0;
		}
		else{ 
			System.out.println("Il n'y a plus assez de place dans le sac...");	
			return 1;
		}
	}

	public Equipment getEquipment(){ 
		Equipment e= this.mainPocket.pop();
		this.capacity += e.getWeight();
		return e;
	}

}
