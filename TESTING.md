# Testing

## Manual Testing

Manual tests were carried out across all user stories and features:

### Viewing and Navigation

> USER STORY ID 1 - As a prospect, I want to be able to view a list of services available so that I can select a service to buy

#### Test Case 1.1

**Description:** Verify the Services page displays a list of all available services to the user on entry

**steps:**
1. Open CHrome and navigate to the deployed website
2. Click the Services link in the navbar
3. Scroll down to see a list of all available services
4. Repeat on mobile

**Expected Result:** The Service's pages filter is set to show all services to the user

**Actual Result:** The Service's pages filter is set to show all services to the user

**Pass/Fail:** Pass

> USER STORY ID 2 - As a prosepct, I want to be able to view specific types of services so that I can easily find a service suited to my needs

#### Test Case 2.1 

**Description:** Verify the Services page displays a filter to the user allowing them to filter by service type

**steps:**
1. Open Chrome and navigate to the deployed website
2. Click the Services link in the navbar
3. View service filter and test each link
4. Ensure each filter link displays the correct services
5. Repeat on mobile

**Expected Result:** Users can view a filter at the top of services page allowing them to filter by service type

**Actual Result:** Users can view a filter at the top of services page allowing them to filter by service type

**Pass/Fail:** Pass

**Issues and Fixes during testing of deployed website**
* **Issue:** Filter menu on mobile displays on two lines and overlaps
* **Fix:** Add display inline-block to filter button and include margin
* **Issue:** Filter colour doesn't change on click to display active filter
* **Fix:** JavaScript was required to change the button colour on click. Due to time constraints, the 'Active' colour was removed so all links display the same colour. This has been added to future styling changes to be added. 

> USER STORY ID 3 - As a prospect, I want to be able to view individual service details so that I can identify the service price, description and suitablility

#### Test Case 3.1

**Description:** Ensure that the 'find out more' service button provides the user with a more detailed service description

**steps:**
1. Open Chrome and navigate to the deployed website
2. Click the Services link in the navbar
3. Scroll down to a service and click the 'Find out more' button
4. View the service detail pages decription and price
5. Repeate on mobile

**Expected Result:** The Find out more service button opens the service detail page

**Actual Result:** The Find out more service button opens the service detail page

**Pass/Fail:** Pass

> USER STORY ID 4 - As a prospect, I want to be able to easily view the total of my purchases so that I can ensure the total cost falls within my budget

#### Test Case 4.1

**Description:** Verify that a logged in and logged out user can see the total of the items added to their bag

**steps:**
1. Open Chrome and navigate to the deployed website
2. Navigate to the services page
3. Scroll down and click to find out more about a service
4. On the service detail page click to add the service to the bag
5. View the basket icon in the navigation bar to ensure the correct service price added displays beside it
6. Navigate to the basket and check the Grand total
7. Repeat on mobile
8. Repeat the above for logged in users

**Expected Result:** The user can see the total of their basket in the nav bar and on the bag page

**Actual Result:** The user can see the total of their basket in the nav bar and on the bag page

**Pass/Fail:** Pass

> USER STORY ID 5 - As a prospect, I want to be able to read blogs so that I can expand my knowledge on design and development

#### Test Case 5.1

**Description:** Ensure the user can open up the Blog page and click to read individual blog posts
**steps:**
1. Open Chrome and navigate to the deployed website
2. Navigate to the Blog page on the navigation menu
3. Scroll down to see blogs
4. Click 'Read more' to open up a blog post
5. Ensure blog post displays correctly
6. Repeat on mobile

**Expected Result:** The user can open and read blog posts

**Actual Result:** The user can open and read blog posts

**Pass/Fail:** Pass

> USER STORY ID 6 - As a prospect, I want to be able to review case studies so that I can trust the quality of the freelancing services on offer

#### Test Case 6.1

**Description:** Ensure the user can open up the Case Study page and click to read individual case studies
**steps:**
1. Open Chrome and navigate to the deployed website
2. Navigate to the Case Study page on the navigation menu
3. Scroll down to see case studies
4. Click 'Read more' to open up a case study
5. Ensure case study displays correctly
6. Repeat on mobile

**Expected Result:** The user can open and read case study posts

**Expected Result:**  The user can open and read case study posts

**Pass/Fail:** Pass

**Issues and Fixes during testing of deployed website**

* **Issue:** The case studies heading was further down the page than other styling on the website
* **Fix:** Apply the appropriate class to the case study to give it correct margin

--- 

### Registration and User Accounts

> [USER STORY ID - 7] As a client, I want to be able to easily register for an account so that I can setup my own personal area on the website to see my order history and profile

#### Test Case 7.1

