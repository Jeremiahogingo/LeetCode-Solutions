/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val === undefined ? 0 : val)
 *     this.left = (left === undefined ? null : left)
 *     this.right = (right === undefined ? null : right)
 * }
 */

/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function (p, q) {

    // Both nodes are null
    if (p === null && q === null) {
        return true;
    }

    // One node is null or values differ
    if (p === null || q === null || p.val !== q.val) {
        return false;
    }

    // Compare left and right subtrees
    return isSameTree(p.left, q.left) &&
           isSameTree(p.right, q.right);
};