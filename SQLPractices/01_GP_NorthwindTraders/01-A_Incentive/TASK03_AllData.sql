SELECT LastName, FirstName, Orders.OrderID, Products.ProductID, Quantity, Price
FROM Employees
	INNER JOIN Orders
		ON Employees.Employeeid = Orders.EmployeeID
    INNER JOIN OrderDetails
    		ON Orders.OrderID=OrderDetails.OrderID
   	 INNER JOIN Products
    		ON OrderDetails.ProductID=Products.ProductID
ORDER BY LastName, FirstName;