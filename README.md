# EMSI Grades Checker

## **ℹ️ Project Overview**

EMSI Grades Checker is a Python program dedicated to checking and retrieving grades from the EMSI student portal. Its primary function is to automate the process of checking grades and providing a convenient way for students to access their academic performance.

## **👨‍💻 Technologies**

- **Python:** The fundamental programming language of script.
- **Selenium:** Employed for web scraping, allowing for the automated process of logging into the EMSI student portal and fetching grade details.

## **📁 Folder Structure**

- 📂 **scraper**
  - ***init.py***: Represents a web scrapig boilerplate, utilizing Selenium and the undetected_chromedriver library, and imports necessary modules to automate web interactions with Chrome.
- 📂 **utils**
  - ***auth.py***: Manages authentication into the EMSI student portal, navigating into the website and then inserting login credentials passed as environment variables.
  - ***navigate.py***: Automates the navigation on the grades webpage (1st and 2nd term).
  - ***grades.py***: Contains the main script responsible for scraping grade information from the web portal and saving it to a JSON file.
- ***main.py***: Coordinates the entire workflow, designed to continuously gather grade data until authentication and data retrieval are successfully completed.

## **🖥️ Code Execution**

1. **Authentication:**
   - The **authenticate()** function attempts to log in to the web portal using provided credentials. It navigates to the specified base URL and fills in the username, password, and city fields.
   - After submitting the login form, it checks if the authentication was successful or not, and according to that returns boolean value.
2. **Navigation:**
   - The **navigate(term)** function navigates to a term on the web portal, by locating the dropdown menu containing terms and clicks on it to expand the options, then selects the term specifies by the passed parameter **term**.
   - If the selected term is disabled, indicating it's not selectable, it prints a message and returns **False**. Otherwise, it clicks on the term link and returns **True**.
3. **Grades Scraping:**
   - The **bring_grades()** function is responsible for scraping grade information for each module within the selected term.
   - For each module on the page, it scrolls to it and extracts its title, clicks on the details dropdown button to reveal additional information, waits for the module details to load and then extracts the module's average grade and details of its sub-modules.
   - The scraped data is stored and saved to the JSON file **grades.json**.
4. **Retry Mechanism:**
   - The **main.py** script orchestrates the execution of the authentication, navigation, and grades scraping processes in a loop.
   - It continuously attempts authentication and navigation through terms until successful or until an exception occurs.
   - If the authentication is successful and grade scraping completes for at least one term, the script terminates.
5. **Error Handling and Retry Strategy:**
   If any exception occurs during the execution, the script pauses for 5 seconds before retrying the process.

## **📋 Setup Instructions**

Follow these steps to set up and run the project:

1. **Clone the Repository:**
   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/sifeddineEddr/emsi-grades-checker.git
   ```

2. **Install Requirements:**

   - Navigate to the project directory:
     ```bash
     cd emsi-grades-checker
     ```
   - Install the required Python dependencies using pip:
     ```bash
     pip install -r requirements.txt
     ```

3. **Build the `.env` File:**

   - Copy the `.env.example` file and rename it to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit the `.env` file and fill in the required environment variables with your specific values:
     - `CITY`: City value for authentication (**CB** for Casablanca - **RA** for Rabat - **MK** for Marrakech - **TA** for Tangier - **FS** for Fez).
     - `USER`: Username for authentication.
     - `PASSWORD`: Password for authentication.

4. **Execute the Script:**

   - Run the `main.py` script and provide the desired terms's grades number to initiate the scraping process:
     ```bash
     py main.py 1
     ```
     or
     ```bash
     py main.py 2
     ```

5. **Review Results:**
   - After execution, review the scraped data stored in the **grades.json** file.

**⚠️Note:** Ensure that you have Python installed on your system and that the required dependencies are installed before running the script.
