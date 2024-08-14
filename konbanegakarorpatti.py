import random as ran


print("##################### Kon Banega Karorpati #######################\n\n\n")
easyquestions=("""Which of these is not a work of William Shakespeare?
A) Macbeth
B) Othello
C) War and Peaces
D) Romeo and Juliet""","""What is the capital of India?
A) Mumbai
B) Kolkata
C) New Delhi
D) Chennai""","""Who is known as the Father of the Nation in India?
A) Jawaharlal Nehru
B) Mahatma Gandhi
C) Subhas Chandra Bose
D) Sardar Vallabhbhai Patel""","""Which is the largest planet in our solar system?
A) Earth
B) Mars
C) Jupiter
D) Saturn""","""Which of these festivals is known as the "Festival of Lights"?
A) Holi
B) Diwali
C) Eid
D) Christmas""","""In which year did India gain independence?
A) 1945
B) 1947
C) 1950
D) 1952""","""Which of these is a traditional Indian garment?
A) Kimono
B) Sari
C) Toga
D) Kilt""","""Who wrote the Indian national anthem "Jana Gana Mana"?
A) Rabindranath Tagore
B) Bankim Chandra Chatterjee
C) Sarojini Naidu
D) Lata Mangeshkar""","""Which river is the longest in India?
A) Ganga
B) Yamuna
C) Brahmaputra
D) Godavari""","""Which sport is associated with the term "googly"?
A) Football
B) Hockey
C) Tennis
D) Cricket""")

hardlevel=("""Who was the first Indian to win an individual Olympic gold medal?

A) Leander Paes
B) Abhinav Bindra
C) Milkha Singh
D) P.T. Usha""","""Which Mughal emperor built the Taj Mahal?
A) Akbar
B) Jahangir
C) Shah Jahan
D) Aurangzeb""","""In which language was the ancient Indian epic "Ramayana" originally written?
A) Hindi
B) Sanskrit
C) Tamil
D) Pali""","""Which is the smallest state in India by area?
A) Goa
B) Sikkim
C) Tripura
D) Manipur""","""Who was the first woman to receive the Bharat Ratna?
A) Mother Teresa
B) Indira Gandhi
C) Lata Mangeshkar
D) Sarojini Naidu""","""Which Indian scientist won the Nobel Prize in Physics in 1930?
A) C.V. Raman
B) Homi Bhabha
C) Vikram Sarabhai
D) Satyendra Nath Bose""","""Which Indian cricketer was known as the "Little Master"?
A) Sunil Gavaskar
B) Sachin Tendulkar
C) Kapil Dev
D) Rahul Dravid""")



E_answers=("War and Peace","New Delhi","Mahatma Gandhi","Jupiter","Diwali","1947","Sari","Rabindranath Tagore","Ganga","Cricket")

h_answers=("Abhinav Bindra","Shah Jahan","Sanskrit","Goa","Indira Gandhi","C.V. Raman","Sunil Gavaskar")

n=20
n=40
E_amount=0
H_amount=0
easyscore=0
hardscore=0
random_item=ran.sample(list(zip(easyquestions,E_answers)),k=len(easyquestions))
print("####### ROUND 1 ##########")
for question, correct_answers in random_item:
    print(question)
    ans=input("Enter your answer: ")
    if ans.strip().lower()==correct_answers.lower():
        print("\n Correct Answer!")
        easyscore+=10
        E_amount+=1
        print(f"\nScore: {easyscore}")
        print(f"Amount Won: {E_amount}L\n")
    else:
        print('Wrong Answer!')
        print(f"\nScore: {easyscore}")
        print(f"Amount Won: {E_amount}L\n")

if easyscore>=70:
    print("####### ROUND 2 ##########")
    random_item=ran.sample(list(zip(hardlevel,h_answers)),k=len(hardlevel))
    for question,c_answer in random_item:
        print(question)
        ans=input("Emter your answer: ")
        if ans.strip().lower()==c_answer.lower():
            print("\n Correct Answer!")
            H_amount+=1
            hardscore+=10
           
            print(f"\n Score: {hardscore}")
            print(f"Amount Won: {H_amount}L\n")
        else:
            print('Wrong Answer!')
            print(f"\nScore: {easyscore}")
            print(f"Amount Won: {H_amount}L\n")
            
            
else:
    print("You are not going to the next round!\n")


totalscore=easyscore+hardscore
Total_amount=H_amount+E_amount
print(f"\nTotal Score: {totalscore}")
print(f"Total Amount Won: {Total_amount}\n")

        



