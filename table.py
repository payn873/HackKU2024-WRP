create_movies_table_query = """
CREATE TABLE inventory(
id INT AUTO_INCREMENT PRIMARY KEY
Category VARCHAR(100),
CategoryID INT,
SubCategory VARCHAR(100),
SubCategoryID INT,
ItemName VARCHAR(100),
ItemID INT,
Vendor VARCHAR(100),
VendorID INT,
UnitPrice($/BL) FLOAT,
Weight(BLS) FLOAT,
ItemPrice FLOAT,
InitialQuantity INT,
ReStockDate VARCHAR(100),
RestockQty INT,
ReturnQty INT,
SoldQty INT,
Qtybalance INT
)

"""
