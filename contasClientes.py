from contas import Conta
from clientes import Clientes
cliente1 = Clientes(12365478900, "João", "Rua 1")
cliente2 = Clientes(32145698755, "Maria", "Rua 2")
cliente1 = Conta([cliente1, cliente2], 1, 0) (1)
conta1.geraSaldo()
conta1.depositar(1500)
conta1.sacar()
conta1.geraSaldo()
