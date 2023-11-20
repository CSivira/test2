package bTree

sealed trait BTree
case class Branch(value: Int, l: BTree, r: BTree) extends BTree
case class Leaf(value: Int) extends BTree

def isMaxHeap(tree: BTree): Boolean = tree match {
  case Leaf(_) => true
  case Branch(value, l: Leaf, r: Leaf) => value >= l.value && value >= r.value
  case Branch(value, l: Branch, r: Leaf) => value >= l.value && value >= r.value && isMaxHeap(l)
  case Branch(value, l: Leaf, r: Branch) => value >= l.value && value >= r.value && isMaxHeap(r)
  case Branch(value, l: Branch, r: Branch) => value >= l.value && value >= r.value && isMaxHeap(l) && isMaxHeap(r)
}

def preOrderList(tree: BTree): List[Int] = tree match {
  case Leaf(value) => List(value)
  case Branch(value, l, r) => value :: preOrderList(l) ::: preOrderList(r)
}

def postOrderList(tree: BTree): List[Int] = tree match {
  case Leaf(value) => List(value)
  case Branch(value, l, r) => postOrderList(r) ::: postOrderList(l) ::: List(value)
}

def isSymmetricMaxHeap(tree: BTree): Boolean = {
  isMaxHeap(tree) && preOrderList(tree) == postOrderList(tree).reverse
}
