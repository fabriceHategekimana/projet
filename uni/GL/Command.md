Command
========

### Behavioral pattern

![Command_design_pattern](images/Command_design_pattern.png){ width=75% }
![Command_meme](images/Command_meme.jpeg){ width=120% }

## Définition
**Problème:** On veut pouvoir géré une liste de commandes/actions sur des objets. On pourra lancer/annuler les commandes quand on veut.
**Solution:** On crée une interface Command. Pour chaque objet, on créer des ConcreteCommands. On utilise un Invoker qui les liste et les exécute.
Permet de créer une liste de commande listable ou annulable.

## Composition:
- Client: Crée des commande pour des reciever 
- Invoker: Stock est exécute les commandes
- Command: Interface qui défini comment manipuler les commandes
- ConcreteCommande: Implémente Command et seront exécuté par l'Invoker
- Reciever: Sont les objets contrôlés par les commandes.

## Exemple:
On a un Broker (=Courtier, une personne qui gère les transactions financières) qui doit gérer des stocks.
Pour ce faire on a des commandes (orders) pour l'achat et la vente de stock. Le broker peut prendre les commandes et les exécuter à tout moment.

## Définitions	
| classe             | rôle             | description           |
|--------------------|------------------|-----------------------|
| Broker             | Invoker          | execute les commandes |
| SellStock          | Concrete Command | vente pour les stocks |
| BuyStock           | Concrete Command | achat pour les stocks |
| Stock              | Reciever         | Stocks à vendre       |
| CommandPatternDemo | main             | classe Principale     |
| OrderReciever      | Command          | Interface             |

## Pseudocode
main()
  Création d'un nouveau stock
  Création d'une commande d'achat et une commande de vente pour le store
  Création d'un Broker
  Le Broker prend les commandes
  Le Broker exécute les commandes

## Code
```java
public class CommandPatternDemo {
   public static void main(String[] args) {
      Stock abcStock = new Stock();

      BuyStock buyStockOrder = new BuyStock(abcStock);
      SellStock sellStockOrder = new SellStock(abcStock);

      Broker broker = new Broker();
      broker.takeOrder(buyStockOrder);
      broker.takeOrder(sellStockOrder);

      broker.placeOrders();
   }
}
public interface Order {
   void execute();
}

public class Stock {
	
   private String name = "ABC";
   private int quantity = 10;

   public void buy(){
      System.out.println("Stock [ Name: "+name+", Quantity: " + quantity +" ] bought");
   }
   public void sell(){
      System.out.println("Stock [ Name: "+name+", Quantity: " + quantity +" ] sold");
   }
}

public class BuyStock implements Order {
   private Stock abcStock;

   public BuyStock(Stock abcStock){
      this.abcStock = abcStock;
   }

   public void execute() {
      abcStock.buy();
   }
}


public class SellStock implements Order {
   private Stock abcStock;

   public SellStock(Stock abcStock){
      this.abcStock = abcStock;
   }

   public void execute() {
      abcStock.sell();
   }
}

import java.util.ArrayList;
import java.util.List;

   public class Broker {
   private List<Order> orderList = new ArrayList<Order>(); 

   public void takeOrder(Order order){
      orderList.add(order);		
   }

   public void placeOrders(){
   
      for (Order order : orderList) {
         order.execute();
      }
      orderList.clear();
   }
}

```
