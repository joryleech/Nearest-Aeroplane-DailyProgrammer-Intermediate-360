# [Nearest-Aeroplane-DailyProgrammer-Intermediate-360](https://www.reddit.com/r/dailyprogrammer/comments/8i5zc3/20180509_challenge_360_intermediate_find_the/)

[found on /r/dailyprogrammer](https://www.reddit.com/r/dailyprogrammer/comments/8i5zc3/20180509_challenge_360_intermediate_find_the/)

Daily Programmer - Find the nearest plane to a given latitude and longitude, given a web form that returns a JSON doc of all current flights. Uses the OpenSKY rest api, then calculates the distance from every current flight, and returns the given information about that flight.

Since the world is a sphere the program uses haversines formula to determine the distance from any given point. 

*Haversines Formula* 

    a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
    c = 2 ⋅ atan2( √a, √(1−a) )
    d = R ⋅ c
    where	φ is latitude, λ is longitude, R is earth’s radius
## Input

Input is the latitude and longitude of the given point with a space between

Example Input

    30.354 60.12
    
## Output 

Example Output

    Please input your latitude and longitude like so '11.4 4.1':
    > 105 10
    Distance:6259.111573478084
    Callsign:CQH8579 
    Latitiude:104.9455
    Longitude:16.6808
    Altitude:10370.82
    Origin Country:China
