/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {

    if (n <= 3) { 
        return n
    }
    let table = [n+1];
    table [0] = 0;
    table [1] = 1;
    table [2] = 2;
    for (let i = 3 ; i <= n ; i++) {
        table[i] = table [i-1] + table[i-2]
    }
    return table[n]
};

console.log(climbStairs(4))