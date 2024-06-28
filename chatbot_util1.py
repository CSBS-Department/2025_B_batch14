import random

TOTAL_INCOME = 0

def initiate_budget_management():
        prompts = [
            "Sure, I'd be happy to help you manage your budget.",
            "Of course, I can assist you with managing your budget.",
            "Absolutely, managing your budget is important, and I'm here to help.",
            "Certainly, let's work together to manage your budget effectively.",
            "No problem, I'm here to provide guidance on managing your budget.",
            "Definitely, I can offer support in managing your budget.",
            "Absolutely, managing your budget is a crucial aspect of financial wellness, and I'm here to support you.",
            "Sure thing, I can provide assistance and advice for managing your budget.",
            "Absolutely, I'm here to help you navigate and manage your budget effectively.",
            "Without a doubt, managing your budget is key to financial stability, and I'm here to assist you with that.",
            "I'm here to lend a hand with managing your budget, just let me know what you need.",
            "You've got a partner in me when it comes to managing your budget.",
            "Let's tackle your budget together, step by step, so you feel confident and in control.",
            "Managing your budget can feel overwhelming, but I'm here to simplify things for you.",
            "Don't worry, I'll help you manage your budget in a way that feels comfortable and stress-free.",
            "Your budget is important, and I'm here to provide the support and guidance you need.",
            "Managing your budget is like crafting a personalized plan for financial success, and I'm here to help you create yours.",
            "Let's make managing your budget a collaborative effort, so you feel empowered and motivated along the way.",
            "I understand that managing your budget can be challenging, but I'm here to make it as easy and painless as possible.",
            "Your financial well-being matters to me, and I'm committed to helping you achieve your budgeting goals.",
            "Count on me to be your trusted ally as you navigate the ins and outs of budgeting.",
            "Let's team up to make sure your budget reflects your priorities and values.",
            "Your budget is your financial roadmap, and I'm here to help you chart the course.",
            "Managing your budget is all about finding balance, and I'm here to help you strike that balance.",
            "Let's approach budgeting with kindness and patience, focusing on progress rather than perfection.",
            "I'm here to offer gentle guidance and encouragement as you take control of your finances.",
            "Together, we'll create a budgeting strategy that fits your unique lifestyle and goals.",
            "Your budget is a tool for building the life you want, and I'm here to help you wield it effectively.",
            "Let's turn budgeting into a positive and empowering experience, one step at a time.",
            "Remember, your budget is not set in stone – we can adjust and refine it as needed to fit your evolving needs and circumstances.",
            "Your financial journey is unique, and I'm here to provide personalized support every step of the way.",
            "Let's approach budgeting with compassion for ourselves and our financial circumstances.",
            "Managing your budget is about more than just numbers; it's about aligning your spending with your values and priorities.",
            "I'm here to help you build a budget that not only meets your financial goals but also brings you peace of mind.",
            "Let's create a budgeting plan that allows you to live comfortably while working towards your long-term aspirations.",
            "Your budget should serve you, not stress you out. Let's work together to make it manageable and sustainable.",
            "I'm committed to helping you cultivate a healthy relationship with money through mindful budgeting practices.",
            "Let's take a holistic approach to budgeting, considering not just your expenses but also your income, savings, and financial goals.",
            "Managing your budget is an ongoing process, and I'm here to provide consistent support and guidance along the way.",
            "Remember, it's okay to ask for help and take things one step at a time as you navigate your budgeting journey.",
            "Your budget is a reflection of your values and priorities, and I'm here to help you align them with your financial goals.",
            "Let's approach budgeting with curiosity and openness, exploring what works best for you.",
            "I'm here to empower you to make informed decisions about your finances and take control of your financial future.",
            "Let's view budgeting as an opportunity for growth and self-discovery, rather than a chore.",
            "Your budgeting journey is unique to you, and I'm here to provide personalized guidance tailored to your needs.",
            "Let's create a budgeting strategy that allows you to enjoy life today while planning for tomorrow.",
            "Remember, every small step you take towards managing your budget is a step towards financial freedom.",
            "Your financial well-being is important, and I'm here to support you in achieving it through effective budgeting.",
            "Let's approach budgeting with flexibility and adaptability, recognizing that circumstances may change over time.",
            "I'm here to cheer you on as you make progress towards your financial goals, one budgeting decision at a time."
        ]
        # Choose a random prompt
        initial_prompt = random.choice(prompts)
        print(initial_prompt)
        #self.ask_total_income()
        return initial_prompt


def ask_total_income():
        prompts = [
            "What is your annual income?",
            "Could you share your monthly income?",
            "How much do you earn annually?",
            "What is your total income before taxes?",
            "Can you provide your monthly take-home pay?",
            "How much do you make in a year?",
            "What is your yearly salary?",
            "Could you share your gross annual income?",
            "How much do you earn per month?",
            "Can you provide your yearly income?",
            "What is your total income on an annual basis?",
            "Could you share your monthly earnings?",
            "How much do you bring in each year before taxes?",
            "Can you provide your monthly salary?",
            "What is your annual salary?",
            "How much do you earn annually from all sources?",
            "Can you share your yearly income before deductions?",
            "What is your monthly gross income?",
            "Could you provide your total income for the past year?",
            "How much do you make per month before taxes?"
        ]
        # Choose a random prompt
        income_prompt = random.choice(prompts)
        #self.total_income = int(input(income_prompt + " (e.g., ' 200000 ') "))
        #self.ask_total_expenses()
        return income_prompt


