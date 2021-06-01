# Resume-Scanner
<p align="center">
<a href=""><img title="Flutter" src="https://img.shields.io/badge/Python3-3-yellow?style=for-the-badge&logo=python"></a>
<a href=""><img title="License" src="https://img.shields.io/badge/License-Open Source-brightgreen?style=for-the-badge&logo="></a>
</p>

# WHAT IS RESUME SCANNER? 


**The main objective of this Resume Scanner is to analyse the Resume of the student and comparing it with the company's requirments**
It was completely built on **Python**. The steps involved in Scanning the resume are explained below: 

- First the student needs to upload their Resume and the Resume which is in a **PDF** format is being converted into a **txt** file. 
- Now the text file is being scanned and the **keywords** from the file are being extracted. **key_phrases.py** analyses the whole file and 
  the important keywords are seperated out. Now the key words are given a Polarity value based on which the student is examined. 
- The Student's qualification is now being compared with the Company's **requirment**. If the student's qualification meets the comany's
  requirments the person is taken to a **CHATBOT** of the institution or company. **chat.py** is a scalable lightweighted chat which is 
  used to act as a medium between the company and the student. The Chat Bot is an interactive bot which provides information about the company
  and informs the student about the interview and other information. 
 - A mail is automatically sent to the student regarding the performance and tells the candidate if the person is eligble to attend an 
 interview or not. 
 - **automail.py** is a simple mail sending software developed in python which is used to send mails automatically to the respective candidate.
 
 # WHERE CAN RESUME SCANNER BE USED? 
 
 Resume Scanner can be used by an Educational Instituions or Companies. This software automates the process of Job hiring. 
 
 In colleges this can be used in a larger scale since it would be easier for the Placement Cell to assign each student's to the right company. 
 
# TOOLS
- Python
- html css js
- Flask
