import java.util.HashMap;

public class DefaultDict<K, V> extends HashMap<K, V>{

    private final Class<V> cls;

    public DefaultDict(Class factory){
        this.cls = factory;
    }


    @Override
    public V get(Object key) {

        V value = super.get(key);

        if (value == null){
            try {
                value = cls.getDeclaredConstructor().newInstance();
            } catch (Exception e) {
                e.printStackTrace();
            }

            this.put((K) key, value);
        }

        return value;
    }

}
