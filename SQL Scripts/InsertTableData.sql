-- SQLite scripts to setup product table.
INSERT INTO product VALUES (NULL, 'Rolling pin', 'This is a pin for rolling. Obviously.', 9.99);
INSERT INTO product VALUES (NULL, 'Spatula', 'Flip things! Disclaimer: We are not responsible for broken yolks!', 4.99);
INSERT INTO product VALUES (NULL, 'Pizza cutter', 'Much easier than picking up the whole pizza at once', 7.49);
INSERT INTO product VALUES (NULL, 'Coffee grinder', 'Grind your own beans. Look down on people who drink instant coffee', 39.99);

-- Insert into Customers NOTE: this demonstrates an alternative way to insert data without having to provide the NULL value for ID!
INSERT INTO Customers (name, email, phone_number) VALUES
('Alice Johnson', 'alice@example.com', '07123456789'),
('Bob Smith', 'bob@example.com', '07987654321'),
('Ash Malde', 'avm@collyers.ac.uk', '07123454321'),
('Miles McGowan', 'mfm@collyers.ac.uk', '07987656789');

-- Insert into Sales
INSERT INTO Sales (product_id, customer_id, quantity, sale_date) VALUES
(1, 1, 2, '2024-04-15'),
(2, 2, 1, '2024-04-16'),
(3, 2, 3, '2024-04-21'),
(3, 1, 3, '2024-04-22'),
(2, 3, 3, '2024-04-23'),
(4, 4, 3, '2024-04-26'),
(3, 4, 1, '2024-04-26');