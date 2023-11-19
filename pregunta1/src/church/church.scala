// Reference: https://en.wikipedia.org/wiki/Church_encoding
package church

trait Church {
  def get[A]: (A => A) => A => A
}

case object Cero extends Church {
  def get[A]: (A => A) => A => A = f => x => x
}

def suc(n: Church): Church = {
  new Church {
    def get[A]: (A => A) => A => A = f => x => f(n.get(f)(x))
  }
}

def sum(m: Church, n: Church): Church = {
  new Church {
    def get[A]: (A => A) => A => A = f => x => m.get(f)(n.get(f)(x))
  }
}

def mul(m: Church, n: Church): Church = {
  new Church {
    def get[A]: (A => A) => A => A = f => x => m.get(n.get(f))(x)
  }
}