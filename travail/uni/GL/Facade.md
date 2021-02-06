Facade
=======

### Structural Pattern

![facade_design_pattern](images/facade_design_pattern.png)
![Facade_meme](images/Facade_meme.jpeg)

## Définition
**Problème:** On a un système (ou une structure) super complexe et on aimerait que le Client puisse intéragir facilement avec.  
**Solution:** On crée une facade qui va prendre les instructions du clients et manipuler le système.
"On cache la complexité d'un système et son interaction"
Crée une interface de haut niveau pour rendre l'utilisation d'un système complexe plus facile. Ici on a plusieurs formes et on cherche un moyen de les créer simplement. C'est comme la face avant d'une construction. 

## Composition:
- Facade: Interface qui recevra les demandes du client et executera les Component nécessaire
- ConcreteFacade: exécutera concrètement les commandes.
- Component: Objets divers qui seront appellé par la ConcreteFacade
  
## Exemple:
Ici, on utilisera pas d'interface mais une classe ConcreteFacade facade (=ShapeMaker) qui va manipuler les différentes formes selon les orderes qu'on lui donnera.

## Définitions	
| classe            | rôle           | description                       |
|-------------------|----------------|-----------------------------------|
| ShapeMaker        | ConcreteFacade | Facilite l'utilisation des formes |
| Shape             | type           | interface                         |
| Rectangle         | Component      | type de Shape                     |
| Circle            | Component      | type de Shape                     |
| Square            | Component      | type de Shape                     |
| FacadePatternDemo | Client         | classe principale                 |

## Pseudo code
```
main()
  Créer un ShapeMaker
  Créer des formes (cercle, rectangle, carré) avec le ShapeMaker
```

## Code
```java

//Use the facade to draw various types of shapes.
//FacadePatternDemo.java
public class FacadePatternDemo {
   public static void main(String[] args) {
      ShapeMaker shapeMaker = new ShapeMaker();

      shapeMaker.drawCircle();
      shapeMaker.drawRectangle();
      shapeMaker.drawSquare();		
   }
}

//Create an interface.
//Shape.java
public interface Shape {
   void draw();
}

//Create concrete classes implementing the same interface.
//Rectangle.java
public class Rectangle implements Shape {

   @Override
   public void draw() {
      System.out.println("Rectangle::draw()");
   }
}

//Square.java
public class Square implements Shape {

   @Override
   public void draw() {
      System.out.println("Square::draw()");
   }
}

//Circle.java
public class Circle implements Shape {

   @Override
   public void draw() {
      System.out.println("Circle::draw()");
   }
}

//Create a facade class.
//ShapeMaker.java
public class ShapeMaker {
   private Shape circle;
   private Shape rectangle;
   private Shape square;

   public ShapeMaker() {
      circle = new Circle();
      rectangle = new Rectangle();
      square = new Square();
   }

   public void drawCircle(){
      circle.draw();
   }
   public void drawRectangle(){
      rectangle.draw();
   }
   public void drawSquare(){
      square.draw();
   }
}

```
