import csv

# ==========================================
# STEP 1: Raw Data (Simulating a dataset)
# ==========================================
students_data = [
    {"name": "Brian", "math": 85, "science": 90, "history": 78},
    {"name": "Kevin", "math": 45, "science": 55, "history": 60},
    {"name": "Faith", "math": 95, "science": 92, "history": 98},
    {"name": "Dennis", "math": 30, "science": 40, "history": 35},
]

# ==========================================
# STEP 2: Calculate Average Function
# ==========================================
def calculate_average(student):
    """Calculates the average score for a single student."""
    scores = [student["math"], student["science"], student["history"]]
    return sum(scores) / len(scores)

# ==========================================
# STEP 3: Process Data Function
# ==========================================
def process_students(data):
    """Processes the data to add averages and filter passing students."""
    processed_data = []
    passing_students = []
    
    for student in data:
        avg = calculate_average(student)
        student_record = {
            "name": student["name"],
            "average": round(avg, 2),
            "status": "Pass" if avg >= 50 else "Fail"
        }
        processed_data.append(student_record)
        
        if avg >= 50:
            passing_students.append(student_record)
            
    return processed_data, passing_students

# ==========================================
# STEP 4: Save to File Function
# ==========================================
def save_to_file(data, filename):
    """Saves the processed data to a CSV file."""
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "average", "status"])
            writer.writeheader()
            writer.writerows(data)
        print(f"Successfully saved data to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

# ==========================================
# STEP 5: Main Execution
# ==========================================
if __name__ == "__main__":
    print("Starting data processing...")
    
    # 1. Process the data
    all_processed, passing_only = process_students(students_data)
    
    # 2. Print results to console
    print("\n--- All Students ---")
    for record in all_processed:
        print(record)
        
    print("\n--- Passing Students Only ---")
    for record in passing_only:
        print(record)
        
    # 3. Save the passing students to a CSV file
    save_to_file(passing_only, "passing_students.csv")