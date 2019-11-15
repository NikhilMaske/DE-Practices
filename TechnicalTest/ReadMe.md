
# Technical Test 

## Question 1.

Provided below two sets of representation, create a parser which can take both types of data and create pandas dataframe with all available information.


    Data 1: 
        ```{
            "name":"Harry Potter",
            "age":"29y 11m 23d",
            "mobile":"4562341234"
            "mobile_country_code":"+1",
            "status":"married"    
        }```

    Data 2: 
        ```{
            "name":{
                "first_name":"Harry",
                "last_name":"Potter"
            },
            "dob":"18 Nov 1889",
            "mobile":"+14562341234",
            "nationality":"American"
        }```

#Question 2

Find the rows from above created dataframe where Age is 25 years or older. [Hint] : ```df[df.age == '29']```

#Question 3

Save the data in CSV format from Dataframe [Hint] : ```df.to_csv(''test.csv)```


#Getting Started

1. Add your json files in source folders in current directory where parser.py exist
2. Run parser.py 
```python parser.py```