# Kaun Banega Crorepati
import random

def rulesOfKBC():
    print("\nThe rules of KBC are as follows: -")
    print("1. There are 16 questions in the game")
    print("2. If you answer all questions correctly, then you win!!")
    print("3. There are 2 milestones in the game, 5th question worth 10,000 Rupees & 10th Question worth 3,20,000 Rupees")
    print("4. If the user has selected an incorrect option, the amount will be given according to milestone cleared.")
    print("5. If you quit at a particular question, then you will win the amount for the last question that you have answered.")
    print("6. The prize assigned for each question is a follows: -\n\t\tQuestion 1\tRs.1,000\n\t\tQuestion 2\tRs.2,000\n\t\tQuestion 3\tRs.3,000\n\t\tQuestion 4\tRs.5,000\n\t\tQuestion 5\tRs.10,000\n\t\tQuestion 6\tRs.20,000\n\t\tQuestion 7\tRs.40,000\n\t\tQuestion 8\tRs.80,000\n\t\tQuestion 9\tRs.1,60,000\n\t\tQuestion 10\tRs.3,20,000\n\t\tQuestion 11\tRs.6,40,000\n\t\tQuestion 12\tRs.12,50,000\n\t\tQuestion 13\tRs.25,00,000\n\t\tQuestion 14\tRs.50,00,000\n\t\tQuestion 15\tRs.1,00,00,000\n\t\tQuestion 16\tRs.7,00,00,000")
    print("6. That's all the rules. Have fun playing!!!")

def incorrectAnswer(questionCount):
    if (questionCount<4):
        print("\nSorry, you have won no prize money!!!")
    elif (questionCount>=4 and questionCount<9):
        print("\nCongratulations, you have won Rs. 10,000")
    elif (questionCount>=9):
        print("\nCongratulations, you have won Rs. 3,20,000")
    exit()
        
    
def quitGame(questionCount):
    if (questionCount==0):
        print("\nSorry, you have won no prize money!!!")
    else:
        prizeMoney = amount_won[questionCount-1]
        print("\nCongratulations, you have won Rs.",prizeMoney,"!!!")
    exit()

# total prize for each question
amount_won = ["1,000", "2,000", "3,000", "5,000", "10,000",
              "20,000", "40,000", "80,000", "1,60,000",
              "3,20,000", "6,40,000", "12,50,000", "25,00,000",
              "50,00,000", "1,00,00,000", "7,00,00,000"]

questions = ['In ODI Cricket, who created the record of scoring the fastest century in just 31 balls ?',
             'If you call someone ''Makkhichoos'' then what are you calling him ?',
             'How many players of a Kho-Kho team can play on the field during the match ?',
             'Which of these Indian cities is closest to the Pakistani city of Lahore ?',
             'The language spoken by the people by Pakistan is ?',
             'The term“Googly” is associated with ?',
             'India first took part in the olympic games in the year ?',
             'Where can we find Kangaroos ?',
             'Oval stadium in England is associated with ?',
             'In 2011 India won the World Cup. Who was adjudicated as the man of the series in the tournament ? ',
             'Eden Gardens in Kolkata is ----- stadium.? ',
             'Ronaldo is associated with ? ',
             'Icc''s 2007, the World Cup Cricket was held in ? ',
             'Wankhede Stadium is at ? ',
             'World''s most ancient game is ? ',
             'Stethoscope was invented by ?',
             'A dye is prepared from ',
             'Which disease is caused by the fungi? ',
             'Which is the Land of the Rising Sun? ',
             'The desert that lies on the boundary between India and Pakistan is ',
             'In which kingdom is the story of the ''Bahubali'' series of films mainly set?',
             'What is the common name for surgery conducted on coronary arteries that supply blood to the heart ?',
             'In July 2017, Narendra Modi Become the first Indian Prime Minister to visit which country ?',
             'Which of these musical instrument is held in one hand and played with the other ?',
             'On the last day of his life Bhagat Singh was reading a book about the Ideology of which revolutionary ?',
             'Which Air force officer had the unique honour of leading the fly-post over the Red fort in Delhi on 15 August 1947 ?',
             'Which image appears on the flip side of the new 2000 Rs Note, launched in 2016?',
             'Which Indian hill station gets its name from the Tibetan words that mean ''land of the thunderbolt''?',
             'Which of these diseases is transmitted by mosquitoes?',
             'Who among these has served as the Ambassador of India to the United Nations?',
             'Who was the first Indian to win the World Junior Badminton Championships?',
             'Which of the following is a recipient of the Nobel Peace Prize?',
             'The cave temples at the historical site of Elephanta are dedicated to which God?']

