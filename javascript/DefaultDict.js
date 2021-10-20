
class MapWithDefault extends Map{
    get(key){
        if (!this.has(key)) this.set(key, this.default());
        return super.get(key);
    }

    constructor(defaultFunctions, entries){
        super(entries);
        this.default = defaultFunctions;
    }
}


const stringMap = new MapWithDefault(() => []);
console.log(stringMap.get('whatever'));

stringMap.get("whatever").push('javascript');
console.log(stringMap.get("whatever"));

const intMap = new MapWithDefault(() => []);
console.log(intMap.get(1));
intMap.get(1).push(2);
console.log(intMap.get(1));
