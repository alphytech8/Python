from datetime import datetime

def library_books(book_id, return_date, due_date):
    # Convert input dates from string to datetime objects
    return_date = datetime.strptime(return_date, "%Y-%m-%d")
    due_date = datetime.strptime(due_date, "%Y-%m-%d")
    
    # Calculate the number of days overdue
    over_due = (return_date - due_date).days
    
    # Determine the fine rate based on the number of days overdue
    if over_due <= 7:
        fine_rate = 20 * (return_date - due_date).days
    elif over_due >= 8 and over_due <= 14:
        fine_rate = 50 * (return_date - due_date).days
    elif over_due >= 15:
        fine_rate = 100 * (return_date - due_date).days
    
    # Return the calculated fine rate
    return fine_rate

# Get user input for book ID, return date, and due date
book_id = input("Enter the book id: ")
return_date = input("Enter the return date (YYYY-MM-DD): ")
due_date = input("Enter the due date (YYYY-MM-DD): ")

# Print the calculated fine rate
print(library_books(book_id, return_date, due_date))
