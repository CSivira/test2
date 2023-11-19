package tree

trait Tree
case class Leaf (t : Tree) extends Tree
case class Branch(l : Tree, r : Tree) extends Tree

def isSimetricHeap(implicit ord: Ordering[A]): Boolean = {
  def preOrder(tree: Tree): List[A] = tree match {
    case Leaf(v) => List(v)
    case Branch(v, l, r) => v :: preOrder(l) ::: preOrder(r)
  }

  def postOrder(tree: Tree): List[A] = tree match {
    case Leaf(v) => List(v)
    case Branch(v, l, r) => postOrder(l) ::: postOrder(r) ::: List(v)
  }

  def isHeap(tree: Tree): Boolean = tree match {
    case Leaf(_) => true
    case Branch(v, l: Leaf[A], r: Leaf[A]) => ord.gteq(v, l.value) && ord.gteq(v, r.value)
    case Branch(v, l: Branch[A], r: Branch[A]) => ord.gteq(v, l.value) && ord.gteq(v, r.value) && isHeap(l) && isHeap(r)
    case _ => false
  }

  preOrder(tree) == postOrder(tree).reverse && isHeap(tree)
}
