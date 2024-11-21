def inputData():
    annualRateOfInterest = float(input())
    monthlyPayment = int(input())
    begBalance = int(input())
    return annualRateOfInterest,monthlyPayment,begBalance

def calculateValues(annualRateOfInterest, monthlyPayment, begBalance):
    
    intForMonth = (annualRateOfInterest / 100) / 12 * begBalance
    # 소숫점 둘째자리까지 내림 
    intForMonth = int(intForMonth * 100) / 100 #12345.678 -> 1234567.8 -> 1234567 -> 12345.67

    redOfPrincipal = monthlyPayment - intForMonth
    endBalance = begBalance - redOfPrincipal

    return intForMonth, redOfPrincipal, endBalance

def displayOutput(intForMonth, redOfPrincipal, endBalance):
    print("Interest paid for the month: ${:,.2f}\nReduction of principal: ${:,.2f}\nEnd of month balance: ${:,.2f}".format(intForMonth,redOfPrincipal,endBalance))

def main():
    ## Analyze monthly payment of mortgage.  
    annualRateOfInterest, monthlyPayment, begBalance = inputData() 
    (intForMonth, redOfPrincipal, endBalance)= calculateValues(annualRateOfInterest, monthlyPayment, begBalance) 
    displayOutput(intForMonth, redOfPrincipal, endBalance) 

main()