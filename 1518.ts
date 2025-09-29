function numWaterBottles(numBottles: number, numExchange: number): number {
    let drank:number = 0
    let newBottles:number;
    while (numBottles >= numExchange) {
        drank += numBottles
        newBottles = Math.floor(numBottles/numExchange) + numBottles % numExchange
        drank -= numBottles % numExchange
        numBottles = newBottles
    }
    return drank += numBottles
}

let numBottles = 15, numExchange = 4
console.log(numWaterBottles(numBottles,numExchange))





// There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.
// The operation of drinking a full water bottle turns it into an empty bottle.
// Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.