/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {

    if (numRows == 1) { 
        return [[1]]
    }
    if (numRows == 2) {
        return [[1],[1,1]]
    }
    let rows = [numRows]
    rows[0] = [1]
    rows[1] = [1,1]


    for (let i = 2 ; i < numRows ; i++) {
        let newRow = [i + 1]
        for (let j = 0; j < rows[i-1].length ; j++) {
            if (j == 0) {
                newRow[j] = rows[i-1][j]
            }
            else 
            {
                newRow[j] = rows[i-1][j] + rows[i-1][j-1]
            }
            if (j == rows[i-1].length - 1) {
                newRow[j+1] = rows[i-1][j]
            }
        }
        rows[i] = newRow
    }
    return rows
};

console.log(generate(5))