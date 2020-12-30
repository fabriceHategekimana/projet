Template Method
===============

Behavioral Pattern

![Template_design_pattern](../../images/Template_design_pattern.png)

## Définition
Crée une "une recette", un algorithme que vont suivre toute les classes qui l'implémente.

## Composition:
## Exemple:

## Définitions	
| classe                      | rôle     | description             |
|-----------------------------|----------|-------------------------|
| TemplateMethodPatternClient | Main     | classe principale       |
| OrderProcessTemplate        | Template | Définit l'algorithme    |
| StoreOrder                  | Objet    | Implémente l'algorithme |
| NetOrder                    | Objet    | Implémente l'algorithme |

## Pseudocode
main() 
    On crée un NetOrder et on applique la méthode processOrder()
    On crée un StoreOrder et on applique la méthode processOrder()

## Code
```java
class TemplateMethodPatternClient 
{ 
	public static void main(String[] args) 
	{ 
		OrderProcessTemplate netOrder = new NetOrder(); 
		netOrder.processOrder(true); 
		System.out.println(); 
		OrderProcessTemplate storeOrder = new StoreOrder(); 
		storeOrder.processOrder(true); 
	} 
} 

bstract class OrderProcessTemplate 
{ 
	public boolean isGift; 

	public abstract void doSelect(); 

	public abstract void doPayment(); 

	public final void giftWrap() 
	{ 
		try
		{ 
			System.out.println("Gift wrap successful"); 
		} 
		catch (Exception e) 
		{ 
			System.out.println("Gift wrap unsuccessful"); 
		} 
	} 

	public abstract void doDelivery(); 

	public final void processOrder(boolean isGift) 
	{ 
		doSelect(); 
		doPayment(); 
		if (isGift) { 
			giftWrap(); 
		} 
		doDelivery(); 
	} 
} 


class NetOrder extends OrderProcessTemplate 
{ 
	@Override
	public void doSelect() 
	{ 
		System.out.println("Item added to online shopping cart"); 
		System.out.println("Get gift wrap preference"); 
		System.out.println("Get delivery address."); 
	} 

	@Override
	public void doPayment() 
	{ 
		System.out.println 
				("Online Payment through Netbanking, card or Paytm"); 
	} 

	@Override
	public void doDelivery() 
	{ 
		System.out.println 
					("Ship the item through post to delivery address"); 
	} 

} 

class StoreOrder extends OrderProcessTemplate 
{ 

	@Override
	public void doSelect() 
	{ 
		System.out.println("Customer chooses the item from shelf."); 
	} 

	@Override
	public void doPayment() 
	{ 
		System.out.println("Pays at counter through cash/POS"); 
	} 

	@Override
	public void doDelivery() 
	{ 
		System.out.println("Item delivered to in delivery counter."); 
	} 

} 

class TemplateMethodPatternClient 
{ 
	public static void main(String[] args) 
	{ 
		OrderProcessTemplate netOrder = new NetOrder(); 
		netOrder.processOrder(true); 
		System.out.println(); 
		OrderProcessTemplate storeOrder = new StoreOrder(); 
		storeOrder.processOrder(true); 
	} 
} 
```
