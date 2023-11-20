import bTree.*

@main
def main(): Unit = {
  val arbol = Branch(10, Branch(5, Leaf(3), Leaf(4)), Branch(7, Leaf(6), Leaf(2)))
  println(isSymmetricMaxHeap(arbol))
}