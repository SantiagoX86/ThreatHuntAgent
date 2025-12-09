'''
This project will be a reconstruction of LogN Pacific Threat Hunter using most
    efficient/Pythonic standards including the implementation of Classes and OOP
    where appropriate.
'''

'''
1. User Inputs::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
This will initiate the program as various inputs will be obtained from the user,
including:
- brief prompt describing suspicious activity to be searched for
- search type desired (speed optimized, robust, budget, etc)
    1. Should be a list in the console that prompts the user to input a number from the option
    2. Will feed selection into the Prompt generator
- user credentials, may be obtained via keys.py file such as Josh has done
    1. Most likely user entering manually as that would more closely mimic a working
        environment.
    2. Perform input validation on these inputs from user
This section may use input from the following related py files:
- keys.py for user credentials
This section may be a feeder to the following py files:
- OpenAI model selector based on search type desired
- OpenAI cost projector and guardrails doc
- OpenAI Prompt Generator
Possibly create a user interface down the road
'''

'''
2. Model selector:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
This py file will select the appropriate model based on the users indicated search type
- may be multi-level using one model to narrow down data to only items of interest
- more robust model then used to analyze those records more thoroughly
'''


'''
3. Prompt Generator:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Using some pre-written elements and some dynamically generated text, prompt will be generated.
The following functionality should be built into prompt generator
- Dynamically determine tables and fields to be include in prompt based on user 
        description of suspicious activity and prewritten tables/fields map (check how Josh
        is doing this)
- Instructs first level results to narrow down to items of interest to be fed into deep level
        prompt
- I believe this should create the prompt as an instance of a class, feed code to ChatGPT to
        analyze after code is written
- This may need to go before model selector
- To be continued????????????        
'''


'''
4. KQL Query generator:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Takes prompt and generates a KQL query
- Will most likely be class based
- Will most likely automatically be written to the final report
'''


'''
5. Guardrails file:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Will check final query results to ensure execution is within user permissions
- check against cost threshold to ensure costs are in a controlled range
- ensure no data access permissions are being violated
- consider making a list of allowed users or user group permissions and this user is
    part of that group and make sure execution is stopped if user is part of another user group
'''


'''
6. Query execution and results::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Constructed query will execute and detailed information about threats will be analyzed for
    report generation
- Mitre Att&ck module/class may be called at this stage
- Mitre Att&ck may be built into prompt
'''


'''
7. Report Generation
Will return results of query to the user in some format, possibly pdf. Will include:
- Original Prompt fed to models
- Copy of the KQL query that was constructed
- Items of interest from resulting data
- MITRE ATT&CK info on items of interest
- Recommended next steps to resolve items of interest'''