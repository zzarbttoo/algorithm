package temp;

public class Child extends Parent{

    String tal;

    public Child(){
        System.out.println("child");
    }

    public Child(String tal){
        System.out.println("hello child2");
        this.tal = tal;
    }

    @Override
    public void helloWorld() {
        System.out.println("hello Child");
    }
}
