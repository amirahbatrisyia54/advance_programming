import smtplib

# This part will open both fileSS
with open('Student_grades_Communication.csv','r') as firstfile, open('Student_grades_Communication(final).csv','w') as secondfile:
	
# read content from first file
	for line in firstfile:
			
# append content to second file
		secondfile.write(line)

#coding for sent notification to email
content = ("Hi, Want to tell you that the data from Students's Grade for Communication was succesfully update")
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('amirahbatrisyia70@gmail.com','wwqmkphegeqmaksx')
mail.sendmail('amirahbatrisyia70@gmail.com','maathirah@graduate.utm.my',content) 
mail.close()
#notify that the email was succesfully sent
print("copy data process was successful and notification was sent to email")
