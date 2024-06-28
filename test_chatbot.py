import random
import pandas as pd



class FinancialBot:
    def __init__(self):
        self.user_input = None
        self.total_income = None
        self.total_expenses = None
        self.house_expenses = None
        self.entertainment_expenses = None
        self.data = None

    def greet_user(self):
        print("Welcome to the Financial Bot!")
        print("1. Budget Management")
        print("2. Financial questions")
        print("3. Investment Advice and Guide")


    def initiate_budget_management(self):
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
        self.ask_total_income()
        

    def ask_total_income(self):
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
        self.total_income = int(input(income_prompt + " (e.g., ' 200000 ') "))
        self.ask_total_expenses()
        

    def ask_total_expenses(self):
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
        self.total_expenses = int(input(expenses_prompt))
        self.ask_house_expenses()
        

    def ask_house_expenses(self):
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
        self.house_expenses = int(input(house_expenses_prompt))
        self.ask_entertainment_expenses()
        

    def ask_entertainment_expenses(self):
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
        self.entertainment_expenses = int(input(entertainment_expenses_prompt))
        self.check_entertainment_expenses()
        

    def check_entertainment_expenses(self):
        entertainment_percent = (self.entertainment_expenses / self.total_expenses) * 100
        if entertainment_percent > 30:
            self.suggest_savings()
            self.calculate_suggested_expenditure()
        else:
            self.congratulate_user()
            self.calculate_suggested_expenditure()

    def suggest_savings(self):
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
        print(suggestion)

    def calculate_suggested_expenditure(self):
        necessities = (self.total_income * 50) / 100
        entertainment = (self.total_income * 30) / 100
        savings = (self.total_income * 20) / 100

        print(f"Based on the 50-30-20 rule:")
        print(f"Allocate {necessities} towards necessities")
        print(f"Allocate {entertainment} towards entertainment")
        print(f"Allocate {savings} towards savings and debt reduction")

        if savings >= (self.total_income * 0.20):
            print("\nConsidering your substantial savings, have you considered investing in stocks? It could be a great way to potentially grow your wealth over time.")
            # Add other suggestions here...

    def congratulate_user(self):
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
        print(congratulatory_message)

    def initiate_general_financial_questions(self):
        questions = [
            ["What's the best way to allocate my income for different expenses?","The best way to allocate your income for different expenses is a personal decision that you'll have to make based on your own circumstances. However, I generally advise individuals to prioritize saving and investing for the long term, while also ensuring they have a sufficient emergency fund for unexpected expenses. It's important to live within your means, avoid high-interest debt, and consider your financial goals when allocating your income for expenses. Remember, it's not about how much you make, but how much you keep and grow over time."],
            ["How should I prioritize my spending based on my income?"," I would advise prioritizing your spending by first ensuring that you have a solid financial foundation in place. This includes setting aside an emergency fund that can cover at least three to six months of living expenses. Once you have established this safety net, focus on paying off any high-interest debt you may have. After taking care of these essentials, consider investing a portion of your income in a diversified, low-cost index fund such as the S&P 500. This approach allows you to participate in the long-term growth of the stock market while keeping costs minimal. Remember to avoid unnecessary trading and excessive fees that can erode your returns over time. Ultimately, the key is to stay disciplined, ignore the noise of the market, and focus on building wealth steadily over the long term."],
            ["Can you guide me in creating a budget plan for my monthly expenses?","Creating a budget plan is a personal decision that you'll have to make based on your own circumstances. However, I can offer some general advice. Start by listing all your sources of income and then categorize your expenses into fixed expenses (such as rent, utilities, and insurance) and variable expenses (such as groceries, entertainment, and dining out). Make sure your total expenses do not exceed your total income. It's also important to allocate some money for savings and emergencies. Regularly review and adjust your budget as needed to ensure you are meeting your financial goals."],
            ["What percentage of my income should I allocate for essential expenses?","I recommend keeping your essential expenses at a level that allows you to comfortably cover your basic needs without overspending. It's important to prioritize saving and investing for the future while also ensuring you have enough set aside for emergencies. Remember to keep your costs minimal and focus on long-term financial security."],
            ["How can I divide my income to ensure I have enough for savings and bills?","Based on what I've shared in the past, I would recommend thinking of your income allocation as different savings accounts. The great one pays an extraordinarily high interest rate that will rise as the years pass, the good one pays an attractive rate of interest that will be earned on deposits that are added, and the gruesome account both pays an inadequate interest rate and requires you to keep adding money at those disappointing returns. By allocating your income in a way that prioritizes saving and investing for the future, you can ensure you have enough for savings and bills while also allowing your wealth to grow over time."],
            ["What are some effective strategies for budgeting my income effectively?","The most important thing in terms of being able to save is to pay yourself first. Make sure that you save a portion of your income before you start spending on other things. It's a lot easier to save if you do it right away rather than waiting to see what's left at the end of the month. Setting a budget and tracking your expenses can also help you understand where your money is going and identify areas where you can cut back. It's important to differentiate between wants and needs and prioritize your spending accordingly. Additionally, avoiding debt and living below your means can help you build up savings over time. Remember, it's not about how much you make, but how much you save and invest that ultimately determines your financial success."],
            ["Can you provide me with a template or tool to help me budget my income?","I'm happy to provide you with a budgeting template based on the principles I've discussed in the past. Here's a simple template you can use to help budget your income: **Income:** - List all your sources of income, such as salary, bonuses, investments, rental income, etc. - Estimate the amount you expect to receive from each source on a monthly basis. **Expenses:** - Break down your expenses into categories such as housing, transportation, food, utilities, entertainment, savings, etc. - Estimate the amount you expect to spend in each category on a monthly basis. **Debt Payments:** - Include any debt payments you have, such as credit card payments, student loans, mortgage, etc. - Make sure to account for both the principal and interest payments. **Savings and Investments:** - Allocate a portion of your income towards savings and investments for future growth. - Consider setting aside funds for emergencies, retirement, and other financial goals. **Review and Adjust:** - Regularly review your budget to track your actual income and expenses. - Compare your actual spending to your budgeted amounts and adjust as needed to stay on track. Remember, budgeting is a valuable tool to help you manage your finances effectively and reach your financial"],
            ["How do I determine the right balance between spending and saving my income?","Generally, it's wise to save a portion of your income for the future, whether it's for emergencies, retirement, or other financial goals. At the same time, it's important to enjoy the present and spend money on things that bring you happiness and fulfillment. Finding the right balance between spending and saving is key to achieving financial security and well-being."],
            ["What steps can I take to ensure I don't overspend and stay within my budget?","The first step is to create a budget that outlines your income and expenses. It's important to track your spending regularly to see where your money is going. Look for areas where you can cut back or make adjustments. Prioritize your spending based on your needs versus wants. Consider setting up automatic transfers to a savings account to ensure you're saving consistently. And remember, it's important to review and adjust your budget as needed to stay on track."],
            ["Can you help me forecast my future expenses based on my current income?","Based on your current income, you should focus on understanding the future productivity of the assets you are considering. It's important to make a rough estimate of the asset's future earnings to determine if it aligns with your financial goals. Speculating on price changes without considering the underlying productivity of the asset is not a sustainable investment strategy. Remember that past performance is not a reliable indicator of future success. It's essential to make informed decisions based on the fundamentals of the investments you are considering."],
            ["How do I adjust my budget if my income fluctuates from month to month?","When your income fluctuates from month to month, it's important to adopt a budgeting strategy that can accommodate these changes. Just as Charlie and I have emphasized the importance of long-term investment commitments over frequent trading for greater after-tax returns, you should focus on creating a budget that allows for variability in income. One approach could be to prioritize essential expenses such as housing, utilities, and groceries, and then allocate a portion of your income to savings and investments. During months of higher income, you can save more or invest in opportunities that align with your financial goals. In months with lower income, you may need to cut back on discretionary spending to ensure you can cover your essential expenses. By maintaining a long-term perspective and being mindful of your spending habits, you can navigate income fluctuations and work towards achieving your financial objectives."],
            ["What are some common pitfalls to avoid when budgeting my income?","When budgeting your income, it's important to beware of weak accounting practices. Just like in investing, where you should watch out for companies with questionable accounting, in budgeting, you should be wary of any practices that may obscure the true financial picture. Trumpeting non-cash metrics like EBITDA can be misleading, as it may not accurately reflect the cash flow of your budget. Additionally, just as skipping capital expenditures can weaken a business over time, neglecting to budget for essential expenses can have long-term negative consequences on your financial health. It's crucial to have a steady and realistic budget that accounts for all necessary expenses to ensure your financial well-being in the long run. Lastly, be cautious of overly optimistic projections or forecasts when budgeting. Just as investment bankers may provide rosy projections for companies they barely know, it's important to be realistic and conservative in your budgeting assumptions to avoid falling into the trap of overestimating your income or underestimating your expenses."],
            ["Can you suggest ways to increase my income to better meet my expenses?","To increase your income to better meet your expenses, you can focus on increasing the long-term earning power of your current job or business through internal growth. Look for opportunities to enhance your skills, take on additional responsibilities, or seek out promotions within your organization. Additionally, consider ways to generate additional income streams, such as starting a side business or investing in assets that can provide passive income. Remember, the key is to focus on long-term sustainable growth rather than quick fixes."],
            ["How should I handle windfalls or unexpected income in my budget?","When you come into windfalls or unexpected income, it's important to handle it wisely. As I've mentioned in the past, it's crucial to keep your costs minimal and invest for the long term. One strategy that I've recommended is to put a portion of the funds in short-term government bonds and the majority in a low-cost S&P 500 index fund, such as Vanguard's. This approach can help you achieve superior long-term results compared to high-fee managers. Additionally, it's essential to be prepared mentally and financially to act swiftly when opportunities arise, especially during times of economic uncertainty when attractive investment prospects may present themselves. Remember, it's not about timing the market but time in the market that counts."],
            ["Can you recommend budgeting techniques tailored to my specific financial goals?","A straightforward approach can often lead to superior long-term results. For your specific financial goals, I would recommend focusing on creating a solid foundation by following a disciplined budgeting technique. One technique you could consider is setting aside a portion of your income for savings and investments, similar to the advice I gave in my will. You could allocate a percentage of your income towards short-term government bonds for stability and the remainder towards a low-cost index fund, such as the S&P 500, like Vanguard's. By following a consistent savings and investment plan tailored to your financial goals, you can build wealth over time while minimizing costs and maximizing returns. Remember, it's important to stay disciplined and stick to your plan even during market fluctuations."],
            ["What are some ways I can understand and manage my monthly expenses better?","Understanding and managing your monthly expenses better is crucial for financial well-being. One way to do this is by creating a detailed budget that outlines all your income and expenses. Track your spending to see where your money is going and identify areas where you can cut back. Prioritize your expenses based on needs versus wants. Consider setting up automatic transfers to savings or investment accounts to ensure you are saving regularly. It's also important to review your expenses regularly and make adjustments as needed. Remember, small changes can add up to significant savings over time."],
            ["Could you help me break down my spending into categories that make sense for my lifestyle?","If you're looking to categorize your spending, you may want to consider breaking it down into essentials like housing, food, transportation, and healthcare, as well as discretionary spending on things like entertainment, travel, and luxury items. It's important to create a budget that aligns with your financial goals and priorities."],
            ["How can I create a budget that reflects my needs and values?","Start by determining your essential expenses such as housing, food, utilities, and transportation. Then, consider your financial goals and values. Allocate funds towards savings, investments, and any charitable contributions that align with your values. Track your spending to ensure you are staying within your budget and make adjustments as needed. Remember, it's important to prioritize your needs and values when creating a budget that works for you."],
            ["Is there a gentle way to analyze how much I'm spending on groceries each month?","It sounds like you're looking for a way to analyze your grocery spending each month. One approach could be to keep track of your grocery receipts and categorize your expenses (e.g., fruits, vegetables, meat, dairy, snacks) to see where your money is going. You can then compare these expenses month over month to identify any trends or areas where you may be overspending. This method can help you gain a better understanding of your grocery budget and make adjustments as needed."],
            ["Can we chat about my entertainment spending and see if there's room for adjustment?","The first step to budgeting for travel and entertainment expenses is to establish clear and realistic guidelines that define what is allowed, what is not, and how to report and reimburse them. These guidelines should be based on your business needs, industry standards, and legal requirements, and they should be communicated and enforced consistently across your organization. You should also review and update your guidelines regularly to reflect any changes in your business environment, such as new travel destinations, tax laws, or customer preferences."],
            ["How can I find a balance between enjoying dining out and being mindful of my spending?","When it comes to balancing enjoyment with mindful spending, I would suggest finding a consistent approach that aligns with your values and goals. Just as a successful restaurant must maintain a clear message to attract customers, you should have a clear understanding of what you value in dining out and how much you are willing to spend. By being mindful of your spending habits and setting a budget for dining out, you can enjoy the experience without compromising your financial well-being. Remember, consistency and discipline in your approach can lead to long-term success, whether in investing or in managing your personal finances."],
            ["I'm realizing I have quite a few subscriptions. Can we look into those?","It sounds like you have quite a few subscriptions, which can add up over time. It's important to evaluate whether each subscription is providing enough value to justify the cost. Just like in business, it's essential to assess the return on investment for each subscription to ensure you're not overspending on services that may not be essential."],
            ["Do you have any suggestions for small changes I can make to save a little more each month?","I would suggest focusing on your spending habits. Look for areas where you can cut back without significantly impacting your quality of life. Small changes like bringing lunch to work instead of eating out, canceling unused subscriptions, buying generic brands instead of name brands, and reducing energy consumption at home can add up over time and help you save more each month. Remember, it's not about depriving yourself, but rather being mindful of where your money is going and making intentional choices to prioritize saving for your financial future."],
            ["I'm not sure how much I should be saving. Can you help me figure that out?","Based on the principles I have shared in the past, it is important to save and invest wisely for the long term. Consider investing in assets that have the potential to provide attractive returns over time. Remember to focus on businesses with strong competitive advantages and moats that can protect their profitability. It's also crucial to avoid high fees and unnecessary expenses that can erode your returns over the years. Ultimately, the amount you should save depends on your individual financial goals, risk tolerance, and time horizon. It's a personal decision that you'll have to make based on your own circumstances."],
            ["What's a realistic amount of money to set aside for emergencies each month?","Setting aside money for emergencies is a prudent financial practice. It's important to have a sufficient cash reserve to cover unexpected expenses or financial setbacks. Basically have 5 times your monthly expenses as an emergency fund, it is advised to have an year amount of money if your family is dependent on single income."],
            ["I'd appreciate some guidance on how to tackle my debt while still budgeting for everything else.","When it comes to tackling debt while still budgeting for everything else, it's important to approach it with a conservative mindset. Just as we do at Berkshire Hathaway, it's crucial to ensure that you can meet your obligations even under adverse conditions. Consider managing both sides of your financial situation well - obtaining the highest return on assets and the lowest cost on liabilities. It may be beneficial to finance in anticipation of need rather than in reaction to it, as this can help you navigate through tight money conditions and high costs for liabilities. Remember the value of patience and prudence in handling debt. Major declines can offer extraordinary opportunities for those who are not burdened by excessive debt. As Kipling's If suggests, keeping a level head and being able to wait for the right moment can lead to success in the long run. Ultimately, it's about ensuring that you can achieve acceptable long-term results even under challenging circumstances."],
            ["Any tips on reducing my utility bills without sacrificing comfort?","To reduce your utility bills without sacrificing comfort, you can consider implementing energy-efficient practices and technologies in your home. This can include: 1. Upgrading to energy-efficient appliances: Investing in appliances with high energy efficiency ratings can significantly reduce your energy consumption and utility bills over time. 2. Improving insulation: Proper insulation in your home can help regulate indoor temperatures, reducing the need for heating and cooling systems to work as hard, thus lowering energy usage. 3. Installing programmable thermostats: Programmable thermostats allow you to set specific temperatures for different times of the day, optimizing energy usage based on your schedule. 4. Using LED lighting: LED light bulbs are more energy-efficient than traditional incandescent bulbs and can help lower your electricity usage. 5. Sealing air leaks: Ensuring that your home is properly sealed can prevent air leaks, which can lead to energy waste and higher utility bills. By implementing these energy-saving measures, you can reduce your utility bills while maintaining a comfortable living environment."],
            ["How can I make sure I have adequate insurance coverage without overpaying?","To ensure you have adequate insurance coverage without overpaying, you should follow these principles: 1. Understand all the potential risks that could lead to losses. 2. Evaluate the likelihood of these risks materializing and the potential costs associated with them. 3. Set premiums at a level that will, on average, generate a profit after covering prospective loss costs and operating expenses. 4. Be willing to walk away from business if the appropriate premium cannot be obtained. It's essential to avoid the temptation to underprice policies just to compete with other insurers. Quality underwriting is crucial in the insurance business, and it's important to prioritize long-term profitability over short-term gains. Remember, not all insurance policies are the same, and the quality of the promise matters significantly in the insurance industry."],
            ["I'm open to any ideas for increasing my income or cutting expenses. What do you think?","I believe in focusing on increasing the intrinsic value of your skills and knowledge to increase your income over the long term. Look for opportunities to invest in yourself through education, gaining new skills, and expanding your expertise in areas that are valuable in the marketplace. Cutting expenses can be important, but not at the expense of quality or long-term growth. It's essential to prioritize value creation and sustainable practices in both increasing income and cutting expenses."],
            ["How can I track my expenses to ensure I stick to my budget?","To track your expenses and ensure you stick to your budget, you should adopt a disciplined approach similar to how we analyze companies at Berkshire Hathaway. Just as we look for companies with strong accounting practices, you should be wary of weak accounting in your personal finances. Make sure you are accurately recording all your expenses and income. Avoid the temptation to focus solely on EBITDA (earnings before interest, taxes, depreciation, and amortization) equivalents in your personal budgeting. Depreciation, although a non-cash charge, represents a real cash outlay that should not be ignored. Treat your expenses truthfully and account for all cash outflows, even if they are labeled as non-cash expenses. By diligently tracking your expenses and income, you can gain a clear understanding of your financial situation and make informed decisions to stay within your budget. Remember, there is seldom just one oversight in financial matters, so pay attention to the details to ensure your financial health."],
            ["Can you suggest a budgeting method that aligns with my spending habits?","Budgeting is a personal decision that you'll have to make based on your own circumstances. It's important to understand your spending habits, set financial goals, and create a budget that works for you. Some people find success with methods like the 50/30/20 rule, where 50% of income goes to needs, 30% to wants, and 20% to savings and debt repayment. Others prefer more detailed budgeting tools like zero-based budgeting, where every dollar is assigned a specific purpose. Ultimately, the key is to find a budgeting method that helps you track your expenses, save for the future, and live within your means."],
            ["What are the essential categories I should include when budgeting my income?","When budgeting your income, it's important to consider a few essential categories based on our investment philosophy: 1. Productive Assets: Invest in businesses, farms, or real estate that have the ability to deliver output retaining its purchasing power value while requiring minimal new capital investment. Look for assets like Coca-Cola, IBM, or other businesses with strong economic moats. 2. Fixed-Income Securities: Consider medium-term and long-term fixed-income securities for stability and income generation. Evaluate these investments based on after-tax returns and mathematical expectation. 3. Cash Equivalents: Hold short-term cash equivalents for liquidity and as a buffer against market volatility. Be cautious of holding excessive cash during times when it should be deployed for better returns. 4. Arbitrage Commitments: Explore short-term arbitrage opportunities that offer the potential for profit through price differentials or market inefficiencies. By diversifying your income across these categories and focusing on maximizing eventual net worth rather than immediately reportable earnings, you can build a resilient and balanced financial portfolio."],
            ["How do I factor in irregular expenses when creating my budget?","When factoring in irregular expenses when creating your budget, it's important to consider them as real expenses that need to be accounted for just like regular operating costs. Just as capital expenditures are a necessity for a business and are as real an expense as labor or utility costs, irregular expenses should be treated with the same level of importance in your budgeting process. You should ensure that your budget can cover not only your regular expenses but also these irregular expenses that may arise from time to time. It's crucial to have a realistic approach to budgeting by working with a range of possibilities rather than trying to pinpoint exact numbers, as precise calculations can be misleading. Just like how a steady diet is essential for a healthy organism, a well-thought-out budget that includes provisions for irregular expenses will help you maintain financial health and stability in the long run. Remember, it's better to be prepared for unexpected expenses rather than facing financial strain when they occur."],
            ["Can you recommend ways to adjust my budget if my financial situation changes?","In times of financial change, it is crucial to keep a level head and not be swayed by emotions. If your financial situation changes, it may be necessary to adjust your budget accordingly. Look for areas where you can cut back on expenses and prioritize essential spending. Avoid taking on unnecessary debt, as it can hinder your ability to take advantage of opportunities that arise during market downturns. Remember the importance of patience and staying true to your financial goals. As Kipling's If advises, staying calm and focused during turbulent times can lead to success in the long run."],
            ["What are the benefits of using budgeting apps or software to manage my income?","Using budgeting apps or software to manage your income can provide you with a clear overview of your financial situation, help you track your expenses, and assist in setting and achieving financial goals. Just as businesses need to carefully manage their capital expenditures and budgeting to ensure long-term success, individuals can benefit from the discipline and insight that budgeting tools provide. By understanding where your money is going and making informed decisions based on realistic financial data, you can strengthen your financial health and make better choices for the future."],
            ["How can I make my budget flexible enough to accommodate unexpected expenses?","One way to achieve this is by maintaining a conservative approach to budgeting and saving. By setting aside a portion of your income for emergencies or unexpected expenses, you can build a financial cushion that can help you weather unforeseen financial challenges. Additionally, it is important to regularly review and adjust your budget as needed. By staying informed about your financial situation and making proactive adjustments, you can ensure that your budget remains flexible and adaptable to changing circumstances. Ultimately, the key is to be prepared for unexpected expenses by taking a proactive and conservative approach to budgeting and saving."],
            ["Can you provide tips for cutting down on unnecessary expenses to meet my budget?","One tip I can offer is to distinguish between wants and needs. It's important to prioritize spending on necessities over luxuries. Additionally, tracking your expenses and creating a budget can help you identify areas where you can cut back. Remember, small savings can add up over time. It's all about being mindful of where your money is going and making conscious decisions about your spending."],
            ["What are some strategies for dealing with seasonal fluctuations in expenses?","Seasonal fluctuations in expenses can pose challenges for businesses, but there are several strategies that can help manage these fluctuations effectively. One approach is to establish a cash reserve during peak seasons to help cover expenses during slower periods. Additionally, businesses can negotiate flexible payment terms with suppliers to align with cash flow fluctuations. It's also important to closely monitor and forecast cash flow to anticipate seasonal variations and adjust spending accordingly. Another strategy is to diversify revenue streams to reduce reliance on any single seasonally affected source of income. Finally, implementing cost-cutting measures during peak seasons to build up reserves can help cushion the impact of slower periods. By proactively planning and managing cash flow, businesses can navigate seasonal fluctuations in expenses more effectively."],
            ["How do I set realistic goals within my budgeting framework?","When setting realistic goals within your budgeting framework, it's important to keep things simple and avoid swinging for the fences. Focus on the future productivity of the assets you are considering. If you're not comfortable estimating the asset's future earnings, it may be best to move on to other opportunities. Remember that you don't need to be an expert to achieve satisfactory returns, but you should recognize your limitations and follow a course that is certain to work reasonably well. In terms of budgeting and financial reporting, it's crucial to report data that helps financially-literate readers answer key questions such as how much a company is worth, the likelihood of meeting future obligations, and the performance of its managers. Often, this information goes beyond what is provided in standard GAAP reports. The business world is complex, and a single set of rules may not effectively capture the economic reality of all enterprises. Therefore, it's important to look beyond the minimum GAAP presentation to truly understand the financial health and performance of a company."],
            ["Can you help me prioritize my expenses based on my financial goals?","Based on the principles I've shared in the past, I would recommend prioritizing your expenses in a way that aligns with your long-term financial goals. It's essential to focus on minimizing unnecessary costs and fees, especially those related to investment advisors, as they can significantly impact your overall returns. Consider investing in low-cost index funds or other cost-effective investment vehicles to achieve broad market exposure at a minimal expense. By keeping your investment costs low, you can potentially improve your long-term returns and grow your wealth more effectively. Additionally, it's crucial to allocate your resources towards activities or investments that have the potential to generate sustainable returns over time. Prioritize investments that align with your risk tolerance, financial objectives, and time horizon. Remember, the key is to focus on maximizing the value of your investments while minimizing unnecessary expenses. By following a disciplined and cost-conscious approach to managing your finances, you can work towards achieving your financial goals more efficiently."],
            ["How can I involve my family in budgeting decisions to ensure everyone is on board?","Involving your family in budgeting decisions is crucial to ensure everyone is on board and understands the financial situation. Encourage open communication and transparency about the family's financial goals, income, expenses, and savings. You may consider holding regular family meetings to discuss budgeting decisions, set financial goals together, and review progress. Just as in the examples you provided from my past letters, seeking professional advice can also be beneficial in certain situations. Financial planners or advisors can provide guidance and expertise to help the family make informed decisions and navigate complex financial matters. However, it's important to remember that ultimately, the family members themselves must be actively engaged in the budgeting process and take ownership of their financial decisions."],
            ["What should I do if I consistently overspend in certain budget categories?","If you consistently overspend in certain budget categories, it's important to address this issue just as you would address any other financial concern. Overspending in specific areas can weaken your overall financial health, just as skipping necessary expenses weakens a business over time. It's crucial to understand that certain expenses, such as capital expenditures, are necessary for the long-term sustainability of your financial well-being. Just as a business must invest in capital to maintain its operations and growth, you must ensure that your spending aligns with your income and financial goals. If you find yourself consistently overspending in certain budget categories, it may be time to reassess your financial priorities, create a realistic budget that accounts for necessary expenses, and make a conscious effort to curb unnecessary spending in those areas. Remember that financial discipline and prudent decision-making are key to achieving long-term financial success."],
            ["Can you guide me on how to review and adjust my budget on a regular basis?","When it comes to personal finance, it's important to establish a budget that aligns with your financial goals and priorities. Regularly reviewing and adjusting your budget is a key component of financial success. I recommend tracking your income and expenses, identifying areas where you can cut back or save more, and setting aside funds for savings and investments. It's also important to periodically reassess your financial goals and make adjustments to your budget as needed. Remember, a well-managed budget can help you achieve financial stability and build wealth over time."],
            ["How do I account for taxes and other deductions in my budgeting process?","In budgeting, it's important to consider the impact of taxes and other deductions on your financial plan. Just like how we adjust our financial statements to reflect economic reality, you should ensure that your budget accounts for all relevant expenses, including taxes and deductions, to provide a clear and accurate picture of your financial situation. While GAAP may have its limitations, it's crucial to go beyond the basic numbers and provide a comprehensive view that includes all necessary information for decision-making. By incorporating taxes and deductions into your budgeting process, you can better plan for the future and make informed financial choices."],
        ]
        
        user_question = input("Ask me a financial question: ")

        for question, answer in questions:
            if user_question.lower() in question.lower():
                print(answer)

    
    

    def provide_investment_advice(self):
        self.data = pd.read_excel("data.xlsx")
        if self.data is None:
            print("Data not loaded. Please load the data first.")
            return

        term_of_investment = input("For how long do you plan to invest (long term/short term)? ")
        risk_level = input("How comfortable are you with taking risks (low/high)? ")

        if term_of_investment.lower() in ["long term", "short term"]:
            if risk_level.lower() == "low":
                self.suggest_low_risk_investments(term_of_investment)
            elif risk_level.lower() == "high":
                self.suggest_high_risk_investments(term_of_investment)
            else:
                print("Invalid risk level entered.")
        else:
            print("Invalid term of investment entered.")

    def suggest_low_risk_investments(self, term_of_investment):
        low_risk_options = self.data[self.data["Return on capital employed %"] >= 20]
        if term_of_investment.lower() == "long term":
            low_risk_options = low_risk_options[low_risk_options["Sales growth 10Yrs %"] >= 15]

        if not low_risk_options.empty:
            print("Consider the following low-risk investment options:")
            print(low_risk_options[["Name", "current market price Rs.", "Return on capital employed %"]])
        else:
            print("No low-risk investment options available based on your criteria.")

    def suggest_high_risk_investments(self, term_of_investment):
        high_risk_options = self.data[self.data["Return on capital employed %"] < 20]
        if term_of_investment.lower() == "long term":
            high_risk_options = high_risk_options[high_risk_options["Sales growth 10Yrs %"] >= 15]

        if not high_risk_options.empty:
            print("Consider the following high-risk investment options:")
            print(high_risk_options[["Name", "current market price Rs.", "Return on capital employed %"]])
        else:
            print("No high-risk investment options available based on your criteria.")

    
    def run(self):
        self.greet_user()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            self.initiate_budget_management()
        elif choice == 2:
            self.initiate_general_financial_questions()
        elif choice == 3:
            self.provide_investment_advice()
        else:
            print("Invalid choice. Please try again.")


# Create and run the bot
bot = FinancialBot()
bot.run()
