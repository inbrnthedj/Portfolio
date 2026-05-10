SELECT LastName, FirstName, Orders.OrderID, SUM(Quantity * Price) AS SalesAmt
FROM Employees
	INNER JOIN Orders
		ON Employees.Employeeid = Orders.EmployeeID
    	INNER JOIN OrderDetails
    		ON Orders.OrderID=OrderDetails.OrderID
   	 INNER JOIN Products
    		ON OrderDetails.ProductID=Products.ProductID
GROUP BY LastName, FirstName, Orders.OrderID
HAVING Orders.OrderID in (10372, 10424, 10417, 10324, 10351)
ORDER BY SalesAmt DESC;