def ask_total_expenses():
        prompts = [
            "What is your total monthly expenditure?",
            "Could you share how much you spend on average each month?",
            "How much do you typically spend in a month?",
            "Can you provide an estimate of your total annual expenditure?",
            "What is your total monthly spending across all categories?",
            "How much do you budget for expenses each month?",
            "Can you share your average monthly spending on essentials like rent, utilities, and groceries?",
            "What is your total monthly outflow of cash?",
            "How much do you typically spend each month after accounting for all expenses?",
            "Can you provide a breakdown of your monthly expenses, including both fixed and variable costs?",
            "What is your monthly expenditure?",
            "How much do you estimate you spend annually on discretionary expenses?",
            "Can you share your total annual spending?",
            "What income do you allocate towards monthly expenses?",
            "How much do you spend monthly on bills, subscriptions, and other recurring payments?",
            "What is your average monthly expenditure on necessities like food, clothing, and transportation?",
            "Can you share your total annual spending?",
            "What is your monthly expenditure after subtracting savings and investments from your income?",
            "What is your monthly expenditure like?",
            "Could you provide insight into your monthly spending habits?",
            "How would you describe your monthly spending patterns?",
            "Can you give an idea of your typical monthly outlay?",
            "What does your monthly spending look like in general?",
            "How much do you usually spend in a month?",
            "Can you share your approximate monthly expenses?",
            "What is your monthly spending total?",
            "How would you characterize your monthly financial outflow?",
            "Can you estimate your monthly expenditure for me?"
        ]
        # Choose a random prompt
        expenses_prompt = random.choice(prompts)
        #self.total_expenses = int(input(expenses_prompt))
        #self.ask_house_expenses()
        return expenses_prompt


def ask_house_expenses():
        prompts = [
            "How much do you typically spend on essential household items and bills each month?",
            "Could you provide an estimate of your monthly expenses for household necessities and bills?",
            "What is your average monthly expenditure on household essentials like groceries, toiletries, and cleaning supplies?",
            "Can you share how much you budget for monthly household expenses such as rent or mortgage, utilities, and insurance?",
            "How do you allocate your monthly budget for household necessities and bills?",
            "What is your total monthly spending on essential household items and recurring bills?",
            "Can you give a breakdown of your monthly expenses for house necessities and billing?",
            "How much do you spend monthly on essential household expenses like rent or mortgage, electricity, water, and internet?",
            "What is the average amount you spend each month on household essentials like food, cleaning products, and personal care items?",
            "How much do you typically allocate towards paying for utilities such as electricity, gas, water, and internet?",
            "Can you provide an estimate of your monthly spending on recurring bills such as rent or mortgage, insurance premiums, and subscription services?",
            "What portion of your monthly budget is dedicated to covering housing-related expenses and essential household items?",
            "How do you manage your finances to ensure you can comfortably afford your housing-related expenses and essential bills each month?",
            "Can you break down your monthly spending on house necessities and billing, including any significant fluctuations or seasonal variations?",
            "How do you prioritize your spending when it comes to covering essential household needs and recurring bills?",
            "Could you provide details on your monthly expenses related to housing, including any strategies you use to minimize costs or save money?"
        ]
        # Choose a random prompt
        house_expenses_prompt = random.choice(prompts)
        #self.house_expenses = int(input(house_expenses_prompt))
        #self.ask_entertainment_expenses()
        return house_expenses_prompt



def ask_entertainment_expenses():
        prompts = [
            "How much do you typically spend on entertainment and miscellaneous expenses each month?",
            "Could you provide an estimate of your monthly expenditure for entertainment and other miscellaneous purposes?",
            "What is your average monthly spending on entertainment activities and miscellaneous items?",
            "Can you share how much you budget for entertainment and miscellaneous expenses on a monthly basis?",
            "How do you allocate your monthly budget for entertainment and miscellaneous purposes?",
            "What is your total monthly spending on entertainment, hobbies, and other miscellaneous items?",
            "Can you give a breakdown of your monthly expenses for entertainment and miscellaneous purposes?",
            "How much do you spend monthly on entertainment, such as dining out, movies, concerts, or subscriptions?",
            "What is the average amount you allocate towards miscellaneous expenses like gifts, travel, or personal indulgences each month?",
            "Could you provide insight into your monthly spending habits for entertainment and other miscellaneous purposes?",
            "How do you budget for entertainment and miscellaneous expenses to ensure they align with your financial goals?",
            "Can you provide details on your monthly spending for entertainment, including any memberships, subscriptions, or recreational activities?",
            "What is your average monthly expenditure on discretionary items such as concerts, hobbies, and vacations?",
            "Can you share any specific categories or activities where you tend to spend more on entertainment and miscellaneous purchases?",
            "How do you prioritize your spending on entertainment and miscellaneous items within your overall budget?",
            "What strategies do you use to control or limit your spending on entertainment and other discretionary expenses?",
            "Could you break down your monthly expenses for miscellaneous purposes, including any impulse purchases or one-time expenses?",
            "What percentage of your monthly budget do you allocate towards entertainment and discretionary spending?",
            "Can you provide examples of recent entertainment or miscellaneous purchases you've made and their associated costs?",
            "How do you balance enjoying leisure activities with staying within your budget for entertainment and miscellaneous spending?"
        ]
        # Choose a random prompt
        entertainment_expenses_prompt = random.choice(prompts)
        #self.entertainment_expenses = int(input(entertainment_expenses_prompt))
        #self.check_entertainment_expenses()
        return entertainment_expenses_prompt

