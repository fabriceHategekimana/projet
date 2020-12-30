Observer
=========

Behavioral pattern

## Définition
l'Observer pattern est utilisé quand il y a beaucoup de dépendance entre les objet (si un objet change, tout les autres doivent changer). Les classes dépenantes vont devenir les observers et une classe (ici Subject) sera chargée de mettre à jour les autres.
![observer_design_patterns](../../images/observer_design_patterns.png)

## Composition:
## Point clé:
Chaque classe observer va prendre le sujet dans son constructeur et va ajouter son addresse dans la liste des observer du sujet. L'observer et le Subject se pointent l'un et l'autre


## Exemple:
## Définitions	
| classe              | rôle     | description                     |
|---------------------|----------|---------------------------------|
| HexaObserver        | Observer | Calcule selon l'état du système |
| OctalObserver       | Observer | Calcule selon l'état du système |
| BinaryObserver      | Observer | Calcule selon l'état du système |
| Observer            | type     | Définit le type des observers   |
| Subject             | State    | Définit l'état du système       |
| ObserverPatternDemo | Client   | classe principale               |

## Pseudocode
main()
  On crée un nouveau sujet.
  On crée successivement des observateur Hexa, Octa et Binaire (Ils dépendent tous du sujet)

  On change l'état du sujet (on lui ajoute 15)
  On change l'état du sujet (on lui ajoute 10)

## Code
```java
//Use Subject and concrete observer objects.
public class ObserverPatternDemo {
   public static void main(String[] args) {
      Subject subject = new Subject();

      new HexaObserver(subject);
      new OctalObserver(subject);
      new BinaryObserver(subject);

      System.out.println("First state change: 15");	
      subject.setState(15);
      System.out.println("Second state change: 10");	
      subject.setState(10);
   }
}

//Create Subject class.
public class Subject {
	
   private List<Observer> observers = new ArrayList<Observer>();
   private int state;

   public int getState() {
      return state;
   }

   public void setState(int state) {
      this.state = state;
      notifyAllObservers();
   }

   public void attach(Observer observer){
      observers.add(observer);		
   }

   public void notifyAllObservers(){
      for (Observer observer : observers) {
         observer.update();
      }
   } 	
}


//Create Observer class.
public abstract class Observer {
   protected Subject subject;
   public abstract void update();
}


//Create concrete observer classes
public class BinaryObserver extends Observer{

   public BinaryObserver(Subject subject){
      this.subject = subject;
      this.subject.attach(this);
   }

   @Override
   public void update() {
      System.out.println( "Binary String: " + Integer.toBinaryString( subject.getState() ) ); 
   }
}


public class OctalObserver extends Observer{

   public OctalObserver(Subject subject){
      this.subject = subject;
      this.subject.attach(this);
   }

   @Override
   public void update() {
     System.out.println( "Octal String: " + Integer.toOctalString( subject.getState() ) ); 
   }
}

public class HexaObserver extends Observer{

   public HexaObserver(Subject subject){
      this.subject = subject;
      this.subject.attach(this);
   }

   @Override
   public void update() {
      System.out.println( "Hex String: " + Integer.toHexString( subject.getState() ).toUpperCase() ); 
   }
}
```
