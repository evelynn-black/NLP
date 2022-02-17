YES = {"yes", "y"}
NO = {"no", "y"}
COUGH = "Are you coughing? "
HEADACHE = "Do you have a headache? "
WHEEZE = "Are you short of breath or wheezing or coughing up phlegm? "
PNEUOMONIA = "Possibilities include pneumonia or infection of the airways"
BONES = "Do you have aching bones or aching joints? "
VIRAL = "Possibilities include viral infection"
RASH = "Do you have a rash? "
INSUFFICIENT = "Insufficient information to list possibilities"
THROAT = "Do you have a sore throat? "
THROAT_INFECTION = "Possibilities include throat infection"
BACK_PAIN = f"Do you have back pain just above " \
            f"the waist with chills and fever? "
KIDNEY = "Possibilities include kidney infection"
URINE = "Do you have pain urinating or unrinate more often? "
URINE_INFECTION = "Possibilities include urinary tract infection"
SUN = "Have you spent a day in the sun or in hot conditions? "
SUNSTROKE = "Possibilities include sunstroke or heat exhaustion"
CONFUSION = f"Are you experiencing any of the following: " \
            f"pain when bending your head forwared, " \
            f"nausea or vomiting, " \
            f"bright light hurting your eyes, " \
            f"drowsiness or confusion? "
MENINGITIS = "Possibilities include meningitis"
VOMIT = "Do you have vomiting or diarrhea? "
DIGESTIVE = "Possibilities include digestive tract infection"


def ask(prompt):
    '''
    Function - ask
    '''
    msg = input(prompt).lower()
    return msg

def next_stop_on_yes(answ, no, yes):
    '''
    Function - next_stop_on_yes
        - stops the program on yes
        - continues the program on no

    Parameters:
        - answ = the answer to the previous question
        - no = calls the ask function with the no prompt
        - yes = the message to print out if the answer is yes

    Returns:
        returns the answer to the no question if answ = NO
        returns nothing if answ = YES
    '''
    if answ in YES:
        print(yes)
    elif answ in NO:
        answ = ask(no)
        return answ


def next_branch_at_yes(answ, no, yes):
    '''
    Function - next_branch_on_yes 
        - continues the program on yes
        - continues the program on no

    Parameters:
        - answ = the answer to the previous question
        - no = the question to be asked if answ = NO
        - yes = the question to be asked if answ = YES

    Returns:
        - the response to the question & 1 if answ = YES
        - the response to the question & 2 if  answ = NO
    '''
    if answ in YES:
        answ = ask(yes)
        return answ, 1
    elif answ in NO:
        answ = ask(no)
        return answ, 2


def try_me():
    answ = ask(COUGH)
    next_answ = next_branch_at_yes(answ, HEADACHE, WHEEZE)
    if next_answ[1] == 1:
        answ = next_stop_on_yes(next_answ[0], HEADACHE, VIRAL)
        if answ in YES:
            bones_onward_2()
    elif next_answ[1] == 2:
        answ = next_branch_at_yes(next_answ[0], BONES, CONFUSION)
        if answ[1] == 1:
            bones_onward_2
        elif answ[1] == 2:
            next_answ = next_stop_on_yes(answ[0], VOMIT, MENINGITIS)
            answ = next_stop_on_yes(next_answ, BONES, DIGESTIVE)
            if answ in NO:
                bones_onward_2()




def end(answ, no, yes):
    if answ in YES:
        print(yes)
    elif answ in NO:
        print(no)


def bones_onward_2():
    '''
    Function - bones_onward_2
        - asks the rest of the questions after the bone question

    Parameters: none

    Returns: none
    '''
    answ = ask(BONES)
    next_asnw = next_stop_on_yes(answ, RASH, VIRAL)
    answ = next_stop_on_yes(next_asnw, THROAT, INSUFFICIENT)
    next_answ = next_stop_on_yes(answ, BACK_PAIN, THROAT_INFECTION)
    answ = next_stop_on_yes(next_answ, URINE, KIDNEY)
    next_answ = next_stop_on_yes(answ, SUN, URINE_INFECTION)
    end(next_answ, INSUFFICIENT, SUNSTROKE)
