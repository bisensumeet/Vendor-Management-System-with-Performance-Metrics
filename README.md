# Vendor-Management-System-with-Performance-Metrics
Vendor Management System using Django and Django REST Framework. This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics.

# Set Up
## 1 Clone the Repositor:
git clone https://github.com/bisensumeet/Vendor-Management-System-with-Performance-Metrics.git

## 2 Install the dependencies:
pip install -r requirements.txt

## 3 Perform Migrations:
python manage.py makemigrations
python manage.py migrate

## 4 Run the Server:
python manage.py runserver

# Register the User:
All the API endpoints need token authorization, follow the below instructions to generate tokens
1) Register an user by sending a post request on http://localhost:8000/api/register/, json file input of
{username: 'user', password: 'pass', email: 'mail'}

2) Generate a token by sending a post request on http://localhost:8000/api/token/, json file input of
{username: 'user', password: 'pass'}

3) Copy the generated token, go to Authorization window of Postman, select bearer token and paste it. Now you can access all the other API endpoints.

# API Endpoints
For the VendorListAPIView, we have two endpoints:

## 1 GET /api/vendors/
Description: Retrieve a list of all vendors.
Method: GET
Authentication Required: Yes
Permissions Required: IsAuthenticated
Response: Returns a list of all vendors in the system.
Response Status Code: 200 (OK)
Response Body: List of vendor objects serialized as JSON.

## 2 POST /api/vendors/
Description: Create a new vendor.
Method: POST
Authentication Required: Yes
Permissions Required: IsAuthenticated
Request Body: JSON object representing the new vendor to be created.
Response: Returns the details of the newly created vendor if successful.
Response Status Code: 201 (Created) if successful, 400 (Bad Request) if the request is invalid.
Response Body: JSON object representing the newly created vendor, or error details if the request is invalid.

For the VendorDetailAPIView, we have 3 endpoints:

## 1 GET /api/vendors/<vendor_code>/
Description: Retrieve details of a specific vendor.
Method: GET
Authentication Required: Yes
Permissions Required: IsAuthenticated
Parameters: vendor_code (String) - Unique identifier for the vendor.
Response: Returns the details of the specified vendor.
Response Status Code: 200 (OK) if successful, 404 (Not Found) if the vendor does not exist.
Response Body: JSON object representing the vendor, or an error message if the vendor does not exist.

## 2 PUT /api/vendors/<vendor_code>/
Description: Update details of a specific vendor.
Method: PUT
Authentication Required: Yes
Permissions Required: IsAuthenticated
Parameters: vendor_code (String) - Unique identifier for the vendor.
Request Body: JSON object containing the updated details of the vendor.
Response: Returns the updated details of the vendor if successful.
Response Status Code: 200 (OK) if successful, 400 (Bad Request) if the request is invalid, 404 (Not Found) if the vendor does not exist.
Response Body: JSON object representing the updated vendor, or error details if the request is invalid or the vendor does not exist.

## 3 DELETE /api/vendors/<vendor_code>/
Description: Delete a specific vendor.
Method: DELETE
Authentication Required: Yes
Permissions Required: IsAuthenticated
Parameters: vendor_code (String) - Unique identifier for the vendor.
Response: Returns no content if the vendor is successfully deleted.
Response Status Code: 204 (No Content) if successful, 404 (Not Found) if the vendor does not exist.

For the PurchaseOrderListCreateAPIView, we have two endpoints:

## 1 GET /api/purchase_orders/
Description: Retrieve a list of all purchase orders.
Method: GET
Authentication Required: Yes
Permissions Required: IsAuthenticated
Response: Returns a list of all purchase orders.
Response Status Code: 200 (OK)
Response Body: JSON array containing details of all purchase orders.

## 2 POST /api/purchase_orders/
Description: Create a new purchase order.
Method: POST
Authentication Required: Yes
Permissions Required: IsAuthenticated
Request Body: JSON object containing details of the new purchase order.
Response: Returns the details of the newly created purchase order if successful.
Response Status Code: 201 (Created) if successful, 400 (Bad Request) if the request is invalid.
Response Body: JSON object representing the newly created purchase order, or error details if the request is invalid.

