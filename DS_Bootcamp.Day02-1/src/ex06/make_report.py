import sys
from analytics import Research
from config import filepath, template, num_of_steps, n_predictions, output_file, telegram_bot_token, telegram_chat_id

def main():
    research = Research(filepath)
    data = research.file_reader(has_header=True)
    
    if data is not None:
        analytics = Research.Analytics(data)
        
        heads_count, tails_count = analytics.counts(analytics.data)
        heads_fraction, tails_fraction = analytics.fractions(heads_count, tails_count)
        
        predictions = analytics.predict_random(n_predictions=n_predictions)
        predicted_heads = sum([prediction[0] for prediction in predictions])
        predicted_tails = sum([prediction[1] for prediction in predictions])
        
        report = template.format(
            num_of_steps,
            tails_count,
            heads_count,
            tails_fraction,
            heads_fraction,
            n_predictions,
            predicted_tails,
            predicted_heads
        )
        
        analytics.save_result_to_file(report, output_file)

        research.send_telegram_message("Отчет успешно создан.", telegram_bot_token, telegram_chat_id)

    else:
        research.send_telegram_message("Отчет не создан из-за ошибки.", telegram_bot_token, telegram_chat_id)

if __name__ == "__main__":
    main()