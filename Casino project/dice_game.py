from qiskit import QuantumCircuit
from qiskit_aer import Aer
def dice_game():
  qc=QuantumCircuit(6,6)
  for i in range(6):
    qc.h(i)
  qc.measure(range(6), range(6))
  backend=Aer.get_backend("qasm_simulator")
  result=backend.run(qc,shots=1).result()
  counts=result.get_counts()
  binary=list(counts.keys())[0]
  number=int(binary, 2)
  dicevalue=(number % 6) + 1
  return dicevalue
