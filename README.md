# election-analysis

## Project Overview
The purpose of the audit is to ensure accuracy of the voting data during the election.

## Results
- **How many votes were cast in this congressional election?**
    - There were a total of 369,711 total votes cast. For future auditing the variable total_votes will match this value.
- **Breakdown of votes and percentage of total votes by county**
    - Jefferson County: 38,855 votes representing 10.5% of all votes cast.
    - Denver County: 306,055 votes representing 82.8% of all votes cast.
    - Arapahoe County: 24,801 votes representing 6.7% of all votes cast.
- **Which county had the largest number of votes?**
    - Denver County had  the largest share of votes cast amongst all the counties in the election.
- **Breakdown of votes and percentage of total votes by candidate**
    - Charles Casper Stockham: recieved 85,213 votes representing 23.0% of all votes cast.
    - Diana Degette: recieved 272,892 votes representing 73.8% of all votes cast.
    - Raymon Anthony Doane: recieved 11,606 votes representing 3.1% of all votes cast.
- **Which candidate won the election?**
    - Diana Degette was the winning candidate for the congressional election with 272,892 votes, which was 82.8% of all votes cast.

## Summary
This script is a robust tool for this election and others in the future. A few ways to to leverage this resource in the futur include:

### Multiple Seats in Next Election 
This Python script was originally designed for a single race with one seat up for votes. Yet many elections have multiple seats available for voting, such as a US Senate seat or a Governors race. This script can be adapted to look at multiple races assuming the results file has all of them included in distinct columns. This would make tabulating data for future multi-race elections much easier.

### Real-time Reporting
This Python script can also be adjusted with a slight tweak to the language to showcase which candidate is leading in a given race. Often results are shared live now to allow local news networks to report on the race. If more specific geographic location was available in the voter list (like zip codes), election officials could see if turnout in certain areas of a county or congressional district are unusually low and use to detect potential issues in voting access.
