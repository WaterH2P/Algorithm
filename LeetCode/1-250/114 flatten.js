
// Definition for a binary tree node.
function TreeNode(val, left, right) {
  this.val = (val === undefined ? 0 : val)
  this.left = (left === undefined ? null : left)
  this.right = (right === undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @return {void} Do not return anything, modify root in-place instead.
 */
var flatten = function(root) {
  if (!root || (!root.left && !root.right)) { return root; }

  function preorder(node = new TreeNode()) {
    if (node.left) {
      let nodeR = node.right;
      node.right = node.left;
      node.left = null;
      let last = preorder(node.right);
      if (nodeR) {
        last.right = nodeR;
        return preorder(nodeR);
      } else { return last; }
    }
    else if (node.right) { return preorder(node.right); }
    else { return node; }
  }
  preorder(root);
};