import nltk
from nltk.chat.util import Chat, reflections

pairs = [
            [
                '(hi|hello|hey|hello|greetings|whats up)',
                ['Greetings, How can i help you?\n']
            ],
            [
                '(.*)(name is|im|i\'m|i am|call me) (.*)',
                ["Hello %3, how are you today?\n"]
            ],
            [
                '(.*)your name(.*)',
                ["I'm Finbot, I can assist you with your financial queries.\n"]
            ],
            [
                '(.*)(where|investment|investing|options)(.*)(invest|investing|investment|options)(.*)',
                [
                    "There are following investment options: "
                    "\n1. Fixed Deposits"
                    "\n2. Mutual Funds"
                    "\n3. Stocks"
                    "\nwhich section would you like to explore?\n"
                 ]
            ],
            [
                '(.*)(start|help)(.*)',
                [
                    "For getting started there are following investment options: "
                    "\n1. Fixed Deposits"
                    "\n2. Mutual Funds"
                    "\n3. Stocks"
                    "\nwhich section would you like to explore?\n"
                 ]
            ],
            [
                '(.*)(FD|fd|fixed|deposit|deposits|Fixed|Deposit|Deposits)(.*)',
                [
                    "Following banks provide Fixed Deposits:"
                    "\n1. SBI"
                    "\n2. HDFC"
                    "\n3. UBI"
                    "\n4. Axis Bank"
                    "\nWhich bank would you like to go for?\n"

                ]
            ],
            [
                '(.*)(SBI|sbi|state bank)(.*)',
                ["Risk: Low\nFixed APR: 5.60\n"]
            ],
            [
                '(.*)(HDFC|hdfc)(.*)',
                ["Risk: Low\nFixed APR: 6.20\n"]
            ],
            [
                '(.*)(UBI|ubi|union bank)(.*)',
                ["Risk: Low\nFixed APR: 5.90\n"]
            ],
            [
                '(.*)(Axis|axis)(.*)',
                ["Risk: Low\nFixed APR: 6.56\n"]
            ],
            [
                '(.*)(mutual funds|Mutual Funds)(.*)',
                [
                    "We have following options for Mutual Funds:"
                    "\n1. Bluechip Fund"
                    "\n2. Small Cap"
                    "\n3. Technology Direct"
                    "\nWhich one would you explore?\n"
                ]
            ],
            [
                '(.*)(Bluechip|bluechip)(.*)',
                ["Provider: Axis Bank\nRisk: Moderate\nAverage APR: 20.16\n"]
            ],
            [
                '(.*)(Small Cap|small cap)(.*)',
                ["Provider: Nippon India\nRisk: High\nAverage APR: 29.31\n"]

            ],
            [
                '(.*)(Technology Direct|technology direct)(.*)',
                ["Provider: ICICI\nRisk: High\nAverage APR: 43.08\n"]

            ],
            [
                '(.*)(Stocks|stocks)(.*)',
                [
                    "We have following stocks listed:"
                    "\n1. Wipro           |    Average APR: 45.52"
                    "\n2. Infosys         |    Average APR: 51.61"
                    "\n3. Reliance Ind.   |    Average APR: 69.42"
                    "\n4. Tata Motors     |    Average APR: 12.47"
                    "\n5. IRCTC           |    Average APR: 6.64"
                    "\nRisk: Very high\n"
                ]
            ],
            [
                '(.*)(quit|bye|exit|no)(.*)',
                ["Signing out, hope to see you again!\n\n\n\n",]
            ],
            [
                '(.*)(ok|OK|okay)(.*)',
                ["Is there anything else you would like to know?\n",]
            ],
            [
                '(.*)',
                ["Sorry, could not comprehend\n"]
            ]
        ]


if __name__ == "__main__":
    print("Booting up...\n\n")
    print("Hello! I'm Finbot, I can assist you with your financial queries.")
    chat = Chat(pairs, reflections)
    chat.converse()
