## Flask Application Design

### HTML Files

- **index.html**: This will serve as the main page of the application. It should include a form that allows the user to enter the details of the ad campaign, such as the campaign name, start date, end date, budget, etc.
- **results.html**: This page will display the ad campaign details entered by the user in a tabulated format. It should also include a link to download the data in a CSV file.

### Routes

**1. `/`:** This route will handle the GET request for the main page (index.html).

**2. `/submit`:** This route will handle the POST request when the user submits the ad campaign details. It should validate the input data and store it in a database or other data store.

**3. `/results`:** This route will handle the GET request to display the ad campaign details. It should fetch the stored data and render the results.html page with the data.

**4. `/download`:** This route will handle the GET request to download the ad campaign details in a CSV file. It should generate a CSV file with the data and return it to the user.