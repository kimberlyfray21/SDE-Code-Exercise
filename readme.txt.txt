====SDE Code Exercise=====

This program matches destination addresses with drivers according to the highest score.
The score is calculated by different rules:

#If the length of the shipment's destination street name is even, the base suitability score (SS) is the number of vowels in the driver’s name multiplied by 1.5.

#If the length of the shipment's destination street name is odd, the base SS is the number of consonants in the driver’s name multiplied by 1.

#If the length of the shipment's destination street name shares any common factors (besides 1) with the length of the driver’s name, the SS is increased by 50% above the base SS.

====Requirements====

Python installation
Creation of two json files: Destinations and Drivers

====Input====

It is necessary to run the application from the console: Example py .\main.py
When executing the command, the program will automatically read the 2 files and make the comparison

====Output====

The program will print the best relationship that exists between destinations and drivers according to the highest score

#Example:
Match Destination: 987 Champlin Lake| Driver: Murphy Mosciski| Score: 10
Match Destination: 9856 Marvin Stravenue| Driver: Howard Emmerich| Score: 9
Match Destination: 8725 Aufderhar River Suite 859| Driver: Izaiah Lowe| Score: 9.0
Match Destination: 79035 Shanna Light Apt. 322| Driver: Everardo Welch| Score: 8
Match Destination: 75855 Dessie Lights| Driver: Monica Hermann| Score: 8
Match Destination: 7127 Kathlyn Ferry| Driver: Noemie Murphy| Score: 7.5
Match Destination: 63187 Volkman Garden Suite 447| Driver: Kaiser Sose| Score: 7.5
Match Destination: 2431 Lindgren Corners| Driver: Orval Mayert| Score: 7
Match Destination: 215 Osinski Manors| Driver: Ellis Wisozk| Score: 6.0
Match Destination: 1797 Adolf Island Apt. 744| Driver: Cleve Durgan| Score: 6.0

====Instructions====

1. Clone the repository or copy package in your local /server
2. Open a command prompt and navigate to the directory where the file is located
3. Create two files, the first containing the addresses of the shipment destinations and the second containing the driver's names
5. Run the command "py .\main.py" to execute the program





