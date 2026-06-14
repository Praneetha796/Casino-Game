
from qiskit import QuantumCircuit
from qiskit_aer import Aer
def lottery():

    lottery_numbers = []

    while len(lottery_numbers) < 6:

        qc = QuantumCircuit(6,6)

        for i in range(6):
            qc.h(i)

        qc.measure(range(6), range(6))

        backend = Aer.get_backend("qasm_simulator")

        result = backend.run(qc, shots=1).result()

        counts = result.get_counts()

        binary = list(counts.keys())[0]

        number = int(binary, 2)

        lottery = (number % 49) + 1

        if lottery not in lottery_numbers:
            lottery_numbers.append(lottery)

    return lottery_numbers
  