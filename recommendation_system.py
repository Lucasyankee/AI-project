items = [
    {"id": 1, "name": "Intro to AI", "tags": {"ai", "ml", "basics"}},
    {"id": 2, "name": "Deep Learning 101", "tags": {"dl", "ml", "ai"}},
    {"id": 3, "name": "Data Visualization", "tags": {"viz", "charts", "plots"}},
    {"id": 4, "name": "Recommenders", "tags": {"recsys", "ml", "ai"}},
    {"id": 5, "name": "Python for Data", "tags": {"python", "data"}},
]

def recommend_by_tag(query_tag, k=3):
    scored = []
    for it in items:
        score = 1 if query_tag in it["tags"] else 0
        scored.append((score, it))
    scored.sort(reverse=True, key=lambda x: x[0])
    return [it for s, it in scored[:k] if s > 0]

def main():
    q = "ai"
    recs = recommend_by_tag(q, k=3)
    print(f"Query tag: {q}")
    for r in recs:
        print("-", r["name"])

if __name__ == "__main__":
    main()