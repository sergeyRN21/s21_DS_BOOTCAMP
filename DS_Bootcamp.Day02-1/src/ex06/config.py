filepath = 'data.csv'
num_of_steps = 3
n_predictions = 3  
template = """Report
We have made {} observations from tossing a coin: {} of them were tails and {} of
them were heads. The probabilities are {:.2f}% and {:.2f}%, respectively. Our
forecast is that in the next {} observations we will have: {} tail and {} heads
"""

output_file = 'report.txt'

# Параметры для Telegram
telegram_bot_token = ''
telegram_chat_id = ''