import numpy as np

vocabulary = ["Python", "Cloud", "Automation", "Java", "Algorithms", "Web Design"]

items_database = {
    "Course_A": {"name": "Advanced Python & Automation", "tags": ["Python", "Automation"]},
    "Course_B": {"name": "Cloud Architecture with Java", "tags": ["Cloud", "Java"]},
    "Course_C": {"name": "Data Structures & Algorithms", "tags": ["Python", "Algorithms"]},
    "Course_D": {"name": "Frontend Web Development", "tags": ["Web Design"]}
}

def text_to_binary_vector(tags, vocab):
    """Transforms raw qualitative tags into a numerical binary array (1s and 0s)"""
    return np.array([1 if feature in tags else 0 for feature in vocab])

item_vectors = {
    item_id: text_to_binary_vector(data["tags"], vocabulary)
    for item_id, data in items_database.items()
}

def calculate_jaccard_similarity(vector_a, vector_b):
    """
    Computes Jaccard Similarity: Size of intersection divided by size of union.
    Used for simple binary overlap matching.
    """
    intersection = np.logical_and(vector_a, vector_b).sum()
    union = np.logical_or(vector_a, vector_b).sum()
    
    if union == 0:
        return 0.0
    return intersection / union

def get_recommendations(user_choices, top_n=2):
    print(f"\n[INPUT] User selected interests: {user_choices}")
    user_vector = text_to_binary_vector(user_choices, vocabulary)
    
    similarity_scores = {}
    for item_id, item_vector in item_vectors.items():
        score = calculate_jaccard_similarity(user_vector, item_vector)
        similarity_scores[item_id] = score
        
    sorted_items = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)
    
    print("[PROCESS] Matching user profile against database indices...")
    recommendations = []
    for item_id, score in sorted_items[:top_n]:
        if score > 0:  
            item_details = items_database[item_id]
            recommendations.append((item_details["name"], score))
            
    return recommendations

if __name__ == "_main_":
    print("--- DecodeLabs Recommendation Engine Skeleton v1.8 ---")
    
    user_interests = ["Python", "Algorithms"] 
    top_matches = get_recommendations(user_interests, top_n=2)
    
    print("\n[OUTPUT] Top-N Recommended Items:")
    if top_matches:
        for rank, (name, score) in enumerate(top_matches, 1):
            print(f" {rank}. {name} (Match Score: {score:.2f})")
    else:
        print(" No close matches found. Adjust user profile tags.")
    print("\n-----------------------------------------------------")