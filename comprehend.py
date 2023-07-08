import tkinter as tk 
import boto3 

root= tk.Tk()
root.geometry("400x240")
root.title("Sentiment Analysis")
textExample=tk.Text(root,height=10)
textExample.pack()
def getText():
    aws_mag_con=boto3.session.Session(profile_name="demo_user")
    client=aws_mag_con.client(service_name='comprehend',region_name="us-east-1")
    result=textExample.get("1.0","end")
    print(result)
    response = client.detect_sentiment(Text=result,LanguageCode='en')
    print('The prominant sentiment is:',response['Sentiment'])
    print('The SentimentScore is:',response['SentimentScore'])
    #response = client.detect_key_phrases(Text=result,LanguageCode='en')
    #for ph in response['KeyPhrases']:
    #    print(ph['Text'])
    #response = client.detect_syntax(Text=result,LanguageCode='en')
    #print(response)
btnRead=tk.Button(root,height=1,width=10,text="Read",command=getText)
btnRead.pack()
root.mainloop()