**Description:** The user can create an account and see their purchase history
**Steps:**
1. Open Chrome and navigate to the deployed website
2. Navigate to the 'My Account' dropdown button and select 'Register'
3. Fill in registration details and create an account
4. Navigate to services and add a service to the bage
5. Complete checkout
6. Navigate to 'My Profile' in the 'My Account' dropdown menu
7. View previous order history
8. Repeate on mobile

**Expected Result:** The user can easily create an account and see a summary of the past orders

**Expected Result:** The user can easily create an account and see a summary of the past orders

**Pass/Fail:** Pass

> [USER STORY ID - 8] As a client, I want to be able to easily login or logout so that I can access my personal account information

#### Test Case 8.1

**Description:** A user needs to be logged in to see their profile
**Steps:**
1. Open Chrome and navigate to the deployed website
2. Select the 'My Account' drop down to ensure the 'My Profile' button doesn't appear when not logged in
3. Click the Login button
4. Enter login details and navigate back to the 'My Account' dropdown menu
5. Click the 'My Profile' link
6. Navigate back to the 'My Account' drop down and click to sign out
7. Repeat on mobile

**Expected Result:** Users can easily log in and out. Only logged in users can see their profile

**Expected Result:** Users can easily log in and out. Only logged in users can see their profile

**Pass/Fail:** Pass

> [USER STORY ID 9] As a client, I want to be able to easily recover my password if I forget it so that I can recover access to my account

**As outlined in the README under Features, User Story ID 9 has been moved to Features To Be Added.**

> [USER STORY ID - 10] As a client, I want to be able to receive an email confirmation after registering so that I can verify that my account registration was successful

**As outlined in the README under Features, User Story ID 10 has been moved to Features To Be Added.**

> [USER STORY ID  - 11] As a client, I want to be able to have a personalised user profile so that I can view my personal order history and progress

#### Test Case 11.1

**Description:** Logged in users can navigate to the 'My Profile' sectiona and udpate any of their personal details

**Steps:**
1. Open Chrome and navigate to the deployed website
2. Navigated to the 'My Account' dropdown and click to sign in
3. Once signed in, navigate to the 'My Profile' link on the 'My Account' dropdown
4. Update saved personal details
5. Click to 'Update Information'
6. Go to the homepage and then navigate back the profile
7. Ensure the details have been successfully changes
8. Repeat on mobile

**Expected Result:** Users with an account can update their profile details

**Expected Result:** Users with an account can update their profile details

**Pass/Fail:** Pass

**As outlined in the README under Features, the progress element of User Story ID 11 has been moved to Features To Be Added.**

---

### Sorting and Searching

> [USER STORY ID - 12] As a prospect, I want to be able to sort the list of available services quickly to find a service that meets my requirements

#### Test Case 12.1

**Description:** Verify that users can sort services by type

**Steps:**
1. Open Chrome and navigate to the deployed website
2. Click the Services link in the navbar
3. View service filter and test each link
4. Ensure each filter link displays the correct services
5. Repeat on mobile

**Expected Result:** Users can filter services by type filter on Services page

**Expected Result:** Users can filter services by type filter on Services page

**Pass/Fail:** Pass

> [USER STORY ID - 13] As a prospect, I want to be able to sort services by a specific category so that I can narrow down services to those of interest

**As outlined in the README under Features, User Story ID 13 no longer applies.**

---

### Purchasing and Checkout

> [USER STORY ID - 14] As a prospect, I want to be able to view itmes in my bag to be purchased so that I can see what the total cost of items in my basket are

#### Test Case 14.1

**Description:** Confirm that users can see the total cost of items in the bag and on the navigation menu

**Steps:**
1. Open Chrome and navigate to the deployed website
2. Navigate to the services page
3. Add items to basket
4. Check that the nav bar displays correct the bag total
5. Navigate to the bag page and check that the grand total matches
6. Repeat for logged in users
7. Repeat on mobile

**Expected Result:** Users can see services grand total value in nav bar and bag

**Expected Result:** Users can see services grand total value in nav bar and bag

**Pass/Fail:** Pass

> [USER STORY ID - 15] As a prospect, I want to be able to adjust the quanitity of individual items in my bag so that I can make changes to items in my basket before checking out

#### Test Case 15.1

**Description:** Verify that users are able to ammend (add & remove) their bag items 

**Steps:**
1. Open Chrome and navigate to the deployed website
2. Navigate to the Services page and add a few services to the bag
3. Navigate to the checkout page
4. Click the -/+ links to decrease and increase the service quantities
5. Click to delete a service
6. Repeat on mobile

**Expected Result:** Users can increase or decreate the quantity of items in their bag with the -/+ icons

**Expected Result:** Users can increase or decreate the quantity of items in their bag with the -/+ icons

**Pass/Fail:** Pass

> [USER STORY ID - 16] As a prospect, I want to be able to easily enter my payment information so that I can purchase my desired services

#### Test Case 16.1

**Description:** Verify that users can proceed to checkout page and update their payment details

