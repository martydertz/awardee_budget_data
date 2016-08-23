# NSF awardee_budget_data Risk Analysis
NSF's awardees submits annual budget data. The Office of Budget, Finance and Award Management aggregates that budget data for each award by line item in order to perform its annual risk assessment which assigns a risk rating first to all awardees then to all institutions with NSF awards. 

The analysis proceeeds in the following steps

1. Queery the budget data from SQL server. The queery works on all active awards and sums the budgets by unique award id's.
2. For each high risk budget category, risk points are assigned to each award corresponding to the total amount budgeted for that category. 
3. Risk points are then aggregated by institution. 
4. Additional risk points are added for risky institution features.
5. Institutions are ranked by risk points. Institutions with the highest number of risk and, hence, highest level of risk are visited.

The attached files recreates the analysis. It also includes visualizations and novel approaches to clustering awards by risk to gain insights on NSF's award portfolio that go beyond a ranked list of institutions. 
