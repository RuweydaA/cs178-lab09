import boto3

REGION = "us-east-1"
TABLE_NAME = "Movies"  

def get_table():
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)

def print_item(item):
    title = item.get("Title", "Unknown Title")
    year = item.get("Year", "Unknown Year")
    genre = item.get("Genre", "Unknown Genre")

    print(f"  Title : {title}")
    print(f"  Year  : {year}")
    print(f"  Genre : {genre}")
    print()

def print_all_items():
    table = get_table()
    response = table.scan()
    items = response.get("Items", [])

    print(f"Found {len(items)} item(s):\n")

    for item in items:
        print_item(item)

def main():
    print("===== Reading from DynamoDB =====\n")
    print_all_items()

if __name__ == "__main__":
    main()