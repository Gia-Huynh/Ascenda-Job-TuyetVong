
# The submission

 **1. Overview**  
	Submission from applicant Huỳnh Thiết Gia to solve Ascenda homework, written in Python, comes bundled with a precompiled exe file for your convenience.
 
 **2. Installation & Usage**  
 Using any of the options below will run the program which output an `"output.json"` file containing your requested filtered data:  
 - **Using precompiled binary exe file:** Located in the "Binary" folder, you can try running the `"RunExeTest.bat"` file to invoke the program without needing to open your command line app.  
 -  **Run from the source code:** 
	1) `Cd` in to the code directory.
	2) Run `pip install requirements.txt` (The code doesn't have any requirements).
	3) Run `python main.py --dateInput="2019-12-27"`or run the file `"Run.bat"`.
	4) The program will create the file `output.json`.

 **3. To-do list**  
 	Unit testing needs to be done to further verify the program's edge case coverage.
 
 **4. The excerise**  
 Given that the JSON response mentioned above is already loaded inside a file `input.json`, implement a command line application that:

- Accept an argument which is the customer check-in date with the format: `YYYY-MM-DD`
- Load the `input.json` file
- Filter the offers via the following rules:
    - Only select offers with category that is `Restaurant`, `Retail` or `Activity`. Category ID mapping is 


      ```
      Restaurant: 1 
      Retail: 2
      Hotel: 3
      Activity: 4
      ```
    -  Offer needs to be valid till checkin date + 5 days. (valid_to is in `YYYY-MM-DD`)
    -  If an offer is available in multiple merchants, only select the closest merchant
    -  This class should only return 2 offers even though there are several eligible offers
    -  Both final selected offers should be in different categories. If there are multiple offers in the same category give priority to the closest merchant offer.
    -  If there are multiple offers with different categories, select the closest merchant offers when selecting 2 offers
- Finally, save the filtered offers to a file `output.json` (stored at the root of the project)
