function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

function dfs(tree, length) {
    if (tree == null) return length
    length++
    return Math.max(dfs(tree.left,length), dfs(tree.right,length))
}

var maxDepth = function(root) {
    if (root.length <= 1) return root.length
    if (root.length <= 3) return 2

    let t = new TreeNode(root[0],root[1],root[2]);
    let nodePointer = 1;
    let leafPointer = 3;
    console.log(t.val + " LEFT " + t.left)
    console.log(t.val + " RIGHT " + t.right)
    while (leafPointer < root.length) {
        root[nodePointer].left = root[leafPointer]
        console.log(root[nodePointer] + " LEFT " + root[leafPointer])
        leafPointer++;
        root[nodePointer].right = root[leafPointer]
        console.log(root[nodePointer] + " RIGHT " + root[leafPointer])
        nodePointer++;
        leafPointer++;
    }
    
    return dfs(t,1)
};



let root = [3,9,20,null,null,15,7]


console.log(maxDepth(root))