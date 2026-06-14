from qiskit import QuantumCircuit
from qiskit_aer import Aer
import string

def password_generator(length):

    password = ""
    for i in range(length):

        qc = QuantumCircuit(8,8)

        for j in range(8):
            qc.h(j)
        qc.measure(range(8), range(8))
        backend = Aer.get_backend("qasm_simulator")
        result = backend.run(qc, shots=1).result()
        counts = result.get_counts()
        binary = list(counts.keys())[0]

        number = int(binary, 2)

        characters = string.ascii_letters + string.digits

        index = number % len(characters)

        character = characters[index]

        password += character

    return password
