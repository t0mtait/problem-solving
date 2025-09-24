function longestCommonPrefix(strs: string[]): string {
    let ans: string = ""
    let it: number = 0
    if (strs.length == 0 || strs[0].length == 0) return ans
    let l : number = strs[0].length
    for (let elem of strs) {
        if (elem.length < l ) l = elem.length
    }
    while (it < l) {
        let prefix: string = ''
        for (let elem of strs) {
            if (prefix == '') { 
                prefix = elem[it]
            }
            else {
                if (prefix != elem[it]) {
                    return ans
                }
            }
        }
        it++
        ans += prefix
    }
    return ans
};


let input : string[] = ["flower","flower","flower", "flower"]

console.log(longestCommonPrefix(input))