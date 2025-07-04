"""
Programa demostrativo de Programación Orientada a Objetos (POO)
---------------------------------------------------------------
Conceptos cubiertos:
- Definición de clase
- Creación de objetos
- Encapsulación
- Herencia
- Polimorfismo
"""

from abc import ABC, abstractmethod   # para la clase base abstracta

class Empleado(ABC):
    """
    Clase base (abstracta) que representa a cualquier empleado.
    Demuestra ENCAPSULACIÓN mediante el atributo _salario (protegido).
    """

    def __init__(self, nombre: str, salario_base: float) -> None:
        self.nombre = nombre             # atributo público
        self._salario = salario_base     # atributo protegido (convención: 1 guion bajo)

    # Getter y setter (encapsulan el acceso al salario)
    @property
    def salario(self) -> float:
        """Devuelve el salario actual (lectura controlada)."""
        return self._salario

    @salario.setter
    def salario(self, nuevo_salario: float) -> None:
        """Actualiza el salario con validación básica."""
        if nuevo_salario < 0:
            raise ValueError("El salario no puede ser negativo.")
        self._salario = nuevo_salario

    @abstractmethod
    def calcular_salario(self) -> float:
        """
        Método abstracto: *obliga* a las subclases a proporcionar su
        propia lógica de cálculo de salario ➜ POLIMORFISMO.
        """
        pass

    def __str__(self) -> str:
        """Representación legible del objeto."""
        return f"{self.__class__.__name__}({self.nombre}, ${self.calcular_salario():,.2f})"


class Desarrollador(Empleado):
    """
    Subclase que hereda de Empleado.
    - Aporta atributo propio: lenguaje.
    - Sobrescribe calcular_salario() (polimorfismo por overriding).
    """

    def __init__(self, nombre: str, salario_base: float, lenguaje: str) -> None:
        super().__init__(nombre, salario_base)
        self.lenguaje = lenguaje

    def calcular_salario(self) -> float:
        """
        Salario = base + bono por lenguaje “premium”.
        Se muestra POLIMORFISMO: cada clase concreta define su versión.
        """
        bonus = 0.15 * self._salario if self.lenguaje.lower() in {"python", "rust"} else 0
        return self._salario + bonus


class Gerente(Empleado):
    """
    Otra subclase. Demuestra HERENCIA y POLIMORFISMO.
    Tiene un atributo adicional: número de personas a cargo.
    """

    def __init__(self, nombre: str, salario_base: float, equipo: int) -> None:
        super().__init__(nombre, salario_base)
        self.equipo = equipo

    def calcular_salario(self) -> float:
        """
        Salario = base + bono fijo por persona supervisada.
        """
        bono_equipo = 200 * self.equipo
        return self._salario + bono_equipo


def total_nomina(empleados: list[Empleado]) -> float:
    """
    Función independiente que recibe *cualquier* lista de objetos Empleado
    (o subclases) y llama a calcular_salario().
    🔥 Esto demuestra POLIMORFISMO “en acción”: la función no necesita
    saber el tipo exacto de cada objeto.
    """
    return sum(emp.calcular_salario() for emp in empleados)


# ----------------- DEMOSTRACIÓN EN CONSOLA ------------------ #
if __name__ == "__main__":
    # Creación de objetos (instancias)
    dev1 = Desarrollador("Ana", 1200, "Python")
    dev2 = Desarrollador("Luis", 1000, "JavaScript")
    gerente = Gerente("María", 2000, equipo=5)

    # Uso de métodos y encapsulación
    print(dev1)          # __str__
    print(dev2)
    print(gerente)

    # Acceso controlado al salario
    dev2.salario = 1100  # setter invocado

    # Cálculo de la nómina total (polimorfismo)
    empleados = [dev1, dev2, gerente]
    print(f"TOTAL NÓMINA: ${total_nomina(empleados):,.2f}")