option1 = ['Corey Anderson', 'Evil', '10', 'Srinagar', 'Hindi',
           'Cricket', '1920', 'Bangladesh', 'polo', 'Virat Kohli',
           'Tennis', 'Cricket', 'Australia', 'Kolkata', 'Wrestling',
           'Bessemer', 'Sida', 'Polio', 'China', 'Thar', 'Magadh',
           'Cataract', 'Israel', 'Tabla', 'Antonio Gramsci ',
           'Arjan Singh', 'Parliament of India', 'Gangtok', 'Rabies',
           'Mohd Hamid Ansari', 'P V Sindhu', 'Mahatma Gandhi', 'Hanuman']
 
option2 = ['AB De Villiers', 'Humble', '9', 'Jaisalmer', 'Palauan',
           'Football', '1928', 'Kenya', 'Cricket', 'Yuvraj Singh',
           'Cricket', 'Football', 'West Indies', 'Mumbai', 'Swimming',
           'Rane Laennec', 'Tridax', 'Malaria', 'Taiwan', 'Sahara',
           'Mahishmati', 'Gastric', 'Jordan', 'Santoor', 'Che Guevera',
           'Pratap Chandra Lal', 'Tractor', 'Aizawl', 'Tetanus', 'I K Gujral',
           'Aparna Balan', 'Swami Vivekananda ', 'Vishnu']
 
option3 = ['Shahid Afridi', 'Dishonest', '7', 'Amritsar', 'Sindhi',
           'Badminton', '1972', 'Pakistan', 'Hockey', 'MS Dhoni',
           'Hockey', 'Hockey', 'South Africa', 'Delhi', 'Boxing',
           'Henry Becquerel', 'Tephrosia', 'Dermatitis', 'Japan',
           'Gobi', 'Kalinga', 'Bypass', 'Saudi Arabia', 'Mridangam',
           'Leon Trotsky ', 'Subroto Mukarjee', 'Red Fort', 'Darjeeling',
           'Japanese Encephalitis', 'Mohd Hidayatullah ', 'Saina Nehwal',
           'Rabindranath Tagore ', 'Shiva']
 
option4 = ['Rohit Sharma', 'Miserly', '8', 'Udhampur', 'English', 'Hockey',
           '1976', 'Australia', 'Football', 'Zaheer Khan', 'Polo', 'Tennis',
           'India', 'Jaipur', 'Running', 'None of these', 'Indigofera',
           'Cholera', 'Australia', 'None of these', 'Badami', 'Debridement',
           'Qatar', 'Dafli', 'Vladimir Lenin', 'Aspy Engineer', 'Mangalyaan',
           'Kohima', 'Plague', 'Zakir Hussain', 'Jwala Gutta', 'Mother Teresa',
           'Kamadeva']
 
options = [option1, option2, option3, option4]
 
# answer key
answer = [2, 4, 2, 3, 3, 1, 1, 4, 2, 2, 2, 2, 2, 2, 1, 3, 4, 3, 3, 1, 2, 3, 1, 4, 4, 1, 4, 3, 3, 1, 3, 4, 3]

questionCount=0
x = input("Are you ready to play Kaun Banega Crorepati (Y/N)??")
if (x=='n'):
    exit()
else:
    rulesOfKBC()
    while(questionCount<=16):
        print("\nQuestion Number:",questionCount+1)
        rand = random.randint(0,len(questions)-1)
        print(questions[rand],"\n1:",options[0][rand],"\n2:",options[1][rand],"\n3:",options[2][rand],"\n4:",options[3][rand],"\n5: Quit")
        while(True):
            userAns = int(input("\nEnter your answer as an option: "))
            if (userAns>5 or userAns<1):
                print("Invalid option. Retry")
                continue
            else:
                break
        if (userAns==5):
            quitGame(questionCount)
        
        questionCount+=1
        if (userAns!=answer[rand]):
            print("\nYou have answered incorrectly :(")
            incorrectAnswer(questionCount)
        elif(questionCount==16):
            print("\nYou have cleared the game")
            quitGame(questionCount)
        else:
            prizeMoney = amount_won[questionCount-1]
            print("\nCorrect Answer, you have won Rs.",prizeMoney,"and are moving on to the next question :)")
            del questions[rand]
            del option1[rand]
            del option2[rand]
            del option3[rand]
            del option4[rand]
            del answer[rand]
            options = [option1,option2,option3,option4]
        continue
