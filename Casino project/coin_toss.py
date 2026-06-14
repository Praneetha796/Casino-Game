import qiskit
from qiskit_aer import Aer  
from qiskit import QuantumCircuit
def coin_toss():
  qc=QuantumCircuit(1,1)
  qc.h(0)
  qc.measure(0,0)
  backend=Aer.get_backend("qasm_simulator")
  result=backend.run(qc).result()
  counts=result.get_counts()
  binary=list(counts.keys())[0]
  if binary=="0":
     return "Head"
  else:
    return "Tail"
 