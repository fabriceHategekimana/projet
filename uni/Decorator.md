Decorator
==========

Structural pattern

![Decorator_design_pattern](../../images/Decorator_design_pattern.png)

## Définition
Les décorateurs ajoute du nouveau contenu sans altéré la structure de l'objet qu'on modifie. Ils font une surcharge.

On peut ainsi wrapper la classe tout en gardant la signature de celle-ci.

Le decorator doit être une abstract class qui implémente l'interface en question.

## Composition:
## Exemple:
On crée une classe concrète qui étant le décorateur. Cela permet de pouvoir ajouter des fonctionnalité à un groupe d'interface sans en modifier l'interface principale.

## Définitions	
| classe               | rôle       | description    |
|----------------------|------------|----------------|
| Shape                | Type       | interface      |
| Circle               | Objet      | interface      |
| Rectangle            | Objet      | interface      |
| ShapeDecorator       | Decorator  | abstract class |
| RedShapeDecorator    | Coloration | concrete class |
| DecoratorPatternDemo | Main       | interface      |

## Pseudocode
main() 
      On crée un Shape Circle
      On crée un Shape redCircle avec RedShapeDecorator et le Circle
      On crée un Shape Rectangle
      On crée un Shape redRectangle avec RedShapeDecorator et le Rectangle
      On déssine les formes et leur version rouge avec la méthode draw

## Code
```java
public class DecoratorPatternDemo {
   public static void main(String[] args) {

      Shape circle = new Circle();

      Shape redCircle = new RedShapeDecorator(new Circle());

      Shape redRectangle = new RedShapeDecorator(new Rectangle());
      System.out.println("Circle with normal border");
      circle.draw();

      System.out.println("\nCircle of red border");
      redCircle.draw();

      System.out.println("\nRectangle of red border");
      redRectangle.draw();
   }
}

public interface Shape { 
   void draw();
   }

public class Rectangle implements Shape {

   @Override
   public void draw() {
      System.out.println("Shape: Rectangle");
   }
}

public class Circle implements Shape {

   @Override
   public void draw() {
      System.out.println("Shape: Circle");
   }
}


public abstract class ShapeDecorator implements Shape {
   protected Shape decoratedShape;

   public ShapeDecorator(Shape decoratedShape){
      this.decoratedShape = decoratedShape;
   }

   public void draw(){
      decoratedShape.draw();
   }	
}

public class RedShapeDecorator extends ShapeDecorator {

   public RedShapeDecorator(Shape decoratedShape) {
      super(decoratedShape);		
   }

   @Override
   public void draw() {
      decoratedShape.draw();	       
      setRedBorder(decoratedShape);
   }

   private void setRedBorder(Shape decoratedShape){
      System.out.println("Border Color: Red");
   }
}
```
