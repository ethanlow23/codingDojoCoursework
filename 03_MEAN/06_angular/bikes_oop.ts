class Bike {
    constructor(
        public price: number,
        public max_speed: number,
    ){}
    displayInfo(){
        console.log('price: ' + this.price + ', max speed: ' + this.max_speed + ', miles: ' + this.miles);
        return this;
    }
    ride(){
        console.log('riding...');
        this.miles += 10;
        return this;
    }
    reverse(){
        console.log('reversing...');
        this.miles -= 10;
        return this;
    }
}
const bike1 = new Bike(500, 20);
const bike2 = new Bike(450, 18);
const bike3 = new Bike(550, 25);

bike1.ride().ride().ride().reverse().reverse().displayInfo();
bike2.ride().ride().reverse().reverse().displayInfo();
bike3.reverse().reverse().reverse().displayInfo();