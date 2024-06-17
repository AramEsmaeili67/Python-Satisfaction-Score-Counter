def satisfaction_counter(satisfaction_scores):
    # Initialize counters for different satisfaction levels
    number_of_low_satisfaction_Count = 0
    number_of_moderate_satisfaction_Count = 0
    number_of_high_satisfaction_Count = 0
    
    # Iterate through each score in the satisfaction_scores list
    for score in satisfaction_scores:
        # Check if the score indicates low satisfaction (between 1 and 2)
        if score >= 1 and score <= 2:
            number_of_low_satisfaction_Count += 1
            
        # Check if the score indicates moderate satisfaction (between 3 and 4)
        if score >= 3 and score <= 4:
            number_of_moderate_satisfaction_Count += 1
        
        # Check if the score indicates high satisfaction (exactly 5)
        if score == 5:
            number_of_high_satisfaction_Count += 1
            
    # Print the counts for each satisfaction level
    print('Low Satisfaction: ', number_of_low_satisfaction_Count)   
    print('Moderate Satisfaction: ', number_of_moderate_satisfaction_Count)
    print('High Satisfaction: ', number_of_high_satisfaction_Count)
    

# Example usage of the function with a list of satisfaction scores
satisfaction_counter([1, 2, 3, 4, 5])
