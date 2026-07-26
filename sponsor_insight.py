from legislation import search_legislation
from collections import Counter

def most_active_sponsors(query, top_n=10):
    data = search_legislation(query, limit=150)
    total = data["estimated_total_results"]
    bills = data["results"]

    sponsor_counts = Counter()

    for item in bills:
        bill = item["bill"]
        for sponsor in bill.get("primary_sponsors", []):
            sponsor_counts[sponsor["name"]] += 1

    print(f"Query: '{query}'")
    print(f"Total bills matched: {total}")
    print(f"Bills analyzed: {len(bills)}")
    print()
    print(f"Top {top_n} most active sponsors on this topic:")
    for name, count in sponsor_counts.most_common(top_n):
        print(f"  {count} bill(s) - {name}")

if __name__ == "__main__":
    most_active_sponsors("artificial intelligence chatbot minor")