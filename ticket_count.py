
input_tickets = 6

def count_tickets(random):
    random = random-1
    return random
    

def tickets_left(tickets):
    while tickets:
        tickets_left = count_tickets(tickets)
        tickets = tickets_left
        print
        print(f"ticket remaining {tickets}")
        if tickets_left == 0:
            print("full house")
            break
        
tickets_left(input_tickets)
        
  