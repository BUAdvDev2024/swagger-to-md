# Swagger-to-md.py
A python script to convert your OpenAPI endpoint data to human-readable docs!

## How to use
1) Clone repository
2) Open terminal of your choosing
3) Run `python swagger-to-md.py [your api services' name] [path to source swagger json file] [path to output directory + name of output file]`
    <br>i.e. `python swagger-to-md.py 'My Awesome API' 'test-swagger.json' 'output.md'`
4) Let the script execute, then navigate to the output file and add it to your repository!

## How do I get a swagger.json file?
Your API project must be using swagger
1) Run your API server with swagger enabled and on the swagger index page, there should be a link below the name of your API server like this `http://localhost:5114/swagger/v1/swagger.json`
2) Navigate to that link and save the json file to your machine
3) Pass the file path of that save file in when running the script

## Reporting Issues / Features
Please keep in mind this is a simple script I put together and isn't meant to fully document everything/account for every edgecase.
However, please feel free to report any major issues on the issues page, along with any features you'd like to request.

## Contributing
Feel free to create a branch and make any changes you'd like, then make a pull request when you're ready to push.

