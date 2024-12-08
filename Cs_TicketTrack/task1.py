# Task 1 ticket tracker

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(tickets):
    """
    Opens a new service ticket.
    """
    customer = input("Enter customer name: ")
    issue = input("Enter issue description: ")
    new_ticket_id = f"Ticket{len(tickets) + 1:03}"
    tickets[new_ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
    print(f"New ticket {new_ticket_id} created successfully for {customer}.\n")

    ticket_tracker()

def update_ticket_status(tickets):
    """
    Updates the status of an existing ticket.
    """
    ticket_id = input("Enter the ticket ID to update: ")
    if ticket_id in tickets:
        print(f"The current status of {ticket_id} is: {tickets[ticket_id]['Status']}")
        new_status = input("Enter the new status (open/closed): ")
        if new_status == "open" or new_status == "closed":
            tickets[ticket_id]["Status"] = new_status
            print(f"Status of {ticket_id} updated to: {new_status}")
        else:
            print("Invalide status. Enter open or closed.")
    else:
        print("Ticket not found.")

    ticket_tracker()

def filter_and_display_tickets(tickets):
    """
    Filters tickets by status ('open' and 'closed') and displays them 
    in two separate lists."""

    category_tickets = {"open": [], "closed": []}

    for ticket_id, details in tickets.items():
        status = details["Status"]
        if status in category_tickets:
            category_tickets[status].append((ticket_id, details))


    for status, ticket_list in category_tickets.items():
        print(f"\n--- {status.capitalize()} Tickets---")
        if ticket_list:
            for ticket_id, details in ticket_list:
                print(f"""Ticket ID: {ticket_id}
                Customer: {details['Customer']}"
                Issue: {details['Issue']}
                Status: {details['Status']}
                -----------------------""")
        else:
            print(f"No {status} tickets.")

    ticket_tracker()

def ticket_tracker():

        while True:
            print("\n--- Ticket Tracker Menu ---")
            print("1. Display tickets")
            print("2. Open a new ticket")
            print("3. Update ticket status")
            print("4. Exit")
        
            choice = input("Enter your choice (1-4): ").strip()

            if choice == "1":
                filter_and_display_tickets(service_tickets)
            elif choice == "2":
                open_ticket(service_tickets)
            elif choice == "3":
                update_ticket_status(service_tickets)
            elif choice == "4":
                print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Select a valid option.")

ticket_tracker()
