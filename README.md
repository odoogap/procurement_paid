Procurement Paid
========================================

Check if invoices are paid before creating procurements
-------------------------------------------------------

Odoo by default creates procurements after the sale order has been confirmed, this module checks if the invoices of the sale order are fully paid before creating a new procurement.
In case the accountant wants to ignore the invoices not being fully paid and create the procurement anyway he can do so by clicking in the __Create Procurement__ button on the sale order view.

This module can be disabled in the settings of the inventory, reverting to the default behaviour of Odoo generating procurements for sale orders that don't have afterwards.
