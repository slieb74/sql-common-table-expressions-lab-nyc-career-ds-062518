def use_cte_to_determine_average_sale():
    return """WITH average_sales AS (SELECT AVG(amount) FROM sales) SELECT * FROM average_sales;"""

def select_all_above_average_sales():
    return """WITH average_sales AS
                (SELECT AVG(amount) AS avg_sales FROM sales)
                SELECT * FROM sales
                WHERE amount > (SELECT * FROM average_sales);"""
