# Contantes

COMMANDS = {'SALIR': [1, 0], 'DESCRIBIR': [2, 0], 'UNION': [3, 1], 'STRUCT': [3, 1], 'ATOMICO': [4, 0]}
MODE = ['Sin Empaquetar', 'Empaquetando', 'Óptimo']


# Cálculo del mínimo común múltiplo
def mcm(nums: [int]) -> int | None:
    if len(nums) == 0:
        return

    def mcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    res = nums[0]
    for num in nums[1:]:
        res = res * num // mcd(res, num)

    return res


# Verifica si la instrucción ingresada en la consola es permitida para este programa
def is_command_valid(command: [str]) -> bool:
    if command[0] not in COMMANDS:
        return False

    constrain = COMMANDS[command[0]][1]
    size = COMMANDS[command[0]][0]
    if (constrain == 0 and size != len(command)) or (constrain == 1 and size > len(command)):
        return False

    return True


# Clase que maneja el contenido de un tipo de dato
class Type:
    def __init__(self, name, aln, rep=None):
        if rep is None:
            rep = [0, 0, 0]  # unpacked packed, optimal
        self.name = name
        self.aln = aln
        self.rep = rep

    def show(self, idx: int):
        mode = MODE[idx]
        wst = self.rep[idx] - self.rep[1]
        print(f' => {mode} ocupa {self.rep[idx]} bytes, alineado a {self.aln} bytes y con {wst} bytes de desperdicio')


# Clase que maneja el contenido del administrador de tipos
class TypeManager:
    def __init__(self):
        self.types = {}

    # Calcula la el espacio que ocupa un registro sin empaquetar
    def rep_unpacked(self, types: [str]) -> int:
        r = 0
        for t in types:
            diff = r % self.types[t].aln
            r += self.types[t].rep[0] if diff == 0 else self.types[t].aln - diff + self.types[t].rep[0]

        return r

    # Calcula la el espacio que ocupa un registro empaquetado
    def rep_packed(self, types: [str]) -> int:
        return sum([self.types[t].rep[1] for t in types])

    # Calcula la el espacio que ocupa un registro guardado de forma óptima
    def rep_optimal(self, types: [str]) -> int:
        r = 0
        for t in sorted(types, key=lambda e: self.types[e].aln, reverse=True):
            diff = r % self.types[t].aln
            r += self.types[t].rep[2] if diff == 0 else self.types[t].aln - diff + self.types[t].rep[2]

        return r

    # Muestra el contenido del tipo en los 3 modos de guardado
    def describe(self, name: str):
        if name not in self.types:
            print(f"El tipo {name} no está definido")
            return

        print(f'Descripción del tipo "{name}"')
        self.types[name].show(0)
        self.types[name].show(1)
        self.types[name].show(2)

    # Crea un nuevo tipo atómico
    def atomic(self, name: str, aln: int, rep: int):
        if name in self.types:
            print(f"El tipo {name} ya está definido")
            return

        self.types[name] = Type(name, aln, [rep] * 3)

    # Crea un nuevo registro
    def struct(self, name: str, types: [str]):
        if name in self.types:
            print(f"El tipo {name} ya está definido")
            return

        for t in types:
            if t not in self.types:
                print(f"El tipo {name} no está definido")
                return

        aln = max([self.types[t].aln for t in types])
        rep = [self.rep_unpacked(types), self.rep_packed(types), self.rep_optimal(types)]
        self.types[name] = Type(name, aln, rep)

    # Crea un nuevo registro variable
    def union(self, name: str, types: [int]):
        if name in self.types:
            print(f"El tipo {name} ya está definido")
            return

        for t in types:
            if t not in self.types:
                print(f"El tipo {name} no está definido")
                return

        aln = mcm([self.types[t].aln for t in types])
        rep = max([self.types[t].rep for t in types])
        self.types[name] = Type(name, aln, rep)


if __name__ == '__main__':
    type_manager = TypeManager()

    # type_manager.atomic("bool", 2, 1)
    # type_manager.atomic("char", 2, 2)
    # type_manager.atomic("int", 4, 4)
    # type_manager.atomic("double", 8, 8)
    # type_manager.struct("meta", ["int", "char", "int", "double", "bool"])
    # type_manager.struct("meta2", ["meta", "meta"])
    # type_manager.union("meta3", ["int", "char", "int", "double", "bool"])
    # type_manager.struct("meta4", ["meta", "meta2", "meta3"])
    # type_manager.describe("meta")
    # type_manager.describe("meta2")
    # type_manager.describe("meta3")
    # type_manager.describe("meta4")

    # Inicio del cliente
    while True:
        cmd = input()
        if len(cmd) == 0:
            continue

        cmd = cmd.split(' ')
        if not is_command_valid(cmd):
            print("Instrucción desconocida")
            continue

        match cmd[0]:
            case "SALIR":
                break
            case "DESCRIBIR":
                type_manager.describe(cmd[1])
            case "UNION":
                type_manager.union(cmd[1], cmd[2::])
            case "STRUCT":
                type_manager.struct(cmd[1], cmd[2::])
            case "ATOMICO":
                try:
                    type_manager.atomic(cmd[1], int(cmd[3]), int(cmd[2]))
                except ValueError:
                    print("Error: No se pudo convertir el contenido a entero.")



