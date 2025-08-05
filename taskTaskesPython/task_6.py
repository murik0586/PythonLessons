import csv
import json

def main():
    categories = {}
    with open('data_task6/purchase_log.txt', 'r', encoding='utf-8') as f:
        next(f)
        for line in f:
            try:
                purchase = json.loads(line.strip())
                user_id = purchase.get('user_id')
                category = purchase.get('category')
                if user_id and category:
                    categories[user_id] = category
            except json.JSONDecodeError:
                continue

    with open('data_task6/visit_log__1_.csv', 'r', encoding='utf-8') as input_f, \
            open('data_task6/funnel.csv', 'w', encoding='utf-8', newline='') as output_f:
        reader = csv.reader(input_f)
        writer = csv.writer(output_f)
        next(reader)
        writer.writerow(["user_id", "source","category"])
        for row in reader:
            user_id = row[0]
            source = row[1]
            if user_id in categories:
                writer.writerow([user_id,source,categories[user_id]])

# read_csv("data_task6/purchase_log.txt")


if __name__ == "__main__":
    main()
