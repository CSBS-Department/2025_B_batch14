import pandas as pd
def provide_investment_advice(investment_term, risk_lvl):
    data = pd.read_excel("chatbot/data.xlsx")
    if data is None:
        print("Data not loaded. Please load the data first.")
        return

    #term_of_investment = input("For how long do you plan to invest (long term/short term)? ")
    #risk_level = input("How comfortable are you with taking risks (low/high)? ")
    print(investment_term)

    if investment_term.lower() in ["long term", "short term"]:
        if risk_lvl.lower() == "low":
            response = suggest_low_risk_investments(investment_term, data)
        elif risk_lvl.lower() == "high":
            response = suggest_high_risk_investments(investment_term, data)
        else:
            response = "Invalid risk level entered."
    else:
        response = "Invalid term of investment entered."

    return response 



def suggest_low_risk_investments(investment_term, data):
    low_risk_options = data[data["Return on capital employed %"] >= 20]
    if investment_term.lower() == "long term":
        low_risk_options = low_risk_options[low_risk_options["Sales growth 10Yrs %"] >= 15]

    if not low_risk_options.empty:
        response = "Consider the following low-risk investment options:" + str(low_risk_options[["Name"]])
    else:
        response = "No low-risk investment options available based on your criteria."
    return response



def suggest_high_risk_investments(investment_term, data):
    high_risk_options = data[data["Return on capital employed %"] < 20]
    if investment_term.lower() == "long term":
        high_risk_options = high_risk_options[high_risk_options["Sales growth 10Yrs %"] >= 15]

    if not high_risk_options.empty:
        response = "Consider the following low-risk investment options:" + str(high_risk_options[["Name"]])
    else:
        response = "No high-risk investment options available based on your criteria."
    return response

