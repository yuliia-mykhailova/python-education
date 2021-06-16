-- The average sum of finished orders
SELECT AVG(total) AS average_of_finished_orders FROM orders WHERE order_status_order_status_id=4;

-- The max sum of order for the third quarter
SELECT MAX(total) AS max_sum FROM orders WHERE created_at BETWEEN '2020-07-01' AND '2020-09-30' AND order_status_order_status_id=4;