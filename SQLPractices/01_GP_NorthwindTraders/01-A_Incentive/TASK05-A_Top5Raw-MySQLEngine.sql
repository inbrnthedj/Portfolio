SELECT LastName, FirstName, Orders.OrderID, Products.ProductID, Quantity, Price, SUM(Quantity * Price) AS SalesAmt
FROM Employees
	INNER JOIN Orders
		ON Employees.Employeeid = Orders.EmployeeID
    	INNER JOIN OrderDetails
    		ON Orders.OrderID=OrderDetails.OrderID
   	 INNER JOIN Products
    		ON OrderDetails.ProductID=Products.ProductID
GROUP BY LastName, FirstName, Orders.OrderID, Products.ProductID, Quantity, Price
ORDER BY SalesAmt DESC
LIMIT 5;