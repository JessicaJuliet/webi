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
4. Repeat on mobile

**Expected Result:** Users can view a filter at the top of services page allowing them to filter by service type

**Actual Result:** Users can view a filter at the top of services page allowing them to filter by service type

**Pass/Fail:** Pass

**Issues and Fixes during testing of deployed website**
* Issue: Filter menu on mobile displays on two lines and overlaps
* Fix: Add display inline-block to filter button and include margin
* Issue: Filter colour doesn't change on click to display active filter
* Fix: JavaScript was required to change the button colour on click. Due to time constraints, the 'Active' colour was removed so all links display the same colour. This has been added to future styling changes to be added. 

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

**Actual Result:** The user can open and read case study posts

**Pass/Fail:** Pass

**Issues and Fixes during testing of deployed website**
**Issue:** The case studies heading was further down the page than other styling on the website
**Fix:** Apply the appropriate class to the case study to give it correct margin