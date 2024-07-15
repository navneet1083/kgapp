# Knowledge Graph Application

Knowledge Graph Application to visualise relationships between entities.


### Web Interface:

> Front-end Development:

- Create a web-based front end using HTML and JavaScript.
- Provide input fields for users to add entities and their relationships.

> User Input:

- Allow users to manually input entity relationships through text fields or Include a file upload option to allow users to upload datasets in CSV format 
- Use case to be considered for input   
  - Geographic Relationships : establish geographic relationships, such as cities within states and states within countries
- Ensure the interface includes fields for the first entity, relationship, and second entity.
- Enable users to query the graph and visualize the results.
  
> Visualization:
  
- Display the knowledge graph visually on the web page 
- Ensure the visualization updates dynamically as new data is added.
  
### Graph Management and Querying: 

> Backend Implementation:

- Use Flask, a Python web framework, to create the back end for handling requests and responses.
- Use networkx, a Python library, to create and manage the knowledge graph.

> Functionality:

- Implement endpoints to add relationships and query the graph.

### Integration: 

- Integrate the front end and back end to create a cohesive application.
- Handle user input, perform necessary processing, and update the graph.
- Ensure the results are displayed on the web page in a user-friendly manner.