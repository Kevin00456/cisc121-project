# Campus Shuttle Crowd Sorter

## Chosen Problem
This app solves the shuttle stop crowd ranking problem. It ranks campus shuttle stops by crowd count so an extra shuttle can be sent where it is needed most.

## Chosen Algorithm
The algorithm used in this project is Merge Sort.

## Why this algorithm fits
Merge Sort works well for this problem because it efficiently sorts lists by repeatedly dividing the list into smaller halves and merging them back together in order. It is also easy to visualize step-by-step.

## Preconditions / Assumptions
- Each stop must have a name and a crowd count.
- Crowd count must be a number.
- Empty lines are ignored.
- Invalid inputs produce an error message.

## What the user sees during the simulation
The user enters shuttle stop data in the format:

Stop Name, Crowd Count

The app sorts the stops from highest crowd count to lowest crowd count and shows which stop should receive the extra shuttle.

---

# Problem Breakdown & Computational Thinking

## Decomposition
- Read the user input.
- Convert the input into shuttle stop records.
- Validate the input.
- Apply Merge Sort to the crowd counts.
- Display the sorted list of stops.

## Pattern Recognition
The algorithm repeatedly performs the same steps:
- divide the list into smaller halves
- compare values
- merge sorted halves together.

## Abstraction
The program focuses only on important details such as stop name and crowd count. Other unnecessary details are ignored.

## Algorithm Design
Input → Validate Data → Merge Sort → Display Sorted Stops → Recommendation

---

# Flowchart
Start  
↓  
User enters shuttle stop data  
↓  
Validate input  
↓  
Split the list into halves  
↓  
Sort each half  
↓  
Merge the sorted halves  
↓  
Display sorted shuttle stops  
↓  
End

---

# Steps to Run (Local)
1. Install Python
2. Install dependencies:

pip install -r requirements.txt

3. Run the program:

python app.py

---

# Testing

## Test 1 – Normal Input
Library,42  
Main Hall,15  
Residence,67  
Gym,25  

Expected: sorted from highest crowd to lowest.

Result: Passed.

## Test 2 – Empty Input
Expected: error message.

Result: Passed.

## Test 3 – Invalid Crowd Count
Library,abc  

Expected: error message.

Result: Passed.

## Test 4 – One Stop
Library,42  

Expected: one item returned correctly.

Result: Passed.

---

# Demo
(Add screenshots of the app running here.)

---

# Hugging Face Link
(Add your Hugging Face app link after deployment.)

---

# Author
Kevin Johal 