**Steps:**
1. Open Chrome and navigate to the deployed website
2. Navigate to the servicecs page and add a few services to the bag
3. Navigate to the bag page and click to proceed to secure checkout
4. Input payment details
5. Complete order
6. Repeat on mobile

**Expected Result:** Users can input address and card details easily

**Expected Result:** Users can input address and card details easily

**Pass/Fail:** Pass

> [USER STORY ID - 17] As a prospect, I want to feel my personal and payment information is safe and secure so that I can feel comfortable in providing my payment information to make a purchase

#### Test Case 17.1

**Description:** Ensure that the correct terminology is used in the bag app and checkout page to ensure users' feels secure

**Steps:**
1. Open Chrome and navigate to the deployed website
2. Navigate to Services page and add a service to the bag
3. Check that the notification window says 'Go to secure checkout'
4. Navigate to the Checkout page and check that the button says 'Secure Checkout'
5. Repeat on mobile

**Expected Result:** The word 'Secure' is used on the checkout button

**Expected Result:** The word 'Secure' is used on the checkout button

**Pass/Fail:** Pass

> [USER STORY ID - 18] As a prospect, I want to be able to view my order confirmation after checkout so that I can ensure I have made the correct purchase

#### Test Case 18.1

**Description:** Confirm that users can access their previous order history in their 'My Profile' section

**Steps:**
1. Open Chrome and navigate to the deployed website
2. Log into a user account which has made a purchase
3. Navigate to the 'My Account' menu and select 'My Profile'
4. View the previous order history
5. Repeat on mobile

**Expected Result:** Users can view previous orders in their profile

**Expected Result:** Users can view previous orders in their profile

**Pass/Fail:** Pass

> [USER STORY ID - 19] As a prospect, I want to view the progress of my order so that I know when I can expect it to be ready

**As outlined in the README under Features, User Story ID 19 has been moved to Features To Be Added.**

--- 

### Admin and Store Owner

> [USER STORY ID - 20] As an Admin/ Store Owner, I want to be able to add a service so that I can add new items to my store

#### Test Case 20.1

**Description:**

**Steps:**
1. Open Chrome and navigate to the deployed website
2. Navigate to the Services page
3. Navigate to the 'My Account' dropdown and click to sign in as an "admin user"
4. Once signed in navigate to the 'Service Management' page in the 'My Account' dropdown
5. Add the neccessarry details to add a service and click to add service
6. Navigate to the services page to ensure the service appears
7. Repeat on mobile

**Expected Result:** Admin users can add a new service to the store via the 'Service Management' page

**Expected Result:** Admin users can add a new service to the store via the 'Service Management' page

**Pass/Fail:** Pass

> [USER STORY ID - 21] As an Admin/ Store Owner, I want to be able to edit/ update a service so that I can ammend service descriptions, prices and images

#### Test Case 21.1

**Description:** Users with Admin access have the ability to edit/ update an existing service  

**Steps:**
1. Open Chrome and navigate to the deployed website
2. Navigate to the Services page
3. Navigate to the 'My Account' dropdown and click to sign in as an "admin user"
4. Once signed in navigate to the Services page
5. Scroll down to the services and click to edit a service
6. Edit service details and click to update the service
7. Navigate back to the Services page and ensure the new changes have applied
8. Repeat on mobile

**Expected Result:** Admin users can make changes to existing services on the 'Service Management' page

**Expected Result:** Admin users can make changes to existing services on the 'Service Management' page

**Pass/Fail:** Pass

> [USER STORY ID - 22] As an Admin/ Store Owner, I want to be able to delete a service so that I can remove any services which are no longer being sold

#### Test Case 22.1

**Description:** Admin users and the store owner can easily delete services either via the admin panel or on the services page itself and those without admin access cannot

**Steps:**
1. Open Chrome and navigate to the deployed website
2. Navigate to the Services page
3. Ensure that edit/delete buttons to not appear for user not logged in
4. Click to 'Find out more' about the service
5. Ensure that edit/delete buttons to not appear for user not logged in
6. Navigate to the 'My Account' dropdown and click to sign in as a "regular user"
7. Once signed in navigate back to the Services page and repeat steps 2-5
8. Navigate to the 'My Account' dropdown and sign out
9. Then sign in as an admin
10. Navigate to the Services page and service detail page and ensure that edit/delete buttons appear
11. Click 'delete' to remove a service
12. Navigate back to the services page to ensure the product is deleted
13. Repeat on mobile

**Expected Result:** Only users with special privledges can delete products from the store

**Expected Result:** Only users with special privledges can delete products from the store

**Pass/Fail:** PASS

> As an Admin/ Store Owner, I want to be able to edit/ update the status of an order so that I can update clients of their order progress

**As outlined in the README under Features, User Story ID 22 has been moved to Features To Be Added.**
--- 