def check_entertainment_expenses(ent_exp, tot_exp):
        entertainment_percent = (ent_exp / tot_exp) * 100
        if entertainment_percent > 30:
            response = suggest_savings()
        else:
            response = congratulate_user()
        
        return response


def suggest_savings():
        suggestions = [
            "It may not be the best budget management strategy to spend a significant portion of your income on entertainment and miscellaneous items, especially if it leaves little room for savings or essential expenses.",
            "When your income is limited, it's important to prioritize your spending on necessities and savings rather than indulging in excessive entertainment and miscellaneous purchases.",
            "Spending beyond your means on entertainment and miscellaneous expenses can strain your finances and hinder your ability to meet important financial obligations. It might be worth reassessing your spending priorities.",
            "If your income isn't sufficient to support your current level of spending on entertainment and miscellaneous items, it might be wise to scale back and focus on essentials until your financial situation improves.",
            "Overspending on entertainment and miscellaneous expenses when your income doesn't support it can lead to financial stress and instability. It's worth considering a more balanced approach to budgeting.",
            "When your income doesn't align with your spending on entertainment and miscellaneous items, it's essential to reevaluate your budget and make adjustments to ensure financial sustainability.",
            "It's important to live within your means and prioritize spending on essentials when your income isn't sufficient to support excessive spending on entertainment and miscellaneous items.",
            "Relying on credit or dipping into savings to fund excessive spending on entertainment and miscellaneous purchases can put your financial health at risk. It may be time to reevaluate your spending habits.",
            "If your income doesn't comfortably cover your spending on entertainment and miscellaneous items, it's crucial to reassess your budget and make necessary adjustments to avoid financial strain.",
            "Spending beyond your means on entertainment and miscellaneous purchases can hinder your ability to save for future goals or handle unexpected expenses. It's important to find a balance that aligns with your income."
        ]
        # Choose a random suggestion
        suggestion = random.choice(suggestions)
        return suggestion

def calculate_suggested_expenditure(total_income):
        necessities = (total_income * 50) / 100
        entertainment = (total_income * 30) / 100
        savings = (total_income * 20) / 100

        response = f"Based on the 50-30-20 rule: Allocate {necessities} towards necessities Allocate {entertainment} towards entertainment Allocate {savings} towards savings and debt reduction. Considering your substantial savings, have you considered investing in stocks? It could be a great way to potentially grow your wealth over time."
        
        return response



def congratulate_user():
        congratulations = [
            "Congratulations on effectively managing your budget! Keeping your expenditure on entertainment and miscellaneous purposes below 30% of your total spending shows great discipline and financial awareness.",
            "Well done! It's impressive that you've kept your spending on entertainment and miscellaneous items below 30% of your total expenditure. Your financial discipline is commendable.",
            "Great job on your budget management! Maintaining your expenditure on entertainment and miscellaneous purposes below 30% of your total spending demonstrates your commitment to financial responsibility.",
            "Congratulations! Your ability to keep your spending on entertainment and miscellaneous items below 30% of your total expenditure reflects your prudent financial habits and mindful spending.",
            "Kudos to you for your prudent budgeting! By keeping your expenditure on entertainment and miscellaneous purposes below 30% of your total spending, you're demonstrating excellent financial stewardship.",
            "Fantastic work! Your diligence in keeping your spending on entertainment and miscellaneous items below 30% of your total expenditure is a testament to your wise financial management.",
            "Way to go! Your ability to keep your expenditure on entertainment and miscellaneous purposes below 30% of your total spending showcases your commitment to financial discipline and smart budgeting.",
            "Congratulations on your financial achievements! By keeping your expenditure on entertainment and miscellaneous purposes below 30% of your total expenditure, you're demonstrating savvy budgeting skills.",
            "Well done! Your prudent spending habits are evident in your ability to keep your expenditure on entertainment and miscellaneous purposes below 30% of your total spending.",
            "Bravo! Keeping your spending on entertainment and miscellaneous items below 30% of your total expenditure is a testament to your commitment to financial wellness and smart budgeting."
        ]
        # Choose a random congratulatory message
        congratulatory_message = random.choice(congratulations)
        return congratulatory_message


        