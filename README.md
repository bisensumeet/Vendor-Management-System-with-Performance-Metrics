# Vendor-Management-System-with-Performance-Metrics
Vendor Management System using Django and Django REST Framework. This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics.<br>

# Set Up
## 1. Clone the Repository:
git clone https://github.com/bisensumeet/Vendor-Management-System-with-Performance-Metrics.git<br>

## 2. Install the dependencies:
pip install -r requirements.txt<br>

## 3. Perform Migrations:
python manage.py makemigrations<br>
python manage.py migrate<br>

## 4. Run the Server:
python manage.py runserver<br>

# Register the User:
All the API endpoints need token authorization, follow the below instructions to generate tokens<br>
1) Register an user by sending a post request on http://localhost:8000/api/register/, json file input of
{username: 'user', password: 'pass', email: 'mail'}<br>

2) Generate a token by sending a post request on http://localhost:8000/api/token/, json file input of
{username: 'user', password: 'pass'}<br>

3) Copy the generated token, go to Authorization window of Postman, select bearer token and paste it. Now you can access all the other API endpoints.<br>

# API Endpoints
For the VendorListAPIView, we have two endpoints:<br>

## 1. GET /api/vendors/
Description: Retrieve a list of all vendors.<br>
Method: GET<br>
Authentication Required: Yes<br>
Permissions Required: IsAuthenticated<br>
Response: Returns a list of all vendors in the system.<br>
Response Status Code: 200 (OK)<br>
Response Body: List of vendor objects serialized as JSON.<br>

## 2. POST /api/vendors/
Description: Create a new vendor.<br>
Method: POST<br>
Authentication Required: Yes<br>
Permissions Required: IsAuthenticated<br>
Request Body: JSON object representing the new vendor to be created.<br>
Response: Returns the details of the newly created vendor if successful.<br>
Response Status Code: 201 (Created) if successful, 400 (Bad Request) if the request is invalid.<br>
Response Body: JSON object representing the newly created vendor, or error details if the request is invalid.<br>

For the VendorDetailAPIView, we have 3 endpoints:<br>

## 1. GET /api/vendors/<vendor_code>/
Description: Retrieve details of a specific vendor.<br>
Method: GET<br>
Authentication Required: Yes<br>
Permissions Required: IsAuthenticated<br>
Parameters: vendor_code (String) - Unique identifier for the vendor.<br>
Response: Returns the details of the specified vendor.<br>
Response Status Code: 200 (OK) if successful, 404 (Not Found) if the vendor does not exist.<br>
Response Body: JSON object representing the vendor, or an error message if the vendor does not exist.<br>

## 2. PUT /api/vendors/<vendor_code>/
Description: Update details of a specific vendor.<br>
Method: PUT<br>
Authentication Required: Yes<br>
Permissions Required: IsAuthenticated<br>
Parameters: vendor_code (String) - Unique identifier for the vendor.<br>
Request Body: JSON object containing the updated details of the vendor.<br>
Response: Returns the updated details of the vendor if successful.<br>
Response Status Code: 200 (OK) if successful, 400 (Bad Request) if the request is invalid, 404 (Not Found) if the vendor does not exist.<br>
Response Body: JSON object representing the updated vendor, or error details if the request is invalid or the vendor does not exist.<br>

## 3. DELETE /api/vendors/<vendor_code>/
Description: Delete a specific vendor.<br>
Method: DELETE<br>
Authentication Required: Yes<br>
Permissions Required: IsAuthenticated<br>
Parameters: vendor_code (String) - Unique identifier for the vendor.<br>
Response: Returns no content if the vendor is successfully deleted.<br>
Response Status Code: 204 (No Content) if successful, 404 (Not Found) if the vendor does not exist.<br>

For the PurchaseOrderListCreateAPIView, we have two endpoints:<br>

## 1. GET /api/purchase_orders/
Description: Retrieve a list of all purchase orders.<br>
Method: GET<br>
Authentication Required: Yes<br>
Permissions Required: IsAuthenticated<br>
Response: Returns a list of all purchase orders.<br>
Response Status Code: 200 (OK)<br>
Response Body: JSON array containing details of all purchase orders.<br>

## 2. POST /api/purchase_orders/
Description: Create a new purchase order.<br>
Method: POST<br>
Authentication Required: Yes<br>
Permissions Required: IsAuthenticated<br>
Request Body: JSON object containing details of the new purchase order.<br>
Response: Returns the details of the newly created purchase order if successful.<br>
Response Status Code: 201 (Created) if successful, 400 (Bad Request) if the request is invalid.<br>
Response Body: JSON object representing the newly created purchase order, or error details if the request is invalid.<br>

