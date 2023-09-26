# Dataset Description

This dataset contains information related to bank clients and their responses to marketing campaigns. The dataset consists of input variables that detail client information, the last contact of the current campaign, and other attributes related to campaign history. The dataset also includes an output variable indicating whether the client subscribed to a term deposit.

## Input Variables:

### Bank Client Data:
1. **age**: Age of the client (numeric).
2. **job**: Type of job (categorical). Categories include:
   - admin.
   - unknown
   - unemployed
   - management
   - housemaid
   - entrepreneur
   - student
   - blue-collar
   - self-employed
   - retired
   - technician
   - services
3. **marital**: Marital status (categorical). Categories include:
   - married
   - divorced (Note: "divorced" means divorced or widowed)
   - single
4. **education**: Level of education (categorical). Categories include:
   - unknown
   - secondary
   - primary
   - tertiary
5. **default**: Whether the client has credit in default (binary). Categories include:
   - yes
   - no
6. **balance**: Average yearly balance, in euros (numeric).
7. **housing**: Whether the client has a housing loan (binary). Categories include:
   - yes
   - no
8. **loan**: Whether the client has a personal loan (binary). Categories include:
   - yes
   - no

### Related to the Last Contact of the Current Campaign:
9. **contact**: Type of contact communication (categorical). Categories include:
   - unknown
   - telephone
   - cellular
10. **day**: Last contact day of the month (numeric).
11. **month**: Last contact month of the year (categorical). Categories include the months January to December represented as "jan", "feb", ..., "dec".
12. **duration**: Last contact duration, in seconds (numeric).

### Other Attributes:
13. **campaign**: Number of contacts performed during this campaign and for this client (numeric, includes the last contact).
14. **pdays**: Number of days that passed by after the client was last contacted from a previous campaign (numeric; -1 means the client was not previously contacted).
15. **previous**: Number of contacts performed before this campaign and for this client (numeric).
16. **poutcome**: Outcome of the previous marketing campaign (categorical). Categories include:
   - unknown
   - other
   - failure
   - success

## Output Variable (Desired Target):
17. **y**: Has the client subscribed to a term deposit? (binary). Categories include:
   - yes
   - no


