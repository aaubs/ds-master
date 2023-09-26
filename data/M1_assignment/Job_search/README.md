# Datasets Descriptions

This repository contains four datasets related to job listings and user interactions with them. Below are the descriptions of each dataset:

## 1. `jobs.csv`

This dataset contains information about various job listings.

### Structure

- **Total Entries**: 84,090
- **Total Columns**: 22

### Columns

1. **Job.ID** (Integer): Unique identifier for each job listing.
2. **Provider** (Integer): Identifier for the provider of the job listing.
3. **Status** (String): Status of the job listing (e.g., open, closed).
4. **Slug** (String): URL slug for the job listing.
5. **Title** (String): Title of the job listing.
6. **Position** (String): Position offered in the job listing.
7. **Company** (String): Name of the company offering the job.
8. **City** (String): City where the job is located.
9. **State.Name** (String): Name of the state where the job is located.
10. **State.Code** (String): Code of the state where the job is located.
11. **Address** (String): Address of the job location.
12. **Latitude** (Float): Latitude of the job location.
13. **Longitude** (Float): Longitude of the job location.
14. **Industry** (String): Industry of the company offering the job.
15. **Requirements** (Float): Requirements for the job (mostly missing values).
16. **Salary** (Float): Salary offered for the job (mostly missing values).
17. **Listing.Start** (String): Start date of the job listing.
18. **Listing.End** (String): End date of the job listing.
19. **Employment.Type** (String): Type of employment (e.g., Full-Time, Part-Time).
20. **Education.Required** (String): Education level required for the job.
21. **Created.At** (String): Timestamp when the job listing was created.
22. **Updated.At** (String): Timestamp when the job listing was last updated.


## 2. `user_past_experience.csv`

This dataset contains information about the past work experiences of various applicants.

### Structure

- **Total Entries**: 8,653
- **Total Columns**: 13

### Columns

1. **Applicant.ID** (Integer): Unique identifier for each applicant.
2. **Position.Name** (String): Name of the position held by the applicant.
3. **Employer.Name** (String): Name of the employer where the applicant worked.
4. **City** (String): City where the applicant's past job was located.
5. **State.Name** (String): Name of the state where the applicant's past job was located.
6. **State.Code** (String): Code of the state where the applicant's past job was located.
7. **Start.Date** (String): Start date of the applicant's past job.
8. **End.Date** (String): End date of the applicant's past job.
9. **Job.Description** (String): Description of the applicant's past job.
10. **Salary** (Float): Salary received by the applicant in their past job.
11. **Can.Contact.Employer** (String): Indicates whether the employer can be contacted (True/False).
12. **Created.At** (String): Timestamp when the entry was created.
13. **Updated.At** (String): Timestamp when the entry was last updated.


## 3. `user_job_views.csv`

This dataset contains information about the job views of various applicants.

### Structure

- **Total Entries**: 12,370
- **Total Columns**: 13

### Columns

1. **Applicant.ID** (Integer): Unique identifier for each applicant.
2. **Job.ID** (Integer): Unique identifier for each job listing.
3. **Title** (String): Title of the job listing.
4. **Company** (String): Name of the company offering the job.
5. **City** (String): City where the job is located.
6. **State.Name** (String): Name of the state where the job is located.
7. **State.Code** (String): Code of the state where the job is located.
8. **Industry** (String): Industry of the company offering the job.
9. **View.Start** (String): Timestamp when the applicant started viewing the job.
10. **View.End** (String): Timestamp when the applicant stopped viewing the job.
11. **View.Duration** (Float): Duration (in seconds) for which the applicant viewed the job.
12. **Created.At** (String): Timestamp when the entry was created.
13. **Updated.At** (String): Timestamp when the entry was last updated.


## 4. `user_work_interest.csv`

This dataset contains information about the work interests of various applicants.

### Structure

- **Total Entries**: 6,560
- **Total Columns**: 4

### Columns

1. **Applicant.ID** (Integer): Unique identifier for each applicant.
2. **Position.Of.Interest** (String): Position or job role that the applicant is interested in.
3. **Created.At** (String): Timestamp when the entry was created.
4. **Updated.At** (String): Timestamp when the entry was last updated.