For the PurchaseOrderRetrieveUpdateDestroyAPIView, we have three endpoints:<br>

## 1. GET /api/purchase_orders/<po_number>/
Description: Retrieve details of a specific purchase order by its PO number.<br>
Method: GET<br>
Authentication Required: Yes<br>
Permissions Required: IsAuthenticated<br>
Parameters: po_number - The unique identifier of the purchase order.<br>
Response: Returns the details of the specified purchase order.<br>
Response Status Code: 200 (OK) if successful, 404 (Not Found) if the purchase order does not exist.<br>
Response Body: JSON object representing the details of the purchase order.<br>

## 2. PUT /api/purchase_orders/<po_number>/
Description: Update details of a specific purchase order by its PO number.<br>
Method: PUT<br>
Authentication Required: Yes<br>
Permissions Required: IsAuthenticated<br>
Parameters: po_number - The unique identifier of the purchase order.<br>
Request Body: JSON object containing the updated details of the purchase order.<br>
Response: Returns the updated details of the purchase order if successful.<br>
Response Status Code: 200 (OK) if successful, 400 (Bad Request) if the request is invalid.<br>
Response Body: JSON object representing the updated details of the purchase order, or error details if the request is invalid.<br>

## 3. DELETE /api/purchase_orders/<po_number>/
Description: Delete a specific purchase order by its PO number.<br>
Method: DELETE<br>
Authentication Required: Yes<br>
Permissions Required: IsAuthenticated<br>
Parameters: po_number - The unique identifier of the purchase order.<br>
Response: No content in the response body.<br>
Response Status Code: 204 (No Content) if successful, 404 (Not Found) if the purchase order does not exist.<br>

For the AcknowledgmentAPIView, we have one endpoint:<br>

## 1. POST /api/purchase_orders/<po_number>/acknowledge/
Description: Acknowledge a specific purchase order by its PO number, updating its acknowledgment date and triggering recalculation of the average response time for the vendor.<br>
Method: POST<br>
Authentication Required: Yes<br>
Permissions Required: IsAuthenticated<br>
Parameters: po_number - The unique identifier of the purchase order.<br>
Request Body: None<br>
Response: Returns a message indicating the acknowledgment was successful.<br>
Response Status Code: 200 (OK) if successful, 404 (Not Found) if the purchase order does not exist.<br>
Response Body: JSON object containing a message indicating the acknowledgment was successful.<br>

For the VendorPerformanceAPIView, we have one endpoint:<br>

## 1. GET /api/vendors/<vendor_code>/performance/
Description: Retrieve the performance metrics for a specific vendor based on their vendor code. The endpoint also calculates the performance metrics and creates a new entry in the HistoricalPerformance model.<br>
Method: GET<br>
Authentication Required: Yes<br>
Permissions Required: IsAuthenticated<br>
Parameters: vendor_code - The unique identifier of the vendor.v
Request Body: None<br>
Response: Returns a JSON object containing the calculated performance metrics for the vendor.<br>
Response Status Code: 200 (OK) if successful, 404 (Not Found) if the vendor does not exist.<br>
Response Body: JSON object containing the following performance metrics:<br>
on_time_delivery_rate: The on-time delivery rate of the vendor.<br>
quality_rating_avg: The average quality rating of the vendor.<br>
average_response_time: The average response time of the vendor.<br>
fulfillment_rate: The fulfillment rate of the vendor.<br>
Additional Action: Creates a new entry in the HistoricalPerformance model with the calculated performance metrics and the current date and time.<br>

For the UserRegistrationAPIView, we have one endpoint:<br>

## 1. POST /api/register/
Description: Register a new user.<br>
Method: POST<br>
Authentication Required: No<br>
Permissions Required: None<br>
Parameters: None<br>
Request Body: JSON object containing user registration data, including username, email, and password.<br>
Response: Returns a JSON object containing the registered user's details if registration is successful.<br>
Response Status Code: 201 (Created) if successful, 400 (Bad Request) if the request data is invalid.<br>
Response Body: JSON object containing the registered user's details, including username, email, and any other fields specified in the serializer.<br>
Additional Action: Creates a new user with the provided registration data.<br>


## Testing

The test suite runs 11 test cases to test the working of each API endpoint and the calculation of each performance metric.<br>
The file vendors/tests.py has thoroughly mentioned the sample data used for testing as well as the expected results. Please make changes accordingly if you want to run any further tests.<br>
For running the test suite, go to the main directory which has manage.py in the terminal and run the following command:<br>
python manage.py test<br>

This concludes our vendor management system with performance metrics.<br>











