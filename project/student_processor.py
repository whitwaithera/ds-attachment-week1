import csv

# 1. Raw Data (Simulating data you might get from a CSV or API)
students_data = [
    {"name": "Brian", "lifeskills": 85, "web_development": 90, "structured_cabling": 78},
    {"name": "Kevin", "lifeskills": 45, "web_development": 55, "structured_cabling": 60},
    {"name": "Faith", "lifeskills": 95, "web_development": 92, "structured_cabling": 98},
    {"name": "Amina", "lifeskills": 30, "web_development": 40, "structured_cabling": 35},
    {"name": "Dennis", "lifeskills": 70, "web_development": 75, "structured_cabling": 80}
]

def calculate_average(student):
    """Calculates the average score for a single student."""
    # Updated keys to match the new subjects
    scores = [student["lifeskills"], student["web_development"], student["structured_cabling"]]
    return sum(scores) / len(scores)

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

# Main Execution
if __name__ == "__main__":
    print("Starting data processing...")
    
    # Process the data
    all_processed, passing_only = process_students(students_data)
    
    # Print results to console
    print("\n--- All Students ---")
    for record in all_processed:
        print(record)
        
    print("\n--- Passing Students Only ---")
    for record in passing_only:
        print(record)
        
    # Save the passing students to a CSV file
    save_to_file(passing_only, "passing_students.csv")