# 1045. Customers Who Bought All Products

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Language](https://img.shields.io/badge/Language-MySQL-blue)
![Category](https://img.shields.io/badge/Category-Database-purple)
![Topic](https://img.shields.io/badge/Topic-Grouping%20%7C%20Aggregation-green)
![LeetCode](https://img.shields.io/badge/LeetCode-1045-yellow)

## Problem

**[Customers Who Bought All Products](https://leetcode.com/problems/customers-who-bought-all-products/description/)**

Given two database tables, `Customer` and `Product`, identify all customers who purchased every product available in the `Product` table.

Return the `customer_id` of each qualifying customer.

### Database Schema

**Table: Customer**

| Column | Type |
|---|---|
| customer_id | int |
| product_key | int |

The primary key is `(customer_id, product_key)`. Each row represents a product purchased by a customer.

**Table: Product**

| Column | Type |
|---|---|
| product_key | int |

`product_key` is the primary key and uniquely identifies each available product.

## Approach: GROUP BY + HAVING + COUNT(DISTINCT) + Subquery

The key observation is:

> A customer has purchased all available products when their number of distinct purchased products equals the total number of products in the Product table.

We can solve this efficiently using grouping and aggregate filtering.

### 1. Group Purchases by Customer

```sql
SELECT customer_id
FROM Customer
GROUP BY customer_id;
```

This creates a separate group for every customer.

### 2. Count Distinct Products Purchased

```sql
COUNT(DISTINCT product_key)
```

Counts the number of unique products purchased by each customer.

Using `DISTINCT` ensures that each product contributes only once to the count.

### 3. Calculate the Total Number of Products

```sql
SELECT COUNT(*)
FROM Product;
```

This subquery returns the total number of available products.

Since `product_key` is the primary key, every row represents one unique product.

### 4. Filter Using HAVING

```sql
HAVING COUNT(DISTINCT product_key) = (
    SELECT COUNT(*)
    FROM Product
);
```

`HAVING` filters grouped results based on aggregate calculations.

Only customers whose distinct product count equals the total product count are returned.

## SQL Solution

```sql
SELECT
    customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (
    SELECT COUNT(*)
    FROM Product
);
```

## Example and Dry Run

### Input

**Customer**

| customer_id | product_key |
|---:|---:|
| 1 | 5 |
| 2 | 6 |
| 3 | 5 |
| 3 | 6 |
| 1 | 6 |

**Product**

| product_key |
|---:|
| 5 |
| 6 |

### Step 1: Count Available Products

The `Product` table contains two products.

\[
TotalProducts = 2
\]

### Step 2: Group Purchases by Customer

| Customer | Products Purchased | Distinct Count |
|---|---|---:|
| 1 | 5, 6 | 2 |
| 2 | 6 | 1 |
| 3 | 5, 6 | 2 |

### Step 3: Compare Purchase Counts

| Customer | Purchased Count | Required Count | Qualifies |
|---|---:|---:|---|
| 1 | 2 | 2 | Yes |
| 2 | 1 | 2 | No |
| 3 | 2 | 2 | Yes |

### Output

| customer_id |
|---:|
| 1 |
| 3 |

**Explanation:**

- Customer 1 purchased products 5 and 6.
- Customer 2 purchased only product 6.
- Customer 3 purchased products 5 and 6.

Therefore, customers 1 and 3 purchased all available products.

## Complexity Analysis

Let:

- `C` represent the number of purchase records in the `Customer` table.
- `P` represent the number of products in the `Product` table.

| Complexity | Analysis |
|---|---|
| Time | Depends on the database execution plan, grouping strategy, and available indexes. |
| Space | Depends on the number of customer groups and the database's aggregation strategy. |

The query groups customer purchase records, calculates distinct product counts, and compares them against the product catalog size.

The actual execution cost depends on the database engine and its optimization strategy.

## Important SQL Concepts

| SQL Concept | Purpose |
|---|---|
| `GROUP BY` | Groups purchases by customer |
| `COUNT()` | Counts records or products |
| `DISTINCT` | Counts unique purchased products |
| `HAVING` | Filters aggregated groups |
| Subquery | Calculates the total number of available products |
| `COUNT(*)` | Counts all product records |

## Common Mistakes

### 1. Using COUNT(*) for Customer Purchases

```sql
HAVING COUNT(*) = (
    SELECT COUNT(*)
    FROM Product
);
```

This counts purchase records rather than distinct products.

Although the problem's composite primary key prevents duplicate customer-product pairs, `COUNT(DISTINCT product_key)` expresses the requirement more directly and is robust when the underlying data contains duplicates.

### 2. Using WHERE Instead of HAVING

`WHERE` filters individual records before grouping, while `HAVING` filters groups after aggregation.

Since the comparison involves an aggregate count, `HAVING` is appropriate.

### 3. Comparing Against the Wrong Product Count

The required count must come from the `Product` table, not from the number of purchase records.

### 4. Forgetting GROUP BY

Without grouping by `customer_id`, the query cannot calculate a separate purchase count for each customer.

## Alternative Solution: Relational Division Using NOT EXISTS

The same problem can be expressed using nested `NOT EXISTS` conditions.

The idea is to identify customers for whom there is no product that they have not purchased.

```sql
SELECT DISTINCT c.customer_id
FROM Customer c
WHERE NOT EXISTS (
    SELECT 1
    FROM Product p
    WHERE NOT EXISTS (
        SELECT 1
        FROM Customer c2
        WHERE c2.customer_id = c.customer_id
          AND c2.product_key = p.product_key
    )
);
```

**How it works:**

1. The inner query checks whether a customer purchased a particular product.
2. The inner `NOT EXISTS` identifies products the customer did not purchase.
3. The outer `NOT EXISTS` ensures that no such missing product exists.
4. `DISTINCT` prevents a customer from appearing multiple times.

**Recommended approach:** Use the `GROUP BY` and `HAVING` solution as the primary implementation because it is shorter, easier to understand, and demonstrates an important SQL aggregation pattern.

## Key Takeaways

- `GROUP BY` separates records into customer-specific groups.
- `COUNT(DISTINCT)` counts unique purchased products.
- `HAVING` filters groups using aggregate conditions.
- Subqueries can calculate reference values for aggregate comparisons.
- Relational division is a useful database concept for answering questions involving *all* related records.
- Always compare the number of distinct purchased products against the actual product catalog size.

## Related Problems

| Problem | Difficulty | Main Concept |
|---|---|---|
| [1280. Students and Examinations](https://leetcode.com/problems/students-and-examinations/) | Easy | CROSS JOIN, LEFT JOIN, GROUP BY |
| [596. Classes With at Least 5 Students](https://leetcode.com/problems/classes-with-at-least-5-students/) | Easy | GROUP BY and HAVING |
| [1193. Monthly Transactions I](https://leetcode.com/problems/monthly-transactions-i/) | Medium | Conditional Aggregation |
| [586. Customer Placing the Largest Number of Orders](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/) | Easy | GROUP BY and COUNT |

## Repository Structure

```text
LeetCode-Solutions/
└── Databases/
    └── Medium/
        ├── 1045_Customers_Who_Bought_All_Products.sql
        └── README.md
```

## References

- [LeetCode – Customers Who Bought All Products](https://leetcode.com/problems/customers-who-bought-all-products/)
- [MySQL Documentation – Aggregate Functions](https://dev.mysql.com/doc/refman/8.4/en/aggregate-functions.html)
- [MySQL Documentation – GROUP BY Optimization](https://dev.mysql.com/doc/refman/8.4/en/group-by-optimization.html)

---

**Problem:** 1045

**Difficulty:** Medium

**Language:** MySQL

**Topics:** Database, GROUP BY, HAVING, COUNT, DISTINCT, Subqueries, Relational Division

**Primary Technique:** Group purchases by customer and compare distinct product counts against the total product count.