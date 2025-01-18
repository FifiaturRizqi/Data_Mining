1. Dataset Transaksi
Dataset ini akan mencatat transaksi yang terjadi dalam aplikasi kasir.

Transaction_ID	Date	Time	Customer_ID	Product_ID	Quantity	Price_per_Unit	Total_Price	Payment_Method	Discount	Tax	Total_After_Discount
1	2025-01-18	09:15	C001	P001	2	50000	100000	Cash	5000	500	95000
2	2025-01-18	09:45	C002	P002	1	75000	75000	Card	0	750	75750
3	2025-01-18	10:30	C003	P003	3	30000	90000	Cash	1000	900	88900
2. Dataset Produk
Dataset ini akan berisi informasi tentang produk yang ada di dalam toko.

Product_ID	Product_Name	Category	Stock_Quantity	Price_Per_Unit	Supplier_ID
P001	Laptop	Elektronik	10	50000	S001
P002	Headphone	Elektronik	15	75000	S002
P003	Mouse	Aksesoris	25	30000	S003
3. Dataset Customer
Dataset ini menyimpan data pelanggan yang sering berbelanja di toko.

Customer_ID	Name	Email	Phone	Address	Registration_Date
C001	Andi Wijaya	andi@email.com	08123456789	Jl. Merdeka No. 1	2024-05-10
C002	Siti Aminah	siti@email.com	08234567890	Jl. Raya No. 5	2024-06-15
C003	Budi Santoso	budi@email.com	08345678901	Jl. Sejahtera No. 7	2024-07-20
4. Dataset Supplier
Dataset ini berisi data pemasok produk.

Supplier_ID	Supplier_Name	Contact_Person	Phone	Email
S001	PT. Tech Supplies	Joko Santoso	0211234567	techsupplies@email.com
S002	Sound World	Rina Wijaya	0212345678	soundworld@email.com
S003	Mouse Factory	Dedi Pratama	0213456789	mousefactory@email.com
5. Dataset Inventaris
Dataset ini berisi informasi tentang inventaris produk yang tersedia di toko.

Product_ID	Stock_Quantity	Reorder_Level	Last_Restock_Date
P001	10	5	2025-01-10
P002	15	7	2025-01-12
P003	25	10	2025-01-14
