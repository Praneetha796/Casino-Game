from qiskit import QuantumCircuit
from qiskit_aer import Aer
import streamlit as st
def guessing_game():
    qc=QuantumCircuit(4,4)
    for i in range(4):
      qc.h(i)
    qc.measure(range(4), range(4))
    backend=Aer.get_backend("qasm_simulator")
    result=backend.run(qc,shots=1).result()
    counts=result.get_counts()
    binary=list(counts.keys())[0]
    number=int(binary, 2)
    return (number % 10) + 1
   