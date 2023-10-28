if __name__ == '__main__':
  def ques(a):
    questionSet = ["Capital City?", "National Bird?", "National Animal?", "Prime Minister?", "Sabse Bada Chutiya?"]
    return (questionSet[a])
  prize=10
  def checkAns(b):
    answerSet = ["delhi", "peacock", "tiger", "modi", "elvish"]
    return (answerSet[b])
    
  name = input("Welcome to KBC! Enter your name ")
  print("Hello ", name, "Input 1 to start game")
  k=int(input())
  if(k==1):
    for i in range(5):
      print("give answer to question ", i+1)
      print(ques(i))
      temp=str(input("Your Answer? "))
      if(temp==checkAns(i)):
        prize=prize*10
        print("Correct! Your prize now is ", prize, "\n")
      else:
        prize=prize/10
        print("Incorrect! ", prize, "\n")
    print("Your final prize is ", prize, "!!!", "\n")         
  else:
    print("Byeee!")
  print("Thanks")  