For the PurchaseOrderRetrieveUpdateDestroyAPIView, we have three endpoints:

## 1 GET /api/purchase_orders/<po_number>/
Description: Retrieve details of a specific purchase order by its PO number.
Method: GET
Authentication Required: Yes
Permissions Required: IsAuthenticated
Parameters: po_number - The unique identifier of the purchase order.
Response: Returns the details of the specified purchase order.
Response Status Code: 200 (OK) if successful, 404 (Not Found) if the purchase order does not exist.
Response Body: JSON object representing the details of the purchase order.

## 2 PUT /api/purchase_orders/<po_number>/
Description: Update details of a specific purchase order by its PO number.
Method: PUT
Authentication Required: Yes
Permissions Required: IsAuthenticated
Parameters: po_number - The unique identifier of the purchase order.
Request Body: JSON object containing the updated details of the purchase order.
Response: Returns the updated details of the purchase order if successful.
Response Status Code: 200 (OK) if successful, 400 (Bad Request) if the request is invalid.
Response Body: JSON object representing the updated details of the purchase order, or error details if the request is invalid.

## 3 DELETE /api/purchase_orders/<po_number>/
Description: Delete a specific purchase order by its PO number.
Method: DELETE
Authentication Required: Yes
Permissions Required: IsAuthenticated
Parameters: po_number - The unique identifier of the purchase order.
Response: No content in the response body.
Response Status Code: 204 (No Content) if successful, 404 (Not Found) if the purchase order does not exist.

For the AcknowledgmentAPIView, we have one endpoint:

## 1 POST /api/purchase_orders/<po_number>/acknowledge/
Description: Acknowledge a specific purchase order by its PO number, updating its acknowledgment date and triggering recalculation of the average response time for the vendor.
Method: POST
Authentication Required: Yes
Permissions Required: IsAuthenticated
Parameters: po_number - The unique identifier of the purchase order.
Request Body: None
Response: Returns a message indicating the acknowledgment was successful.
Response Status Code: 200 (OK) if successful, 404 (Not Found) if the purchase order does not exist.
Response Body: JSON object containing a message indicating the acknowledgment was successful.

For the VendorPerformanceAPIView, we have one endpoint:

## 1 GET /api/vendors/<vendor_code>/performance/
Description: Retrieve the performance metrics for a specific vendor based on their vendor code. The endpoint also calculates the performance metrics and creates a new entry in the HistoricalPerformance model.
Method: GET
Authentication Required: Yes
Permissions Required: IsAuthenticated
Parameters: vendor_code - The unique identifier of the vendor.
Request Body: None
Response: Returns a JSON object containing the calculated performance metrics for the vendor.
Response Status Code: 200 (OK) if successful, 404 (Not Found) if the vendor does not exist.
Response Body: JSON object containing the following performance metrics:
on_time_delivery_rate: The on-time delivery rate of the vendor.
quality_rating_avg: The average quality rating of the vendor.
average_response_time: The average response time of the vendor.
fulfillment_rate: The fulfillment rate of the vendor.
Additional Action: Creates a new entry in the HistoricalPerformance model with the calculated performance metrics and the current date and time.

For the UserRegistrationAPIView, we have one endpoint:

## 1 POST /api/register/
Description: Register a new user.
Method: POST
Authentication Required: No
Permissions Required: None
Parameters: None
Request Body: JSON object containing user registration data, including username, email, and password.
Response: Returns a JSON object containing the registered user's details if registration is successful.
Response Status Code: 201 (Created) if successful, 400 (Bad Request) if the request data is invalid.
Response Body: JSON object containing the registered user's details, including username, email, and any other fields specified in the serializer.
Additional Action: Creates a new user with the provided registration data.


## Testing

The test suite runs 11 test cases to test the working of each API endpoint and the calculation of each performance metric.
The file vendor/tests.py has thoroughly mentioned the sample data used for testing as well as the expected results. Please make changes accordingly if you want to run any further tests.
For running the test suite, go to the main directory which has manage.py in the terminal and run the following command:
python manage.py test

This concludes our vendor management system with performance metrics.











