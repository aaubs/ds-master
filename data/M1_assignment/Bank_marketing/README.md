# Bank Marketing Dataset Description

This dataset contains information about various marketing campaign attributes and client details, with a total of 41,188 entries and 21 columns.

## Structure

- **Total Entries**: 41,188
- **Total Columns**: 21

## Columns

### Bank Client Data:

1. **age** (Numeric): Age of the client.
2. **job** (Categorical): Type of job (admin., blue-collar, entrepreneur, housemaid, management, retired, self-employed, services, student, technician, unemployed, unknown).
3. **marital** (Categorical): Marital status (divorced, married, single, unknown).
4. **education** (Categorical): Education level (basic.4y, basic.6y, basic.9y, high.school, illiterate, professional.course, university.degree, unknown).
5. **default** (Categorical): Has credit in default? (no, yes, unknown).
6. **housing** (Categorical): Has housing loan? (no, yes, unknown).
7. **loan** (Categorical): Has personal loan? (no, yes, unknown).

### Related with the Last Contact of the Current Campaign:

8. **contact** (Categorical): Contact communication type (cellular, telephone).
9. **month** (Categorical): Last contact month of the year.
10. **day_of_week** (Categorical): Last contact day of the week.
11. **duration** (Numeric): Last contact duration, in seconds.

### Other Attributes:

12. **campaign** (Numeric): Number of contacts performed during this campaign for this client.
13. **pdays** (Numeric): Number of days that passed by after the client was last contacted from a previous campaign (999 means client was not previously contacted).
14. **previous** (Numeric): Number of contacts performed before this campaign for this client.
15. **poutcome** (Categorical): Outcome of the previous marketing campaign (failure, nonexistent, success).

### Social and Economic Context Attributes:

16. **emp.var.rate** (Numeric): Employment variation rate - quarterly indicator.
17. **cons.price.idx** (Numeric): Consumer price index - monthly indicator.
18. **cons.conf.idx** (Numeric): Consumer confidence index - monthly indicator.
19. **euribor3m** (Numeric): Euribor 3 month rate - daily indicator.
20. **nr.employed** (Numeric): Number of employees - quarterly indicator.

### Output Variable (Desired Target):

21. **y** (Categorical): Has the client subscribed to a term deposit? (no, yes).
