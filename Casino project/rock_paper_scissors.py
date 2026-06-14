from qiskit import QuantumCircuit
from qiskit_aer import Aer
import streamlit as st
def rock_paper_scissors():
  user_score=0
  computer_score=0
  for i in range(3):
    qc=QuantumCircuit(2,2)
    qc.h(0)
    qc.h(1)
    qc.measure([0,1],[0,1])
    backend=Aer.get_backend("qasm_simulator")
    result=backend.run(qc,shots=1).result()
    counts=result.get_counts()
    binary=list(counts.keys())[0]
    st.write("Binary:", binary)
    if binary=="00":
      return "Rock"
    elif binary=="01":
      return "Paper"
    elif binary=="10":
       return "Scissors"
    elif binary=="11":
       return "Rock"
    
      #   user=st.write("Enter your choice:")
  #   if user==computer:
  #     st.write("Draw")
  #   elif user=="Rock"and computer=="Scissors":
  #     st.success("User Win")
  #     user_score += 1
  #   elif user=="Scissors" and computer=="Paper":
  #     st.success("User Win")
  #   elif user=="Paper" and computer=="Rock":
  #     st.success("User Win")
  #   else:
  #     st.success("computer Wins")
  #     computer_score += 1
  # st.write("\n===== FINAL SCORE =====")
  # st.write("User Score:", user_score)
  # st.write("Computer Score:", computer_score)

  # if user_score > computer_score:
  #       return "You won the game!"

  # elif computer_score > user_score:
  #       return "Computer won the game!"

  # else:
  #       return "Game Draw!"
