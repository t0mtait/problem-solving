/**
 * // Definition for a _Node.
 * function _Node(val,children) {
 *    this.val = val === undefined ? null : val;
 *    this.children = children === undefined ? null : children;
 * };
 */

/**
 * @param {_Node|null} root
 * @return {number}
 */
 
var maxDepth = function(root) {
    if (root == null) return 0
    let ans = 1
    if (root.children && root.children.length) {
        for (let child of root.children) {
            ans = Math.max(ans, 1 + maxDepth(child))
        }
    }

    return ans
};