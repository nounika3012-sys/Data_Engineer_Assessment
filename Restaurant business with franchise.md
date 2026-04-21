# **Logical Data Model – Restaurant Business (Franchise \+ Food Trucks)**

For Restaurant businesses that want to scale with franchises and food trucks, I would start by identifying the main entities and their relationships. 

Here’s how I’d approach it:

\- I’d create tables for Restaurants, FranchiseLocations, FoodTrucks, MenuItems, Orders, and Customers, and Employees.  
\- Each Restaurant can have multiple FranchiseLocations and FoodTrucks.  
\- MenuItems are available at each location or truck, and Orders contain multiple MenuItems  
\- Orders are linked to either a FranchiseLocation or a FoodTruck, and each order is placed by a        Customer and handled by an Employee..

For the logical model, I would  define the entities and their relationships.   
For the physical model, I would specify the Tables, Primary keys, and Foreign keys.

**Logical Model Example:**

\- Restaurant (RestaurantID, Name, Owner)  
\- FranchiseLocation (LocationID, RestaurantID, Address, OpenDate)  
\- FoodTruck (TruckID, RestaurantID, LicensePlate, Region)  
\- Employee (EmployeeID, Name, Role, LocationID/TruckID)  
\- MenuItem (MenuItemID, Name, Price, Description)  
\- Customer (CustomerID, Name, Email, Phone)  
\- Order (OrderID, CustomerID, EmployeeID, LocationID/TruckID, OrderDate, TotalAmount)  
\- OrderItem (OrderItemID, OrderID, MenuItemID, Quantity, Price)

**Physical Model (Tables, Primary Keys, Foreign Keys, Data Types) Example :**

* **Primary keys:**   
*  RestaurantID, LocationID, TruckID, EmployeeID, MenuItemID, CustomerID, OrderID,  

   OrderItemID

* **Foreign keys:**   
    
* FranchiseLocation.RestaurantID → Restaurant.RestaurantID,

* FoodTruck.RestaurantID → Restaurant.RestaurantID,   
* Employee.LocationID/TruckID → FranchiseLocation.LocationID/FoodTruck.TruckID, Order.CustomerID → Customer.CustomerID,   
* Order.EmployeeID → Employee.EmployeeID,   
* Order.LocationID/TruckID → FranchiseLocation.LocationID/FoodTruck.TruckID,  
* OrderItem.OrderID → Order.OrderID,   
* OrderItem.MenuItemID → MenuItem.MenuItemID

## **Entities**

* **Customer**  
* **Order**  
* **Order Item**  
* **Payment**  
* **Menu Item**  
* **Menu Category**  
* **Location** (Franchise location or food truck)  
* **Employee**  
* **Franchise**  
* **Inventory**  
* **Supplier**  
* **Menu Item Ingredient**

# **Logical Relationships**

## **Customer and Orders**

* A **Customer places Orders**    
* (1‑to‑many)

## **Order Structure**

*  An **Order contains Order Items**    
* (1‑to‑many)

## **Menu Relationships**

* **Order Item references Menu Item**  
* **Menu Item belongs to Menu Category**

## **Payment**

* **Order is paid through Payment**    
* (1‑to‑1 or 1‑to‑many depending on split payments)

## **Location Relationships**

* **Location receives Orders**  
* **Location employs Employees**  
* **Location maintains Inventory**

## **Franchise**

* **Franchise owns Locations**

* ## **Inventory and Suppliers**

* **Inventory is supplied by Supplier**

**Menu Ingredients**

* **Menu Item uses ingredients from Inventory**    
* (many‑to‑many resolved via Menu Item Ingredient)

This logical model captures all major business entities required for a restaurant business that scales through **franchises and food trucks**. It merges your original file’s structure with your updated model:

* **Customers** place orders at specific **locations** (restaurants or food trucks).  
* **Orders** contain multiple **order items**, each referencing a **menu item**.  
* **Menu items** belong to **menu categories** and are composed of **ingredients** sourced from **inventory**.  
* **Inventory** is maintained at each location and supplied by **suppliers**.  
* **Employees** work at locations and may handle orders.  
* **Payments** settle orders.  
* **Franchises** own one or more locations, supporting multi‑unit expansion.

This structure supports analytics such as:

* Sales by location  
* Menu item performance  
* Ingredient usage  
* Supplier reliability  
* Employee productivity  
* Franchise profitability

In this way, the model supports tracking Sales, Employee performance, Menu popularity, and can scale as the business grows with more locations or trucks.