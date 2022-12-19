## Using Python Inheritance to build a Rule Engine for Big Data Validation

In an ETL job, the requirement was to create a Rule Engine with few rules common to all LOBs and few unique and specific to others. In such a case, we can create a common LOB rule file to be attached to all ETL jobs and also custom Python distributions specific to LOBs.

In that case, using Python Inheritance with Common Rules as Parent class and LoB rules as Child class. We can instantiate the methods of parent class from child class. We can also access parent class methods and attributes using super() method in __init__ of child class. 

## Advantages of Inheritance for Rule Engine:
1. Minimal changes are required in parent class distribution file. Commit can solely be focussed on child class.
2. We are able to instantiate the methods of parent class from child class.
3. Reusability of code
4. Less time required for development
5. Any major changes across LOBs, then change it in parent class so that it will be reflected in all sub-classes.
