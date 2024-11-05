# TASK 1 - DUE 03.12.2024

### General Information

Here we can add relevant files concerning task 1. Be a bit careful about the amount of data we add since the 
limit appears to be 2GB for git repos created with a free account.

Link to the google doc: https://docs.google.com/document/d/1IgB5xw7wGH7YgIGa192hlU9EKU0DhggRdntQD0ObNK0/edit?tab=t.0#heading=h.2lbk7i12v4k2

Link to the presentation: https://docs.google.com/presentation/d/1NpLMmUmwTwC8y0PUwsCVmfjx3h8ouMhuFu4Ti0O-ZBA/edit#slide=id.p


### Subtasks and Directions of Work

General Information Flow Diagram

----------    ----------------    ----------
|External| -> |Data Warehouse| -> |Analysis|
----------    ----------------    ----------

Current Roles:
- External- Natasha, Luisa, Anirudh
- Data Warehouse- Nancy, Luke, Nick (Whoever has access to the database)
- Analysis- Luisa, Natasha, Nancy, Chiraag, Anirudh

Current Tasks:
- External
    - Decide on a few data sources
    - Get a Pandas DF containing relevant date information and other important columns (consult analysis)
    - Give Pandas DF to DW team when it has the proper date/time format to join on (refer to google doc) (Rollups may be necessary)
- Data Warehouse
    - Prepare to write data to database from external
    - Consult analysis team to determine what questions need to be SQL'd and ask the DB
      - Create views based on analysis team's responses
      - Deliver data as a pandas DF to analysis team
    - Draw up ER Diagrams for the views used (show development of operations)
    - Formalize queries and outputs (df.head), add to presentation
- Analysis
    - Think about answerable questions, give the top ones to the DW team
    - Use returned Pandas DFs to do further analysis
    - Add to presentation
- All
    - Add to presentation


