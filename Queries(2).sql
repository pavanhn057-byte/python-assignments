CREATE TABLE Chocolates (
    Chocolate_id INT PRIMARY KEY,
    Name VARCHAR(50),
    Brand VARCHAR(50),
    Price DECIMAL(8,2)
);

CREATE TABLE Borrowers (
    borrower_id INT PRIMARY KEY,
    borrower_name VARCHAR(50),
    Chocolate_id INT,
    borrow_date DATE,
    FOREIGN KEY (Chocolate_id) REFERENCES Chocolates(Chocolate_id)
);
INSERT INTO Chocolates VALUES
(1, 'Dairymilk', 'Cadbury', 50.00),
(2, 'Kitkat', 'Nestle', 40.00),
(3, 'Fruit and nut', 'Amul', 100.00);

INSERT INTO Borrowers VALUES
(401, 'Sumadhuri', 1, '2026-01-01'),
(402, 'Madhuri', 2, '2026-01-02'),
(403, 'Pavanasai', 2, '2026-01-03'),
(404, 'Varshitha', 3, '2026-01-04');
SELECT Name, Price
FROM Chocolates
WHERE Price > (
    SELECT AVG(Price)
    FROM Chocolates
);
SELECT borrower_name
FROM Borrowers
WHERE Chocolate_id = (
    SELECT Chocolate_id
    FROM Chocolates
    WHERE Name = 'Dairymilk'
);
SELECT Name
FROM Chocolates
WHERE Chocolate_id IN (
    SELECT Chocolate_id
    FROM Borrowers
    GROUP BY Chocolate_id
    HAVING COUNT(borrower_id) > 1
);
CREATE VIEW Borrower_Chocolate_View AS
SELECT br.borrower_id, br.borrower_name, ch.Name, br.borrow_date
FROM Borrowers br
JOIN Chocolates ch ON br.Chocolate_id = ch.Chocolate_id;
CREATE VIEW Expensive_Chocolates AS
SELECT Chocolate_id, Name, Price
FROM Chocolates
WHERE Price > 40;