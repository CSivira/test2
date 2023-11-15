package church

import church.*

@main
def main(): Unit = {

  def toInt(n: Church): Int = n.get((x: Int) => x + 1)(0)
  
  val zero = Cero
  val one = suc(zero)
  val two = suc(one)
  val three = suc(two)
  val four = suc(three)
  val five = suc(four)

  println(toInt(zero))
  println(toInt(one))
  println(toInt(two))

  // suc tests
  println(toInt(suc(zero)))
  println(toInt(suc(four)))

  // Sum tests
  println(toInt(sum(one, one)))
  println(toInt(sum(two, three)))

  // Mul tests
  println(toInt(mul(one, two)))
  println(toInt(mul(two, two)))
}